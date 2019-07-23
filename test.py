from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

desired_cap = {
 'os_version':'11',
 'device':'iPhone 8 Plus',
 'realMobile': 'true',
 'build':'BroStacAutomation',
 'browserstack.debug':'true',
 'browserstack.local':'false'
}

print(os.environ['BROWSERSTACK_USERNAME'])
print(os.environ['BROWSERSTACK_ACCESS_KEY'])

driver = webdriver.Remote(
    command_executor='http://' + os.environ['BROWSERSTACK_USERNAME'] + ':' + os.environ['BROWSERSTACK_ACCESS_KEY'] + '@hub.browserstack.com:80/wd/hub',
    desired_capabilities=desired_cap)

driver.get("http://www.google.com")
print(os.environ['BROWSERSTACK_USERNAME'])
print(os.getenv("BROWSERSTACK_USERNAME"))


if not "Google" in driver.title:
    raise Exception("Unable to load google page!")
elem = driver.find_element_by_name("q")
elem.send_keys("BrowserStack")
elem.text
elem.submit()
driver.quit()