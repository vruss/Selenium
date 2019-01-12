import getpass
import sys
from json import JSONEncoder
import json
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import argparse


# Class used to store credentials
class Creds:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    username = ""
    password = ""

# Custom JSON Encoder to serialize object for json
class CredsEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Creds):
            return (
                obj.username,
                obj.password
            )
        else:
            return super(CredsEncoder, self).default(object)


### ARGUMENT PARSING
parser = argparse.ArgumentParser()
# Argument group
fileGroup = parser.add_mutually_exclusive_group() 
parser.add_argument("-q", "--quit", help="exit browser after it's done", 
    action="store_true")
fileGroup.add_argument("-i", "--input", help="load json file with credentials")
fileGroup.add_argument("-o", "--output", help="save credentials to a json file")

# Parse the arguments, if statements make args optional
args = parser.parse_args() 


## Using input
if args.input:
    # Open input file args.file
    with open(args.input, 'r') as json_file:
        data = json.load(json_file)        
        # Create config object with username and password
        config = Creds(data[0], data[1])
else:
    config = Creds(raw_input("Enter username: "), getpass.getpass("Enter password: "))

# Using output
if (args.output):
    # Open output file
    with open(args.output, 'w') as output_file:
        json.dump(config, output_file, indent=4, cls=CredsEncoder)
    

## Selenium for chromium
browser = webdriver.Chrome("./chromedriver") # Replace with .Firefox()
url = "https://portal.miun.se/group/student/my-schedule?p_p_id=miunmyscheduleportlet_WAR_miunmyscheduleportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&_miunmyscheduleportlet_WAR_miunmyscheduleportlet_tabs1=grouproom" 
browser.implicitly_wait(10) # seconds
browser.get(url) # Try to navigate to schedule page


### LOGIN
usernameBox = browser.find_element_by_id("username") # Username form field
passwordBox = browser.find_element_by_id("password") # Password form field

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

if args.quit:
    browser.quit()