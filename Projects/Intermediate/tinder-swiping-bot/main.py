from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from dotenv import load_dotenv
import os

EMAIL = os.getenv("EMAIL")
PASS = os.getenv("PASS")

driver = webdriver.Chrome()

driver.get("https://tinder.com/pt")

sleep(2)
entry_btn = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
entry_btn.click()

fb_login_btn = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
fb_login_btn.click()

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

email_field = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/form/div/div[1]/div/input')
pass_field = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/form/div/div[2]/div/input')
#driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]/input').click()

email_field.send_keys(EMAIL)
pass_field.send_keys(PASS)
pass_field.send_keys

sleep(8)

driver.switch_to.window(base_window)
""" sleep(10)
driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div/div[3]/button[1]').click()
sleep(2)
driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div/div[3]/button[2]').click() """

sleep(1000)