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
RUN apt-get -y install build-essential git python-pip python-dev python-lxml libxml2-dev libxslt1-dev python-bcrypt libpq-dev unoconv postgresql postgresql-server-dev-all libsasl2-dev libssl-dev libffi-dev libldap2-dev python-setuptools nodejs npm && \
    easy_install pip


# Install utility scripts, Trytond, download all Trytond modules, SAO
WORKDIR /tryton  # ...
RUN git clone https://github.com/semilimes/trytond-scripts.git && \
    pip install -r trytond-scripts/requirements_tryton.txt && \
    git clone -b $TRYTON_VER https://github.com/tryton/trytond.git
WORKDIR /tryton/trytond
RUN python setup.py install

WORKDIR /tryton/trytond-scripts
RUN apt-get install wget && \
    /tryton/trytond-scripts/download_all_modules.sh $TRYTON_VER && \
    python /tryton/trytond-scripts/generate_config.py

WORKDIR /tryton
RUN apt-get install npm && \
    npm install -g bower grunt grunt-cli && \
    git clone https://github.com/tryton/sao.git
WORKDIR sao
RUN npm install && \
    ln -s /usr/bin/nodejs /usr/bin/node && \
    bower install --allow-root && \
    grunt --force

# Config path and admin db pswd path (deleted after initialization)
ENV TRYTOND_CONFIG /tryton/config.ini
ENV TRYTONPASSFILE /tryton/TRYTONPASSFILE.ini


EXPOSE 8000
CMD ["-c", "/tryton/config.ini", "-v"]
ENTRYPOINT ["/usr/local/bin/trytond"]
