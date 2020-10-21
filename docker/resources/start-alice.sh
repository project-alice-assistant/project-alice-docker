#!/bin/bash

/update-alice-config-from-environment-vars.sh

cd ~/ProjectAlice
./venv/bin/python main.py
