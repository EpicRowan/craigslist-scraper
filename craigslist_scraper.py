from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup
import urllib.request

class CraigslistScraper(object):
	def __init__ (self, postal, max_price, radius):
		self.postal = postal
		self.max_price = max_price
		self.radius = radius

		self.url = f"https://sfbay.craigslist.org/search/sss?search_distance={radius}&postal={postal}&max_price={max_price}"

	def test(self):
		print(self.url)

postal="94501"
max_price="1000"
radius="5"

scraper = CraigslistScraper(postal,max_price,radius)
scraper.load_craigslist_url()
scraper.extract_post_titles()
scraper.extract_post_urls()
scraper.quit()

scraper.test()
