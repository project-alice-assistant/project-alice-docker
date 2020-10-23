# Project Alice's Docker

## How to run Alice

### Headless

You can run Alice headless very simply using the following docker-compose file:

```
---
version: "2"
services:
  alice-base:
    image: assistantprojectalice/main-unit:latest
    container_name: alice-base
    network_mode: host
    environment:
      - ALICE_CONFIG_disableSoundAndMic=true
    restart: unless-stopped
    tty: true
    stdin_open: true
  mosquitto:
    image: eclipse-mosquitto
    container_name: mosquitto
    ports:
      - 1883:1883
      - 8883:8883
    volumes:
      - mosquitto-data:/mosquitto/data
      - mosquitto-logs:/mosquitto/logs
      - mosquitto-conf:/mosquitto/config
    restart: unless-stopped
```

## How to configure Alice

Alice's config.json file supports all sorts of magic that you may wish to change, as such the Docker allows you to set any value you want inside the config file using the following Environment variable format:
```
ALICE_CONFIG_yourVariableName=YourValue
```
You can also set sub-variables using the hyphen character (_), as follows:
```
ALICE_CONFIG_yourRootVariable_yourChildVariable_goForeverIfYouWant=YourValue
```
For example:
```
    environment:
      - ALICE_CONFIG_disableSoundAndMic=true
      - ALICE_CONFIG_supportedLanguages_en_defaultCountryCode=GB
```
