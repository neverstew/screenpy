from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def new_chrome():
    return webdriver.Remote(
          command_executor='http://localhost:4444/wd/hub',
          desired_capabilities=DesiredCapabilities.CHROME)


chromes = [new_chrome() for i in range(5)]

for chrome in chromes:
    chrome.get('https://www.google.com')
    print(chrome.title)
    chrome.quit()
