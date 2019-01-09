# /home/simon/.mozilla/firefox/f64wwqg7.default/
# https://cas2.miun.se/cas/login?service=https%3A%2F%2Fportal.miun.se%2Fc%2Fportal%2Flogin%3Fredirect%3D%252Fgroup%252Fstudent%26p_l_id%3D10634
# http://stanford.edu/~mgorkove/cgi-bin/rpython_tutorials/Scraping_a_Webpage_Rendered_by_Javascript_Using_Python.php 
# https://medium.freecodecamp.org/better-web-scraping-in-python-with-selenium-beautiful-soup-and-pandas-d6390592e251

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import time

##selenium for chromium
#options = webdriver.ChromeOptions()
#options.add_argument("google-chrome --user-data-dir=~/.config/chromium")
#browser = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", chrome_options=options)
## 
##selenium for firefox
profile = FirefoxProfile("/home/simon/.mozilla/firefox/jjen2epc.selenium") ##select folder for firefox profile
browser = webdriver.Firefox(firefox_profile=profile) #load the firefox driver with the profile

url = "https://portal.miun.se/group/student/my-schedule?p_p_id=miunmyscheduleportlet_WAR_miunmyscheduleportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&_miunmyscheduleportlet_WAR_miunmyscheduleportlet_tabs1=grouproom" #url for webbpage

browser.get(url) #navigate to page behind login not working since login fails
time.sleep(600) #sleep so i can enter login information and navigate the page
innerHTML = browser.execute_script("return document.body.innerHTML") #returns the inner HTML as a string

searchString = "data-description"
searchUntil = "aria-controls"
findReserv = "reserved"
amountOfBookings = innerHTML.count(findReserv) #find all occurences of "reserved"
begin = 0
i = 0
length = 15


while(i < amountOfBookings):
    begin = innerHTML.find(searchString,begin) #finds the start of booking data
    length = innerHTML.find(searchUntil,begin) #finds the end of booking data
    begin = begin + len(searchString) + 2
    subS = innerHTML[begin:length] #substring containing booking data
    print(subS)
    i += 1

browser.quit()

text_file = open("index.html", "w")
text_file.write(innerHTML)
text_file.close()
