from selenium import webdriver
from globals import END_MSG, EXPECTED_MSGS_100
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#driver = webdriver.Chrome("./chromedriver")
driver = webdriver.Firefox()
input("givew")

driver.get("http://localhost:5000/")
driver.find_element(By.XPATH, \
    '/html/body/div/div/main/input[1]').send_keys("DjSpinThatShit")
driver.find_element(By.XPATH, \
    '/html/body/div/div/main/input[2]').send_keys("password123")
driver.find_element(By.XPATH, \
    '/html/body/div/div/main/button[2]').click()
time.sleep(5)


for text in EXPECTED_MSGS_100:
    driver.find_element(By.XPATH, '/html/body/div/div/form/input').send_keys(text)
    driver.find_element(By.XPATH, '/html/body/div/div/form/button').click()
    
    time.sleep(0.1)


time.sleep(1)
driver.quit()
