#libraries
from splinter import Browser
from bs4 import BeautifulSoup
import time

def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape_info():
    browsers = init_browser()
    #visit url
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    time.sleep(1)
    #scrape page into soup
    html = browser.html
    #beautiful soup object, parse with 'html.parser'
    soup = BeautifulSoup(html, "html.parser")
    #get ... info
