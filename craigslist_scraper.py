from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

import smtplib

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
		self.delay = 2
		try:
			wait=WebDriverWait(self.driver, self.delay)
			wait.until(EC.presence_of_element_located((By.ID, "searchform")))
			print("Ready")
		except TimeoutException:
			print("Loading took too long")

	def extract_post_titles(self):
		all_posts = self.driver.find_elements_by_class_name("result-row")
		post_title_list = []
		for post in all_posts:
			print(post.text)
			post_title_list.append(post.text)

	def extract_post_urls(self):
		url_list = []
		html_page = urllib.request.urlopen(self.url)
		soup = BeautifulSoup(html_page, "lxml")
		for link in soup.findAll("a", {"class": "result-title hdrlnk"}):
			url_list.append(link["href"])
		return url_list

	def quit(self):
		self.driver.close()

	# def send_email():
	# 	server = smtplib.SMTP('smtp.gmail.com', 587)
	# 	server.ehlo()
	# 	server.starttls()
	# 	server.ehlo()

	# 	server.login({config.email}, {config.password})

	# 	subject = "COVID news"
	# 	body = ""
	# 	msg = f"Subject: {subject} \n\n {body}"

	# 	server.sendmail(
	# 			{config.email},
	# 			{config.email},
	# 			msg
	# 		)
	# 	server.quit()

postal="94501"
max_price="1000"
radius="5"

scraper = CraigslistScraper(postal,max_price,radius)
scraper.load_craigslist_url()
scraper.extract_post_titles()
scraper.extract_post_urls()
# scraper.send_email()
scraper.quit()

