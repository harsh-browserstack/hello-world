import os

from selenium import webdriver

username = os.getenv("BROWSERSTACK_USERNAME")
access_key = os.getenv("BROWSERSTACK_ACCESS_KEY")
browserstack_local = os.getenv("BROWSERSTACK_LOCAL")
browserstack_local_identifier = os.getenv("BROWSERSTACK_LOCAL_IDENTIFIER")

caps = {
 'os': 'Windows',
 'browser': 'chrome',
 'browserstack.local': browserstack_local,
 'browserstack.localIdentifier': browserstack_local_identifier,
 'browserstack.user': username,
 'browserstack.key': access_key
}

driver = webdriver.Remote(
    command_executor='http://hub-cloud.browserstack.com/wd/hub',
    desired_capabilities=caps)

driver.get("https://www.google.com")
driver.get_cookies()
time.sleep(5)
