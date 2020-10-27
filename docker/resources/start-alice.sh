#!/bin/bash

/update-alice-config-from-environment-vars.sh

apt-get update -y

cd ~/ProjectAlice
./venv/bin/python main.py
