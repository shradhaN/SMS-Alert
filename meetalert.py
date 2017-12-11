from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

driver = webdriver.Firefox()

driver.get("http://www.meet.net.np/meet/")

driver.find_element_by_class_name("elgg-input-text").send_keys("shradhaN")
driver.find_element_by_class_name("elgg-input-password").send_keys("Hello1234")
driver.find_element_by_id("loginImage").click()

time.sleep(1)

#driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[2]/div[2]/a/div").click()

driver.get("http://www.meet.net.np/meet/sms/sms")

driver.find_element_by_name("sendsmsbutton").click()

time.sleep(1)

driver.find_element_by_name("recipient").send_keys('9860333434')
driver.find_element_by_id("message").send_keys("hello, message here")
driver.find_element_by_name("sendbutton").click()

driver.find_element_by_name("sendsmsbutton").click()
