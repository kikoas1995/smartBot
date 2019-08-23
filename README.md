# smartBot
_A try to make a bot sufficiently clever to bypass bot detection algorithms of common webpages_
![alt text](http://url/to/img.png)
## Pre-requisites 📋
Before using, it is neccessary to install the following packages:

```
pip install -r smartBotReqs.txt
```
## Usage
This tool is used as an interactive shell, where you can launch a bot which creates an anonymous aaccount in a hidden-service.The main screen is:
'''
                           _   ____        _   
  ___ _ __ ___   __ _ _ __| |_| __ )  ___ | |_ 
 / __| '_ ` _ \ / _` | '__| __|  _ \ / _ \| __|
 \__ \ | | | | | (_| | |  | |_| |_) | (_) | |_ 
 |___/_| |_| |_|\__,_|_|   \__|____/ \___/ \__|
                                               
smartBot >>> help
Usage:
	help:	Show this message
	register <name of service> [--hidden] [--tor]: Register an anonymous user in a service and save it into local database
	comment <name of service>  [--hidden] [--tor]: post a comment with an anonymous user in a service
  hiddenservice <start|stop> [--daemon] Launch a hidden service showing the contents of the users DB
	quit:	Exit the program
smartBot >>> 
'''
## Developed with

This tool has been built using of the following librarie and frameworks: 

* [Selenium](http://www.dropwizard.io/1.0.2/docs/) - This library has been used to automatize tasks in web services.
* [Flask](https://maven.apache.org/) - Used to deploy the hidden web-service
* [Stem](https://rometools.github.io/rome/) - Used to create tor relays and to launch the hidden service

## License

This work is under Creative Commons Attribution – NonCommercial – NoDerivatives.

<img src="https://co.creativecommons.org/wp-content/uploads/2008/02/by-nc-nd.png" height="70" width="200">
