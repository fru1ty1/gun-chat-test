from selenium import webdriver
from globals import END_MSG, EXPECTED_MSGS_100, BRIEFING_URL
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

#driver = webdriver.Chrome("./chromedriver")
driver = webdriver.Firefox()
driver.implicitly_wait(10)

input("press to continue")

driver.get(BRIEFING_URL)
driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/button[3]').click()
driver.find_element(By.XPATH, \
    '/html/body/div/div/div[2]/div/section/div/div/input').send_keys("sender")
driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/section/div/div/button").click()
time.sleep(2)

for text in EXPECTED_MSGS_100:
    driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/section/div/input').send_keys(text + Keys.ENTER)
    time.sleep(0.1)

time.sleep(1)
driver.quit()
