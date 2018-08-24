# ui-testing

This repository will store the testing framework used to write the UI-level tests.  It is still in the very 
early stages; approaches need to be fleshed out and tools developed.

The current resources allow you to launch a selenium grid and perform a basic test.  They require an
element of manual setup for them to work.

## Usage
This repo provides a friendlier way to write tests, based loosely upon [the scrrenplay pattern](https://serenity-js.org/design/screenplay-pattern.html).
It is primarily designed for use in conjunction with Selenium, but those modules are completely optional.

A simple test might look like


```python
class TestNavigation(TestCase):

    def setUp(self):
        self.eddy = Actor.called("eddy").who_can(BrowseTheWeb)
        self.eddy.attempts_to(OpenTheBBCWebsite())

    def test_navigation_to_news(self):
        self.eddy.attempts_to(
            Navigate.to_news()
        )

        heading = self.eddy.sees(
            Text.on(header.news)
        )

        self.assertEqual('BBC News', heading)

```


## Getting Started
### Download The Code
Clone this repo
```
git clone git@bitbucket.org:wspdigitaluk/ui-testing.git
```

### Launch the Selenium Grid
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

### Verify the virtual environment
Ensure you have pipenv installed on your host machine.  If not, grab it with `pip install pipenv`.

From the repo directory, initialise the virtual environment
```commandline
pipenv install
```

To make use of the virtual environment inside an IDE, ensure that you have set the python interpreter to use
the one created as part of the pipenv initialisation.  See your IDE docs for more guidance on this. 

### Verify integrity of the code/environment
To check all the steps have run so far, kick the unit tests off by running
```commandline
pipenv run python -m unittest
``` 

### Verify the selenium environment
To check that the selenium grid has been set up correctly, navigate to `screenpy.abilities.web.tests` 
and remove the `@skip` annotation from the test method.

Run this method using either the `unittest` CLI or your IDE.

If all is well, you should see the test pass.  There may be resource warnings.  These are being worked on.

## Configuring The Browser Tests
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
 