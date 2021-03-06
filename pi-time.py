import os
from dotenv import load_dotenv

import time
import schedule

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=chrome_options)

load_dotenv()

username = os.getenv("USERNAME") 
password = os.getenv("PASSWORD")
channel = os.getenv("CHANNEL")

def pi_time():
    driver.get("https://discord.com/login")
    time.sleep(5)
    
    driver.find_element_by_name('email').send_keys(username)
    
    driver.find_element_by_name('password').send_keys(password)

    driver.find_element_by_xpath('//button[@type="submit"]').click()

    print(">>Login complete!")
    time.sleep(10)

    driver.get(channel)
    print(">>Opening the server link...")
    time.sleep(5)

    msg_input = driver.find_element_by_xpath('//div[@role="textbox"]')
    msg_input.click()
    msg_input.send_keys("it's pi-time!")
    msg_input.send_keys(Keys.ENTER)
    print(">>It's done!")

schedule.every().day.at("03:14:00").do(pi_time)

while True:
    schedule.run_pending()
    time.sleep(1)
