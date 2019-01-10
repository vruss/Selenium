# /home/simon/.mozilla/firefox/f64wwqg7.default/
# https://cas2.miun.se/cas/login?service=https%3A%2F%2Fportal.miun.se%2Fc%2Fportal%2Flogin%3Fredirect%3D%252Fgroup%252Fstudent%26p_l_id%3D10634
# http://stanford.edu/~mgorkove/cgi-bin/rpython_tutorials/Scraping_a_Webpage_Rendered_by_Javascript_Using_Python.php 
# https://medium.freecodecamp.org/better-web-scraping-in-python-with-selenium-beautiful-soup-and-pandas-d6390592e251

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

## Selenium for chromium
browser = webdriver.Chrome("./chromedriver") # Replace with .Firefox()
url = "https://portal.miun.se/group/student/my-schedule?p_p_id=miunmyscheduleportlet_WAR_miunmyscheduleportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&_miunmyscheduleportlet_WAR_miunmyscheduleportlet_tabs1=grouproom" 
browser.implicitly_wait(10) # seconds
browser.get(url) # Try to navigate to schedule page

##selenium for firefox
# profile = FirefoxProfile("/home/simon/.mozilla/firefox/jjen2epc.selenium") ##select folder for firefox profile
# browser = webdriver.Firefox(firefox_profile=profile) #load the firefox driver with the profile

### LOGIN
usernameBox = browser.find_element_by_id("username") # Username form field
passwordBox = browser.find_element_by_id("password") # Password form field

usernameBox.send_keys(config.username)
passwordBox.send_keys(config.password)

submitButton = browser.find_element_by_name("submit") 
submitButton.click() 

### SELECT CAMPUT
select = Select(browser.find_element_by_id('_miunmyscheduleportlet_WAR_miunmyscheduleportlet_pCampus'))
select.select_by_visible_text("Sundsvall")

### COLLECT DATA
time.sleep(2) # Wait for rooms to load
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

# text_file = open("index.html", "w")
# text_file.write(innerHTML)
# text_file.close()


