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
		gecko = "/home/rowan/geckodriver"
		self.driver = webdriver.Firefox(executable_path =gecko)

	def load_craigslist_url(self):
		self.driver.get(self.url)
		self.delay = 3
		try:
			wait=WebDriverWait(self.driver, self.delay)
			wait.until(EC.presence_of_element_location(By.ID, "searchform"))
			print("Ready")
		except TimeoutException:
			print("Loading took too long")



postal="94501"
max_price="1000"
radius="5"

scraper = CraigslistScraper(postal,max_price,radius)
scraper.load_craigslist_url()
# scraper.extract_post_titles()
# scraper.extract_post_urls()
# scraper.quit()

