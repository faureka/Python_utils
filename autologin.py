from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get('https://netaccess.iitm.ac.in/account/login')

username = ''
pwd = ''

usn = driver.find_element_by_id('username')
paswd = driver.find_element_by_id('password')

usn.send_keys(username)
paswd.send_keys(pwd)

driver.find_element_by_name("submit").click()
driver.get('https://netaccess.iitm.ac.in/account/approve')

radio_button = driver.find_element_by_xpath("//input[@name ='duration' and @value = '2']").click()
# radio_button.click()

driver.find_element_by_name("approveBtn").click()
driver.get('file:///C:/Users/stifler/Downloads/study material/OCW/UN data Analysis/Python_utils/message.html')
# driver.implicity_wait(10)

time.sleep(3)
driver.quit()
