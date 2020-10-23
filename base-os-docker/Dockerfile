FROM python:3.7-slim-buster

#Change the timezone to your current timezone!!
ENV TZ=Europe/London

RUN set -x && \
        ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN set -x && \
        apt-get update && apt-get upgrade -y --allow-unauthenticated && apt-get dist-upgrade -y --allow-unauthenticated

RUN set -x && \
        apt-get install -y git python3-toml gcc python3-dev wget sudo jq

RUN set -x && \
        pip3 install psutil

RUN set -x && \
        pip3 install pyyaml

RUN set -x && \
        pip3 install toml

RUN set -x && \
        pip3 install setuptools-rust

RUN set -x && \
        pip3 install virtualenv

RUN set -x && \
        echo "alias python3='python3.7'\nalias pip='pip3.7'" >> ~/.bashrc

ADD ./resources/systemctl /systemctl

RUN set -x && \
        rm /usr/bin/systemctl -f && \
        mv /systemctl /usr/bin/systemctl && \
        chmod +x /usr/bin/systemctl
