from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import requests
from time import sleep

load_dotenv()
URL = "https://www.zillow.com/new-york-ny/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-74.51938436914062%2C%22east%22%3A-73.43997763085937%2C%22south%22%3A40.39575054094651%2C%22north%22%3A40.99858878236764%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A6181%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A597762%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%7D"
HEADER = {
    "User-Agent": os.getenv("USER_AGENT"),
    "Accept-Language": "pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"
}


class RentingResearch:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome()
        resp = requests.get(URL, headers=HEADER)
        resp.raise_for_status()
        web_page = resp.text
        self.soup = BeautifulSoup(web_page, "html.parser")
        
        
    def colect_info_cards(self):
        all_cards = self.soup.select_one("#grid-search-results > ul")
        all_link_elements = all_cards.find_all(attrs={"data-test": "property-card-link"})
        all_links = []
        
        for item in all_link_elements:
            link = item["href"]
            if "https" not in link:
                link = f"https://www.zillow.com{link}"
            all_links.append(link)
            
        all_address = [item.getText() for item in all_cards.find_all(attrs={"data-test": "property-card-addr"})]
        all_prices = [item.getText().split("+")[0] for item in all_cards.find_all(attrs={"data-test": "property-card-price"}) if "$" in item.text]
        
        return all_links, all_address, all_prices
        
        
    def fill_formularie(self, url_forms):
        links, address, prices = self.colect_info_cards()
        
        for i in range(len(address)):
            self.driver.get(url_forms)
            
            sleep(2)
            address_input = self.driver.find_element(By.XPATH, 
                                                     '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            prices_input = self.driver.find_element(By.XPATH, 
                                                    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link_input = self.driver.find_element(By.XPATH, 
                                                  '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            
            address_input.send_keys(address[i])
            prices_input.send_keys(prices[i])
            link_input.send_keys(links[i])
            
            self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()
            
            sleep(3)
        self.driver.quit()