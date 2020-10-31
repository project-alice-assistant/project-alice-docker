FROM python:3.7-slim-buster

#Change the timezone to your current timezone!
ENV TZ=Europe/London

RUN set -x && \
        ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN set -x && \
        sed -i -e's/ main/ main contrib non-free/g' /etc/apt/sources.list \
        && apt-get update \
        && apt-get upgrade -y --allow-unauthenticated \
        && apt-get dist-upgrade -y --allow-unauthenticated \
        && apt-get install -y git python3-toml gcc python3-dev wget sudo jq libttspico-utils

RUN set -x && \
        pip3 install psutil pyyaml toml setuptools-rust virtualenv wheel

RUN set -x && \
        echo "alias python3='python3.7'\nalias pip='pip3.7'" >> ~/.bashrc

ADD ./resources/systemctl /systemctl

RUN set -x && \
        rm /usr/bin/systemctl -f && \
        mv /systemctl /usr/bin/systemctl && \
        chmod +x /usr/bin/systemctl


