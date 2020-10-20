FROM wraithrmm/python-enabled-pi-os:latest

COPY qemu-arm-static /usr/bin

ARG UID=1000
ARG GID=1000

ENV GROUPID=$GID
ENV USERID=$UID

ENV USER=pi
ENV HOME=/home/$USER

#Change the timezone to your current timezone!!
ENV TZ=Europe/London

RUN set -x && \ 
	ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
	
RUN set -x && \
	apt-get update && apt-get upgrade -y --allow-unauthenticated && apt-get dist-upgrade -y --allow-unauthenticated
 
RUN set -x && \	
	apt-get install -y git sudo gnupg2 dirmngr

RUN set -x && \
        groupadd --gid ${GROUPID} ${USER} && \
        useradd --uid ${USERID} --gid ${GROUPID} --create-home --shell /bin/bash $USER && \
        echo 'export PATH="$PATH:$HOME/bin"' >> $HOME/.bashrc && \
        echo "$USER ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers && \
        chown -R $USER:$USER $HOME

RUN set -x && \
        cd ~/ && \
	git clone https://github.com/project-alice-assistant/ProjectAlice.git

RUN set -x && \
        sudo pip3 install psutil

RUN set -x && \
        sudo pip3 install pyyaml

#RUN set -x && \
#        apt-get install -y apt-transport-https zip unzip mpg123 dirmngr gcc make pkg-config automake libtool libicu-dev libpcre2-dev libasound2-dev portaudio19-dev python3-pyaudio mosquitto mosquitto-clients libxml2-dev libxslt-dev flac libatlas-base-dev gfortran ffmpeg

#RUN set -x && \
#        apt-get install -y dbus gir1.2-glib-2.0 libdbus-glib-1-2 libgirepository-1.0-1 libpython3-dev libpython3.5 libpython3.5-dev python-pip-whl python3-cffi-backend python3-crypto python3-cryptography python3-dbus python3-dev python3-gi python3-idna python3-keyring python3-keyrings.alt python3-pkg-resources python3-pyasn1 python3-secretstorage python3-setuptools python3-six python3-xdg python3.5-dev 

RUN set -x && \
        pip3.7 install virtualenv

ADD ./resources/start-alice.sh /start-alice.sh
ADD ./resources/ProjectAlice.yaml /boot/ProjectAlice.yaml

RUN set -x && \
        chown -R $USER:$USER $HOME

RUN set -x && \
        cd ~/ProjectAlice/ && \
        . ~/.bashrc && \
        python3.7 main.py

ADD ./resources/initializer.py /initializer.py

RUN echo -e '#!/bin/bash\necho hello "$@" >> /services-to-start.config' > /usr/bin/systemctl && \
        chmod +x /usr/bin/systemctl

RUN set -x && \
        cd ~/ProjectAlice/ && \
        cp /initializer.py ~/ProjectAlice/ && \
        ./venv/bin/python initializer.py && \
        cat /services-to-start.config

RUN set -x && \
        sudo apt-get install jq

ADD ./resources/update-alice-config-from-environment-vars.sh /update-alice-config-from-environment-vars.sh

ADD ./resources/systemctl /systemctl

RUN set -x && \
        rm /usr/bin/systemctl -f && \
        mv /systemctl /usr/bin/systemctl && \
        chmod +x /usr/bin/systemctl

RUN set -x && \
        chown -R $USER:$USER /usr/share/snips && \
        chown -R $USER:$USER /var/lib/snips && \
        apt-get clean && \
        apt-get -y auto-remove && \
        rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

USER $USER
WORKDIR $HOME

CMD ["bash","/start-alice.sh"]
