import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

running = True
DRIVER_PATH = "C:/Users/aalhassan/Downloads/chromedriver_win32/chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(DRIVER_PATH, options=options)

while (running):  
    # Open the file in read mode
    with open("./Scripts/Python/countries.txt", "r") as file:
        lines=file.read().splitlines()
        #allText = file.read()
        #words = list(map(str, allText.split()))

    driver.get("https://bing.com")

    time.sleep(0.5)

    query = driver.find_element(By.XPATH, '//*[@id="sb_form_q"]')
    query.send_keys(random.choice(lines))

    time.sleep(0.5)
    query.send_keys(Keys.ENTER)
    time.sleep(1)

