from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from time import sleep
import os

driver = webdriver.Chrome()
load_dotenv()

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3624622919&f_E=1%2C2%2C3&f_WT=2%2C3&keywords=Desenvolvedor%20Python&location=Trabalho%20remoto&refresh=true")

driver.find_element(By.CLASS_NAME, "nav__button-secondary").click()
driver.find_element(By.ID, "username").send_keys(os.getenv("EMAIL"))
driver.find_element(By.ID, "password").send_keys(os.getenv("PASSWORD"))
driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button').click()

sleep(30)

job_cards = driver.find_elements(By.CLASS_NAME, "job-card-container")
for job in job_cards:
    job.find_element(By.CLASS_NAME, "job-card-container__link").click()
    sleep(5)
    driver.find_element(By.CLASS_NAME, "jobs-save-button").click()