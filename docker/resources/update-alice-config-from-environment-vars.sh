#!/bin/bash

CONFIG_FILE_PATH="/root/ProjectAlice/config.json"

# Load the config json file ready for editing
CONFIG_JSON=`cat ${CONFIG_FILE_PATH}`

# Parse all environment variables beginning with ALICE_CONFIG_ to generate config.json
# For each matching line
#  - Get property name from beggining to first = sign
#    - Remove ALICE_CONFIG_ from beginning
#    - Convert _ to .
#  - Get property value from everything after first = sign
# Examples
#  - ALICE_CONFIG_disableSoundAndMic=true
#    disableSoundAndMic=true
for P in `printenv | grep '^ALICE_CONFIG_'`
do
  PROP_NAME=${P%%=*}
  PROP_VALUE=${P##${PROP_NAME}=}
  PROP_NAME=${PROP_NAME#*_}
  PROP_NAME=${PROP_NAME#*_}
  PROP_NAME=`echo ${PROP_NAME} | tr "_" "."`
  echo -e "\t${PROP_NAME}=${PROP_VALUE}"
  CONFIG_JSON=`jq ".${PROP_NAME} = \\\$newVal" --arg newVal ${PROP_VALUE} <<<"$CONFIG_JSON"`
done

echo $CONFIG_JSON > $CONFIG_FILE_PATH
