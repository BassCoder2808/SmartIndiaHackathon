from logging import exception
from selenium import webdriver
import time
import glob
import os

driver = webdriver.Chrome(executable_path="C:/Users/vedant jolly/Desktop/chromedriver.exe")
driver.get("https://www.google.com/maps/")
time.sleep(5)

arrival_data_type = driver.find_element("name", "q")
arrival_data_type.send_keys("Rail Mitra, Charkop, Kandivali (W), Mumbai")
time.sleep(5)

btn_go = driver.find_element("id", "searchbox-searchbutton")
btn_go.click()
time.sleep(15)