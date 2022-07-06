from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
# For using sleep function in python
import time

from selenium.webdriver.common.keys import Keys

# Create a new instance of the webdriver
browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
browser.get('https://www.twitter.com/')

# Let's the user see and also load the element
time.sleep(2)

login =  browser.find_elements_by_xpath('//*[@id="doc"]/div[1]/div/div[1]/div[2]/a[3]')

# Using the click function to click on the element
login[0].click()

print("Login in Twitter")

user = browser.find_element_by_xpath('//*[@id="login-dialog-dialog"]/div[2]/div[2]/div[2]/form/div[1]/input')

# Enter user name
user[0].send_keys('USER-NAME')

user = browser.find_element_by_xpath('//*[@id="login-dialog-dialog"]/div[2]/div[2]/div[2]/form/div[2]/input')

# Reads password from text file because
# Saving the password in a script
with open('password.txt', 'r') as f:
    password = f.read().replace('\n', '')
user.send_keys(password)

LOG = browser.find_element_by_xpath('//*[@id="login-dialog-dialog"]/div[2]/div[2]/div[2]/form/div[3]/button')
LOG[0].click()
print("Logged in Twitter")
time.sleep(5)

elem = browser.find_element_by_name("q")
elem.click()
elem.clear()

elem.send_keys("Python programmer")

elem.send_keys(Keys.RETURN)
print("Search Successful")

browser.close()