import getpass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support.ui import Select
import time

### Create config.py AND add it to your .gitignore file before commiting
### Make 2 rows:    username = "username"
###                 password = "password"
import config 

# usrn = input("Enter username: ")
# pswd = getpass.getpass("Enter password: ")

## Selenium for chromium
browser = webdriver.Chrome("./chromedriver") # Replace with .Firefox()
url = "https://portal.miun.se/group/student/my-schedule?p_p_id=miunmyscheduleportlet_WAR_miunmyscheduleportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&_miunmyscheduleportlet_WAR_miunmyscheduleportlet_tabs1=grouproom" 
browser.implicitly_wait(10) # seconds
browser.get(url) # Try to navigate to schedule page


### LOGIN
usernameBox = browser.find_element_by_id("username") # Username form field
passwordBox = browser.find_element_by_id("password") # Password form field

# usernameBox.send_keys(usrn)
# passwordBox.send_keys(pswd)
usernameBox.send_keys(config.username)
passwordBox.send_keys(config.password)

submitButton = browser.find_element_by_name("submit") 
submitButton.click() 

### SELECT CAMPUS
select = Select(browser.find_element_by_id('_miunmyscheduleportlet_WAR_miunmyscheduleportlet_pCampus'))
select.select_by_visible_text("Sundsvall")

### COLLECT DATA
time.sleep(2) # Wait for rooms to load

calenderButton = browser.find_element_by_id("calInput")
calenderButton.click()

calender = browser.find_element_by_class_name("yui3-calendar-content")
# TODO: click a number

innerHTML = browser.execute_script("return document.body.innerHTML") # Returns the inner HTML as a string

searchString = "data-description"
searchUntil = "aria-controls"
findReserv = "reserved"
amountOfBookings = innerHTML.count(findReserv) # Find all occurences of "reserved"
begin = 0
i = 0
length = 15

while(i < amountOfBookings):
    begin = innerHTML.find(searchString,begin) # Finds the start of booking data
    length = innerHTML.find(searchUntil,begin) # Finds the end of booking data
    begin = begin + len(searchString) + 2
    subS = innerHTML[begin:length] # Substring containing booking data
    print(subS)
    i += 1

# browser.quit()