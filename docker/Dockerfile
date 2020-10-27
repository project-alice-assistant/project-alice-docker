FROM wraithrmm/alice-base-os:latest

ADD ./resources/ProjectAlice.yaml /boot/ProjectAlice.yaml
ADD ./resources/initializer.py /initializer.py

RUN set -x && \
        cd ~/ && \
	git clone https://github.com/project-alice-assistant/ProjectAlice.git
        cd ~/ProjectAlice/ && \
        . ~/.bashrc && \
        python3.7 main.py
        cp /initializer.py ~/ProjectAlice/ && \
        ./venv/bin/python initializer.py && \
        cd /home && \
        ln -s /root root

ADD ./resources/start-alice.sh /start-alice.sh
ADD ./resources/update-alice-config-from-environment-vars.sh /update-alice-config-from-environment-vars.sh

CMD ["bash","/start-alice.sh"]
