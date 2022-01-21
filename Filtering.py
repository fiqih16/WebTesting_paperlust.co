from time import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.Chrome()

driver.get("https://paperlust.co/")
driver.find_element_by_name("search").send_keys('wedding invitations',Keys.ENTER)
driver.find_element_by_xpath("//*[@id='search__container']/div/div/div/div/div[1]/div/div[1]/div[4]/div[2]/div/div/ul/li[1]/div").click()

#element = driver.find_element_by_css_selector("#search__container > div > div > div > div > div.grid-sm-9.grid-md-8.grid-lg-8.grid-xl-9 > div.mt-3 > div > div.mx-auto.my-3.grid-12.text-center > a").click()
#previous_height = driver.execute_script('return document.role.scrollHeight')
#driver.execute_script("window.scrollTo(0,900)")
button = driver.find_element_by_xpath('//*[@id="search__container"]/div/div/div/div/div[2]/div[2]/div/div[37]') # Selector might differs
button.location_once_scrolled_into_view
button.click()
#while True:
    #element.send_keys(Keys.PAGE_DOWN)
    #driver.execute_script('window.scrollTo(0, document.role.scrollHeight);')