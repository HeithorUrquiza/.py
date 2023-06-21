from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep

class InstaFollower:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome()  
        
        
    def login(self, email, password):
        """Login on Instagram account"""
        self.driver.get("https://www.instagram.com/accounts/login/")
        
        sleep(2)
        email_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        pass_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        
        email_input.send_keys(email)
        pass_input.send_keys(password)
        pass_input.send_keys(Keys.ENTER)
        sleep(5)
        
        
    def find_followers(self, account):
        """Find the followers of target account"""
        self.driver.get(f"https://www.instagram.com/{account}")
        
        sleep(3)
        followers = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        
        sleep(2)
        popup_wd = self.driver.window_handles[-1]
        self.driver.switch_to.window(popup_wd)
        
        followers_popup = self.driver.find_element(By.CSS_SELECTOR, "._aano")
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_popup)
            sleep(1)
        
        
    def follow(self):
        """Follow the users"""
        
        follows = self.driver.find_elements(By.CSS_SELECTOR, "._aj1-")
        for follow in follows:
            sleep(1)
            try:
                follow.click()
                sleep(1)
            except ElementClickInterceptedException:
                try:
                    cancel_btn = self.driver.find_element(By.CSS_SELECTOR, "._a9_1")
                    print(cancel_btn.text)
                    cancel_btn.click()
                except:
                    print("Without btn")
                    pass
                
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.quit()