from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

#Message
message = raw_input("message")

#driver = webdriver.Firefox()
#driver.get("http://www.meet.net.np/meet/")

#phone numbers of club members
group1 = "9843589187,9841330080,9860090688,9849809814,9845630544,9846646784,9860178868,9840013962"
# Manish(9813168004) and Sonika(9803134711) not included in group 1
group2 = "9867040646,9862006834,9849619208,9860333434,9845596796,9840369998,9860610233"
#Sajesh(9808775604), Srijan(9808901349) not in group 2 (changed numbers of Anushka and Suravi)

#Login
def login(username,password,group):
	driver = webdriver.Firefox()
	driver.get("http://www.meet.net.np/meet/")
	driver.find_element_by_class_name("elgg-input-text").send_keys(username)
	driver.find_element_by_class_name("elgg-input-password").send_keys(password)
	driver.find_element_by_id("loginImage").click()
	time.sleep(1)

	
	#Send Message
	driver.get("http://www.meet.net.np/meet/sms/sms")
	driver.find_element_by_name("sendsmsbutton").click()
	time.sleep(1)
	driver.find_element_by_name("recipient").send_keys(group)
	driver.find_element_by_id("message").send_keys(message)
	driver.find_element_by_name("sendbutton").click()
	#close the browser
	time.sleep(1)
	driver.quit()

login('shradhaN', 'Hello1234', group1)
time.sleep(1)
#reopen the browser with new username and password
login('Anushka12', 'Smileanna', group2)


