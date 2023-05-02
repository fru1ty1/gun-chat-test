from selenium import webdriver
from selenium import common
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from globals import EXPECTED_MSGS_100_REAL, EXPECTED_MSGS_100, END_MSG
import difflib
import time

driver = webdriver.Chrome("./chromedriver")
#driver = webdriver.Firefox()
driver.implicitly_wait(100000)

input("press to continue")


driver.get("https://cafe-et-baguette.noppakorn.com")
driver.find_element(By.XPATH, \
    '/html/body/div/div/div[2]/form/div/div[2]/div/div[1]/input').send_keys("receiver@test.com")
driver.find_element(By.XPATH, \
    '/html/body/div/div/div[2]/form/div/div[2]/div/div[2]/input').send_keys("123" + Keys.ENTER)
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div[2]/div[18]/button").click()
time.sleep(3)

msgs = []
index = 1
# wait for messages
while True:
    text = driver.find_element(By.XPATH, f"/html/body/div/div/div/div/div[2]/div[1]/div[1]/div[{index}]/div[2]/div[1]").text
    if index == 1:
        start_time = time.perf_counter()
    if text == str(END_MSG):
        total_time = time.perf_counter() - start_time
        break
    msgs.append(text)
    index += 1

print(msgs)
print(total_time)

print(f"nr of msgs = {len(msgs)}")

sm=difflib.SequenceMatcher(None,msgs,EXPECTED_MSGS_100_REAL)

print(sm.ratio())



driver.quit()
