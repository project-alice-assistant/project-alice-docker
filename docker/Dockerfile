FROM python:3.7-slim-buster

#Speed up debugging with a bit of local caching
#RUN echo 'Acquire {Retries "0";HTTP { Proxy "http://ha:8000"; }; };' >> /etc/apt/apt.conf.d/00squidproxy
#RUN mkdir -p ~/.pip && echo [global] > ~/.pip/pip.conf && echo index-url = http://ha:3141/root/pypi/+simple/ >> ~/.pip/pip.conf && echo trusted-host = ha >> ~/.pip/pip.conf

#Change the timezone to your current timezone!
ENV TZ=Europe/London
ENV TERM=screen-256color

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

ADD ./resources/ProjectAlice.yaml /boot/ProjectAlice.yaml
ADD ./resources/initializer.py /initializer.py
ADD ./resources/systemctl /systemctl
ADD ./resources/start-alice.sh /start-alice.sh
ADD ./resources/update-alice-config-from-environment-vars.sh /update-alice-config-from-environment-vars.sh

RUN set -x && \
        rm /usr/bin/systemctl -f && \
        mv /systemctl /usr/bin/systemctl && \
        chmod +x /usr/bin/systemctl && \
        chmod +x /update-alice-config-from-environment-vars.sh

RUN set -x && \
        cd ~/ && \
	git clone https://github.com/project-alice-assistant/ProjectAlice.git && \
        cd ~/ProjectAlice/ && \
        . ~/.bashrc && \
        python3.7 main.py && \
        cp /initializer.py ~/ProjectAlice/ && \
        ./venv/bin/python initializer.py && \
        cd /home && \
        ln -s /root root && \
        mv ~/ProjectAlice ~/ProjectAliceBase && \
        mkdir -p /root/ProjectAlice

CMD ["bash","/start-alice.sh"]

#Build & Test commands
 #docker build . --tag alice:latest --no-cache
 #docker run -it --name alice -e ALICE_CONFIG_disableSoundAndMic=true --net=host alice:latest
 #docker run -v ~/docker/ProjectAlice:/root/ProjectAlice -it --name alice -e ALICE_CONFIG_disableSoundAndMic=true --net=host alice:latest
