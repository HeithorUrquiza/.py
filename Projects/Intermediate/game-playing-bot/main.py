from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from pprint import pprint

chrome_driver_path = "C:/Users/heith/Documents/Development/chromedriver.exe"
service = ChromeService(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://www.python.org/")

dates_list = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
events_list = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
events_dict = {}

for i in range(len(dates_list)):
    events_dict.update(
        {
            i:{
                "time": dates_list[i].text,
                "name": events_list[i].text
            }
        }
    )
    
print(events_dict)