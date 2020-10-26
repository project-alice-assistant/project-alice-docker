# Project Alice's Docker

The GitHub repository for this image can be found here:

https://github.com/project-alice-assistant/project-alice-docker

## What is Project Alice?

Project Alice is an open source, privacy-driven voice assistant, but here is not the best place to find out about what she can do.

To find out all about Alice and what she can do, please see the main website:

https://docs.projectalice.io/

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

### Versioning

Alice often has a range of working and developmental versions for you to try/use. It is recomended of course that the master/latest version is used as a general practice, however we do try to provide images for variouse other builds where feasible for you to test from.

The different versions of Alice are made available using Image Tags, as detailed below.

Ultimately, you can switch the version Alice is running from within the running cintainer if you wish, however to help try to provide a simpler deployment experience, see the following list of supported versions of Alice for you to take advantage of.

Tag(s) | Alice Version | Status | Description
------------ | ------------- | ------------- | -------------
latest | Master | Ongoing | This image contains the main release branch that is used to deploy Alice.
dev | 1.0.0-b4 | Ongoing | This image contains the most recent official development branch (e.g. alpha, beta, etc.).
1.0.0-b4 | *Per the tag* | Static | These images contain the code for the specified version of Alice (i.e. the tag is the branch name). These are rolled out for use as requested and/or as they are produced.

#### How to get new versions included

Just hop on over to discord or raise and issue on this GitHub repository and someone will be in touch to discuss or assist.

#### How to run the Beta

This is very simple, just pull the dev tag as follows:

```
    image: assistantprojectalice/main-unit:dev
```

Congrats, you are now running the Beta.

## How to configure Alice

Alice's config.json file supports all sorts of magic that you may wish to change, as such the Docker allows you to set any value you want inside the config file using the following environment variable format:
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

## Supported Platforms

Currently, the following platforms are supported. If the platform you want to use is not currently supported, please check the 'in production' list and let us know if your desired platform is not included and we will see what we can do to introduce it for you.

Currenlty supported:

* ARM v6
* ARM v7
* AMD 64

In production we currently have the following platforms (which we hope to have working at some point):

* Intel 386

Note: If you want to try to add compatabilty for a new platform yourself, please feel free and post your working build into a branch for us to review.

All help is welcome! :-)
