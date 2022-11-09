"""
carsales.py v0.1

Overview: Scrapes the number of cars for sale on carsales.com.au, and stores in a csv file.
Author: Daniel Hussey
Usage: python carsales.py

"""

import requests
import csv
from selenium import webdriver

# Get the html from the page using a Selenium webdriver (Chrome)
url = 'https://www.carsales.com.au/cars/'
driver = webdriver.Chrome(executable_path="./chromedriver")
r = driver.get(url)
html = driver.page_source
driver.quit()

# Find the number of cars for sale
# First extract the text in the <h1> tag with class 'title'
text = html.split('class="title">')[1].split('</h1>')[0].strip('\n').lstrip(' ').rstrip(' ')
# Then extract the number of cars for sale from the text (first space separated 'word')
num_cars = text.split(' ')[0].replace(',', '')

# Write the number of cars to a csv file along with the current date in a new row
import datetime
curr_date = datetime.datetime.now().strftime("%Y-%m-%d")
with open('carsales.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow([num_cars, curr_date])

# Print the number of cars to the console
print(num_cars)



