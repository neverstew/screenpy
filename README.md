# Screenpy
Please see https://screenpy.readthedocs.io/en/latest/ for the latest user documentation.

## Included Tools
### Selenium Grid
This repository includes a sample selenium grid docker-compose definition file.

In a new terminal, launch a machine with docker installed and ensure that you can access the port 4444 from the host machine.
If doing this using the standard dev-tools vagrant machine, simply add another port-mapping to the `Vagrantfile`.

```commandline
cd <dev-tools-dir>
vagrant up
vagrant ssh
```
From the `ui-testing` directory, launch the containers.

```commandline
cd <ui-testing-dir>
docker-compose up
```
You should be able to see the output of the containers, including the node showing that it has connected to the hub.

## Tests
To verify your additions to the codebase, run

```commandline
pipenv run python -m pytest
```

### Browser Configuration
There are a number of environment variables that can be set to change the browser used to execute the tests.

 | Variable | Description |
 |----------|-------------|
 | SELENIUM_HUB_ADDRESS | Changes the address for the selenium hub. |
 | SELENIUM_DRIVER_TYPE | Changes the type of browser requested e.g. 'chrome', 'firefox' |
 | SELENIUM_BROWSER_TIMEOUT | Number of seconds a browser session is allowed to hang while a WebDriver command is running |
 | SELENIUM_CLEANUP | Specifies how often (in ms) the hub will poll running proxies for timed-out (i.e. hung) threads |
 | SELENIUM_TIMEOUT | Specifies the timeout before the server automatically kills a session that hasn't had any activity in the last X seconds. The test slot will then be released for another test to use. This is typically used to take care of client crashes. For grid hub/node roles, cleanUpCycle must also be set. |
 | APP_BASE_URL | Specifies the base url to use to locate the app. e.g. http://bbc.co.uk/ |
 
 For more options, the easiest summary can be found in [this thread](https://stackoverflow.com/questions/43395659/properties-for-selenium-grid-hub-node-config)

### Timeouts
#### Grid
The docker-compose file defining the grid sets some properties on the hub and nodes.  More information about what
environment variables match to each selenium configuration property can be found in the `Dockerfile`s of the images.

The nodes will shut down any browsers that have not received any commands for 60 seconds.  This helps as a fail safe
to ensure that sessions that hang due to driver/connection mishaps do not prevent the remainder of the tests from 
executing.

#### Drivers
The web drivers set an implicit wait time of 5 seconds.  In other words, whenever they try to load a page or find an
element on a page, they will wait for success for 5 seconds.  After this time, they will throw an error.