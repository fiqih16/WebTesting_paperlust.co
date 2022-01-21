from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://paperlust.co/")
driver.find_element_by_name("search").send_keys('wedding invitations',Keys.ENTER)