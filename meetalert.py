from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

message = raw_input("message")

driver = webdriver.Firefox()

driver.get("http://www.meet.net.np/meet/")

#group1 = "9843589187,9841330080,9860090688,9813168004,9849809814,9845630544,9846646784,9803134711,9860178868,9840013962"
group2 = "9867040646,9862006834,9849619208,9808901349,9860333434,9818685920,9808244261,9845596796,9808775604,9808775604"

group1 = "9843589187,9841330080,9860090688"
driver.find_element_by_class_name("elgg-input-text").send_keys("shradhaN")
driver.find_element_by_class_name("elgg-input-password").send_keys("Hello1234")
driver.find_element_by_id("loginImage").click()

time.sleep(1)

#driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[2]/div[2]/a/div").click()

driver.get("http://www.meet.net.np/meet/sms/sms")

driver.find_element_by_name("sendsmsbutton").click()

time.sleep(1)

driver.find_element_by_name("recipient").send_keys(group1)
driver.find_element_by_id("message").send_keys(message)
driver.find_element_by_name("sendbutton").click()


