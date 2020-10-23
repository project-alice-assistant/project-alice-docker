FROM wraithrmm/alice-base-os:latest

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

ADD ./resources/start-alice.sh /start-alice.sh
ADD ./resources/update-alice-config-from-environment-vars.sh /update-alice-config-from-environment-vars.sh

RUN set -x && \
        apt-get clean && \
        apt-get -y auto-remove && \
        rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN set -x && \
        cd /home && \
        ln -s /root root

CMD ["bash","/start-alice.sh"]
