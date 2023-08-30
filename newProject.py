# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 18:29:19 2023

@author: Tapir
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from time import sleep

options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1920x1080")
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
options.add_argument(f'user-agent={user_agent}')

driver = webdriver.Chrome(options)

driver.get("https://www.accuweather.com/de/de/aachen/52062/weather-forecast/170335")
btn_do_not_consent = driver.find_element(By.CLASS_NAME, "fc-cta-do-not-consent")
btn_do_not_consent.click()
sleep(3)

elem = driver.find_element(By.CLASS_NAME, "cur-con-weather-card")
#elem.screenshot("weather.png")

x = elem.text.split("\n")
print(f"{x[1]} {x[2]}\n{x[12]}")

driver.close()

