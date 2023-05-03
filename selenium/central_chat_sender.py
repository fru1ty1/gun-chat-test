from selenium import webdriver
from globals import END_MSG, EXPECTED_MSGS_100
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time

#driver = webdriver.Chrome("./chromedriver")
driver = webdriver.Firefox()
driver.implicitly_wait(10)

input("press to continue")

driver.get("https://cafe-et-baguette.noppakorn.com")
driver.find_element(By.XPATH, '/html/body/div/div/div[2]/form/div/div[2]/div/div[1]/input').send_keys("sender@test.com")
driver.find_element(By.XPATH,'/html/body/div/div/div[2]/form/div/div[2]/div/div[2]/input').send_keys("123" + Keys.ENTER)

#for _ in range(20):
#    actions.send_keys(Keys.SPACE).perform()

time.sleep(4)
driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div/div[2]/div[78]/button').click()
 
time.sleep(2)
for text in EXPECTED_MSGS_100:
    driver.find_element(By.XPATH, '/html/body/div/div/div/div/div[2]/div[1]/div[2]/form/input').send_keys(text + Keys.ENTER)
    time.sleep(0.1)


time.sleep(1)
driver.quit()
