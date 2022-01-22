from ast import Break
from time import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://paperlust.co/")

driver.implicitly_wait(5)
driver.find_element_by_xpath('//*[@id="large-international-pl"]/div[2]').click()

driver.find_element_by_name("search").send_keys('wedding invitations',Keys.ENTER)
driver.implicitly_wait(5)
#driver.find_element_by_xpath("//*[@id='search__container']/div/div/div/div/div[1]/div/div[1]/div[4]/div[2]/div/div/ul/li[1]/div").click()
driver.find_element_by_xpath('//*[@id="search__container"]/div/div/div/div/div[1]/div/div[1]/div[4]/div[2]/div/div/ul/li[10]').click()

# driver.implicitly_wait(5)
# driver.find_element_by_xpath('//*[@id="large-international-pl"]/div[2]').click()

#element = driver.find_element_by_css_selector("#search__container > div > div > div > div > div.grid-sm-9.grid-md-8.grid-lg-8.grid-xl-9 > div.mt-3 > div > div.mx-auto.my-3.grid-12.text-center > a").click()
#previous_height = driver.execute_script('return document.role.scrollHeight')
#driver.execute_script("window.scrollTo(0,900)")
#driver.implicitly_wait(5)
BtnShowMore = driver.find_element_by_xpath('//*[@id="search__container"]/div/div/div/div/div[2]/div[2]/div/div[13]/a')
ScrollUp = driver.find_element_by_xpath('//*[@id="search-index"]/div[1]/div[1]/div[2]')

while True:
        driver.execute_script("arguments[0].scrollIntoView()",BtnShowMore)
        driver.implicitly_wait(2)
        BtnShowMore.click()

#while True:
    #element.send_keys(Keys.PAGE_DOWN)
    #driver.execute_script('window.scrollTo(0, document.role.scrollHeight);')