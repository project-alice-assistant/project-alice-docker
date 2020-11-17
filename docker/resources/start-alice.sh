#!/bin/bash


#If the mount folder is empty, copy ProjectAlice files to it just this once
if [ ! "$(ls -A /root/ProjectAlice)" ]; then
    echo "Staging ProjectAlice files for first run"
     cp -r /root/ProjectAliceBase/. /root/ProjectAlice/
fi

#Update alice config with the environmental variables from docker 
/update-alice-config-from-environment-vars.sh

#Needed so we can install dependencies on the fly
apt-get -qq update -y

#Start the show!
cd ~/ProjectAlice
./venv/bin/python main.py
