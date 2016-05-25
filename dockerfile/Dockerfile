# Trytond + all modules + SAO

FROM ubuntu:14.04
MAINTAINER Mikhail Savushkin <mikhail.savushkin@semilimes.com>

# Update package repository. Install Dependencies
RUN echo .
RUN apt-get update && \
    apt-get -y install language-pack-en zsh htop build-essential git python-pip python-dev python-lxml libxml2-dev libxslt1-dev python-bcrypt libpq-dev unoconv postgresql postgresql-server-dev-all libsasl2-dev libssl-dev libffi-dev libldap2-dev python-setuptools nodejs nodejs-legacy npm wget && easy_install pip

ENV DEBIAN_FRONTEND noninteractive
ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8


# Install SAO
RUN apt-get install npm
RUN npm install -g bower grunt grunt-cli
WORKDIR /tryton

##############################################
# EDIT THIS ENV VAR TO CHANGE TRYTON VERSION #
##############################################
ENV TRYTON_VER 4.0

# Continue installing SAO...
RUN git clone -b $TRYTON_VER https://github.com/tryton/sao.git
WORKDIR /tryton/sao
RUN npm install
RUN bower install --allow-root
RUN grunt --force

# Install utility scripts, Trytond, download all Trytond modules
WORKDIR /tryton
RUN pip install proteus==$TRYTON_VER
# install only 1 module for now, testing/debug mode
RUN git clone -b $TRYTON_VER https://github.com/semilimes/trytond-scripts.git && \
    /tryton/trytond-scripts/download_all_modules_pip.sh $TRYTON_VER && \
    pip install -r /tryton/trytond-scripts/requirements_tryton.txt  # .......

ENV TRYTOND_CONFIG /tryton/config.ini
ENV TRYTONPASSFILE /tryton/TRYTONPASSFILE.ini

EXPOSE 8000
# CMD ["-v"]
ENTRYPOINT ["/bin/bash", "/tryton/trytond-scripts/docker_entry_script.sh", "$TRYTOND_FIRST_RUN"]
