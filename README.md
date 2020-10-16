# Project Alice's Docker

## How to configure Alice

Alice's config.json file supports all sorted of magic that you may wish to change, as such the Docker allows you to set any value you want inside the config file using the following Environment variable format:
```
ALICE_CONFIG_yourVariableName: YourValue
```
You can also set sub-variables using the hyphen character (-), as follows:
```
ALICE_CONFIG_yourRootVariable-yourChildVariable-goForeverIfYouWant: YourValue
```
For example:
```
  - environment:
    ALICE_CONFIG_disableSoundAndMic: true
    ALICE_CONFIG_supportedLanguages_en_defaultCountryCode: GB
```
