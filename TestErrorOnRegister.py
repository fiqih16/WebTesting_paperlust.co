from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.get("https://paperlust.co/")
driver.implicitly_wait(5)
driver.find_element_by_xpath('//*[@id="large-international-pl"]/div[2]').click()

driver.implicitly_wait(7)
join = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/nav/ul/li[17]')

Hover = ActionChains(driver).move_to_element(join)

Hover.click().perform()

#button signup
driver.find_element_by_xpath('//*[@id="register"]/div[10]/button').click()

#Isi field firstname
driver.find_element_by_name("signup-firstname").send_keys('firstname')
#button signup
driver.find_element_by_xpath('//*[@id="register"]/div[10]/button').click()

#Isi field lastname
driver.find_element_by_name("signup-lastname").send_keys('lastname')
#button signup
driver.find_element_by_xpath('//*[@id="register"]/div[10]/button').click()

#Isi field email
driver.find_element_by_name("signup-email").send_keys('ini email')
#button signup
driver.find_element_by_xpath('//*[@id="register"]/div[10]/button').click()

#Isi field mobile phone
driver.find_element_by_name("signup-mobile").send_keys('mobile phone')
#button signup
driver.find_element_by_xpath('//*[@id="register"]/div[10]/button').click()

#Isi field password
driver.find_element_by_name("signup-password").send_keys('1234')
#button signup
driver.find_element_by_xpath('//*[@id="register"]/div[10]/button').click()
