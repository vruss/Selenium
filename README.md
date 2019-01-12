# Selenium
Python script for scraping MIUN room schedules.

## Prerequisites
1. You need the Google Chrome browser installed
2. You need to install selenium with ```pip install selenium ```

### Optional 
When using the input file argument you need to do the following:
1. Create a json file with credentials 
2. Add the json tile to your .gitignore file before commiting anything
3. The file should look like this    
```json
[
    "your_username", 
    "your_password"
]
```

### Sources
[Stanford University - Login system Guide](http://stanford.edu/~mgorkove/cgi-bin/rpython_tutorials/Scraping_a_Webpage_Rendered_by_Javascript_Using_Python.php)

[Freecodecamp - Guide to scraping with Beautiful Soup](https://medium.freecodecamp.org/better-web-scraping-in-python-with-selenium-beautiful-soup-and-pandas-d6390592e251)

[Beautiful Soup - Data scraping made easy](https://www.crummy.com/software/BeautifulSoup/)
