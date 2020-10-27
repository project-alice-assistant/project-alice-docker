FROM wraithrmm/alice-base-os:latest

ARG tagName=1.0.0-d4
ARG channelName=beta

RUN set -x && \
        echo "deb http://deb.debian.org/debian buster main non-free" > /etc/apt/sources.list && \
        apt-get update && apt-get upgrade -y --allow-unauthenticated && apt-get dist-upgrade -y --allow-unauthenticated

RUN set -x && \
	apt-get install -y libttspico-utils

RUN set -x && \
        cd ~/ && \
	git clone https://github.com/project-alice-assistant/ProjectAlice.git

ADD ./resources/ProjectAlice.yaml /boot/ProjectAlice.yaml

RUN set -x && \
        cd ~/ProjectAlice/ && \
        . ~/.bashrc && \
        python3.7 main.py

ADD ./resources/initializer.py /initializer.py

RUN set -x && \
        cd ~/ProjectAlice/ && \
        cp /initializer.py ~/ProjectAlice/ && \
        ./venv/bin/python initializer.py

RUN set -x && \
        cd ~/ProjectAlice && \
        git checkout $tagName && \
        git pull

ADD ./resources/start-alice.sh /start-alice.sh
ADD ./resources/update-alice-config-from-environment-vars.sh /update-alice-config-from-environment-vars.sh

RUN set -x && \
        cd /home && \
        ln -s /root root

ENV ALICE_CONFIG_updateChannel=$channelName
ENV ALICE_CONFIG_skillUpdateChannel=$channelName

CMD ["bash","/start-alice.sh"]
