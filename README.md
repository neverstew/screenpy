# ui-testing

This repository will store the testing framework used to write the UI-level tests.  It is still in the very 
early stages; approaches need to be fleshed out and tools developed.

The current resources allow you to spin up a selenium grid and small verification test.  They require an
element of manual setup for them to work.

## Getting Started
Clone this repo
```
git clone git@bitbucket.org:wspdigitaluk/ui-testing.git
```

Launch a machine with docker installed and ensure that you can access the port 4444 from the host machine.
If doing this using the standard dev-tools vagrant machine, simply add another port-mapping to the `Vagrantfile`.

From the `ui-testing` directory, launch the containers.  The test establishes 5 chrome nodes so we need to 
launch docker-compose with
```
docker-compose up --scale chrome=5 hub=1
```

Run the verification file with any python interpreter.  Ensure that you have the `selenium` python module 
(this is available using `pip`).
