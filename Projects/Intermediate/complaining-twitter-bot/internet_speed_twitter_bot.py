from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

class InternetSpeedTwitterBot:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome()
        self.down = None
        self.up = None
        
    
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        
        sleep(2)
        print("clicked")
        self.driver.find_element(By.CSS_SELECTOR, ".start-text").click()
        
        sleep(45)
        self.down = self.driver.find_element(By.CSS_SELECTOR, ".download-speed").text
        self.up = self.driver.find_element(By.CSS_SELECTOR, ".upload-speed").text
        
        print(f"down: {self.down}")
        print(f"up: {self.up}")
        sleep(3)
    
    
    def tweet_at_provider(self, email, password, user):
        self.driver.get("https://twitter.com/i/flow/login")
        
        sleep(2)
        email_input = self.driver.find_element(By.NAME, "text")
        email_input.send_keys("heithorur@gmail.com")
        email_input.send_keys(Keys.ENTER)
        
        sleep(2)
        user_input = self.driver.find_element(By.NAME, "text")
        user_input.send_keys("Hecth_ur")
        user_input.send_keys(Keys.ENTER)
        
        sleep(2)
        pass_input = self.driver.find_element(By.NAME, "password")
        pass_input.send_keys("Hh08112123@")
        pass_input.send_keys(Keys.ENTER)
        
        sleep(2)
        msg = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for 200down/150up?"
        tweet_input = self.driver.find_element(By.CSS_SELECTOR, ".public-DraftEditor-content")
        tweet_input.send_keys(msg)
        
        sleep(1)
        tweet_btn = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/span/span')
        tweet_btn.click()
        
        sleep(10)

    
    
bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider("a", "a", "a")