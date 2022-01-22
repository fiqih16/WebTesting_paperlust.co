from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://paperlust.co/")

driver.implicitly_wait(5)
driver.find_element_by_xpath('//*[@id="large-international-pl"]/div[2]').click()

driver.find_element_by_name("search").send_keys('wedding invitations',Keys.ENTER)
driver.implicitly_wait(5)

driver.find_element_by_xpath('//*[@id="search__container"]/div/div/div/div/div[1]/div/div[1]/div[4]/div[2]/div/div/ul/li[10]').click()


BtnShowMore = driver.find_element_by_xpath('//*[@id="search__container"]/div/div/div/div/div[2]/div[2]/div/div[13]/a')
ScrollUp = driver.find_element_by_xpath('//*[@id="search-index"]/div[1]/div[1]/div[2]')

while True:
        
        driver.execute_script("arguments[0].scrollIntoView()",BtnShowMore)
        driver.implicitly_wait(2)
        BtnShowMore.click()
        driver.execute_script("arguments[0].scrollIntoView()",ScrollUp)
