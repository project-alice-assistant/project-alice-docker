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
        cd ~/ && \
	git clone https://github.com/project-alice-assistant/ProjectAlice.git

RUN set -x && \
        sudo pip3 install psutil

RUN set -x && \
        sudo pip3 install pyyaml

RUN set -x && \
        pip3 install toml

ADD ./resources/ProjectAlice.yaml /boot/ProjectAlice.yaml

RUN set -x && \
        echo -e '#!/bin/bash\necho hello "$@" >> /services-to-start.config' > /usr/bin/systemctl && \
        chmod +x /usr/bin/systemctl

RUN set -x && \
        pip3 install setuptools-rust

RUN set -x && \
        cd ~/ProjectAlice/ && \
        . ~/.bashrc && \
        python3.7 main.py

ADD ./resources/initializer.py /initializer.py

RUN set -x && \
        pip3.7 install virtualenv

RUN set -x && \
        echo "alias python3='python3.7'\nalias pip='pip3.7'" >> ~/.bashrc

RUN set -x && \
        cd ~/ProjectAlice/ && \
        cp /initializer.py ~/ProjectAlice/ && \
        ./venv/bin/python initializer.py && \
        cat /services-to-start.config

ADD ./resources/start-alice.sh /start-alice.sh
ADD ./resources/update-alice-config-from-environment-vars.sh /update-alice-config-from-environment-vars.sh
ADD ./resources/systemctl /systemctl

RUN set -x && \
        rm /usr/bin/systemctl -f && \
        mv /systemctl /usr/bin/systemctl && \
        chmod +x /usr/bin/systemctl

RUN set -x && \
        apt-get clean && \
        apt-get -y auto-remove && \
        rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN set -x && \
        cd /home && \
        ln -s /root root

CMD ["bash","/start-alice.sh"]
