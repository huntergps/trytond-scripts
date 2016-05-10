# Trytond + all modules + SAO

FROM ubuntu:14.04
MAINTAINER Mikhail Savushkin <mikhail.savushkin@semilimes.com>
ENV TRYTON_VER 3.8

# Update package repository
RUN apt-get update && \
    apt-get -y install language-pack-en zsh htop

ENV DEBIAN_FRONTEND noninteractive
ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

# Install Dependencies
RUN apt-get -y install build-essential git python-pip python-dev python-lxml python-bcrypt libpq-dev unoconv postgresql postgresql-server-dev-all libsasl2-dev libssl-dev libffi-dev libldap2-dev python-setuptools nodejs npm && \
    easy_install pip


# Install utility scripts, Trytond, all Trytond modules (and switch them to the appropriate version), SAO
WORKDIR /tryton
RUN git clone https://github.com/semilimes/trytond-scripts.git && \
    pip install -r trytond-scripts/requirements_tryton.txt && \
    git clone -b $TRYTON_VER https://github.com/tryton/trytond.git && \
    trytond-scripts/download_all_modules.sh && \
    trytond-scripts/change_modules_version.sh $TRYTON_VER && \
    python install_modules.py && \
    sudo apt-get install npm && \
    sudo npm install -g bower grunt grunt-cli && \
    git clone https://github.com/tryton/sao.git #no chache
WORKDIR sao
RUN npm install && \
    npm run postinstall && \
    bower install && \
    grunt
WORKDIR /tryton


EXPOSE 	8000
CMD ["-c", "/etc/trytond.conf", "-v"]
ENTRYPOINT ["/usr/local/bin/trytond"]
