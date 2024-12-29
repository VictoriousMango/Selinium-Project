from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium .webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import config

class bot():
    def __init__(self):
        # options = Options()
        # options.binary_location = config.Brave
        self.driver = webdriver.Chrome()#(options=options)
    
    def _OpenWebsite(self, url):
        self.driver.get(url)
        time.sleep(3)
    
    def _InputElement_ID(self, Id, Input):
        self.driver.find_element(By.ID, Id).send_keys(Input + Keys.ENTER)
        time.sleep(3)

    def _ClickBy_ID(self, Id):
        self.driver.find_element(By.ID, Id).click()
        time.sleep(3)
    
    def _ClickBy_Name(self, name):
        self.driver.find_element(By.NAME, name).click()
        time.sleep(3)
    
    def _SelectBy_Value(self, htmlTag=None, name=None, value=None):
        if htmlTag and name and value:
            path = f"//{htmlTag}[@name='{name}' and @value='{value}']"
        elif htmlTag and value:
            path = f"//{htmlTag}[@value='{value}']"
        self.driver.find_element(By.XPATH, path).click()
        time.sleep(3)
    
