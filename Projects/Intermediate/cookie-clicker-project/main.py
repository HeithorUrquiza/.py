from selenium import webdriver
from selenium.webdriver.common.by import By
from time import time

#chrome_driver_path = "C:/Users/heith/Documents/Development/chromedriver.exe"
#service = ChromeService(executable_path=chrome_driver_path)
driver = webdriver.Chrome()

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")
store = driver.find_elements(By.CSS_SELECTOR, "#store div")
_ids = [item.get_attribute("id") for item in store]
timeout = time() + 5
five_min = time() + 60*5

while True:
    cookie.click()
    if time() > timeout:
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        items_price = []
        
        #Create a list with all current prices
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                items_price.append(int(price.text.split("-")[1].strip().replace(",","")))
                
        #Create a dictionary with the prices and their respectivies ids
        cookie_upgrade = {}
        for i in range(len(items_price)):
            cookie_upgrade[items_price[i]] = _ids[i]
            
        #Find the current money or cookies
        money_element = driver.find_element(By.ID, "money").text
        money = int(money_element.replace(",",""))
        
        #Check the upgrades affordables and store they in a dictionary
        affordable_upgrades = {}
        for price, _id in cookie_upgrade.items():
            if money >= price:
                affordable_upgrades[price] = _id
                
        #Buy the max upgrade affordable
        max_price = max(affordable_upgrades)
        id_upgrade = affordable_upgrades[max_price]
        driver.find_element(By.ID, id_upgrade).click()
        
        timeout = time() + 5
        
        #Colect de rate of cookies
        if time() > five_min:
            states = driver.find_element(By.ID, "cps").text
            print(states)
            break