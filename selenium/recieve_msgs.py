from selenium import webdriver
from selenium import common
from selenium.webdriver.common.by import By
from globals import EXPECTED_MSGS_100_REAL, EXPECTED_MSGS_100, END_MSG
import difflib
import time

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(100000)

driver.get("http://localhost:5000/")
driver.find_element(By.XPATH, '/html/body/div/div/main/input[1]').send_keys("DopeAssRhymer")
driver.find_element(By.XPATH, '/html/body/div/div/main/input[2]').send_keys("password123")
driver.find_element(By.XPATH, '/html/body/div/div/main/button[2]').click()
time.sleep(1)


msgs = []
index = 1
# wait for messages
while True:
    try:
        text = driver.find_element(By.XPATH, f"/html/body/div/div/main/div[{index}]/div/p").text
        if index == 1:
            start_time = time.perf_counter()
        if text == str(END_MSG):
            total_time = time.perf_counter() - start_time
            break
        msgs.append(text)

    except common.NoSuchElementException as e:
        pass
    index += 1

print(msgs)
print(total_time)

print(f"nr of msgs = {len(msgs)}")

sm=difflib.SequenceMatcher(None,msgs,EXPECTED_MSGS_100_REAL)

print(sm.ratio())



time.sleep(2)
driver.quit()
