# Carsales Scraper

v0.1 Fetches the number of cars for sale nationally on carsales daily and stores in a csv file.

## Usage

`python carsales.py`

## Developer Log

### 2022-11-09

- Started project and added all files.
- Getting a weird response that looks like a bot blocker from carsales.com.au
    - Looking more like javascript needs to be executed rather than just trying to read html from the address
- Used Selenium to execute javascript and get the html
