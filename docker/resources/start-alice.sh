#!/bin/bash

/update-alice-config-from-environment-vars.sh

mosquitto &

cd ~/ProjectAlice
sleep 10000
#python3 main.py
