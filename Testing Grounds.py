'''
Testiing Feature

'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium .webdriver.common.keys import Keys
import time
import config

class bot():
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def OpenWebsite(self, url):
        self.driver.get(url)
        time.sleep(3)
    
    def InputElement_ID(self, Id, Input):
        self.driver.find_element(By.ID, Id).send_keys(Input + Keys.ENTER)
        time.sleep(3)

    def ClickBy_ID(self, Id):
        self.driver.find_element(By.ID, Id).click()
        time.sleep(3)
    
    def ClickBy_Name(self, name):
        self.driver.find_element(By.NAME, name).click()
        time.sleep(3)
    
    def SelectBy_Value(self, htmlTag=None, name=None, value=None):
        if htmlTag and name and value:
            path = f"//{htmlTag}[@name='{name}' and @value='{value}']"
        elif htmlTag and value:
            path = f"//{htmlTag}[@value='{value}']"
        self.driver.find_element(By.XPATH, path).click()
        time.sleep(3)
    
    def breakfast(self):
        # Locate the BREAKFAST radio button using its value or text
        breakfast_radio_button = self.driver.find_element(By.XPATH, '//input[@name="Servicetype_id" and @value="59"]')

        # Click on the radio button
        breakfast_radio_button.click()
    

if __name__ == "__main__":
    url = "https://events.iist.ac.in/foodbook/index.php?option=login"
    SBot = bot()
    SBot.OpenWebsite(url)
    SBot.InputElement_ID("Institute_ID", config.IIST_FoodBookingUsername)
    SBot.InputElement_ID("pin", config.IIST_FoodBookingPassword)

    ## Booking Breakfast
    SBot.ClickBy_ID("Canteen_id")
    SBot.SelectBy_Value(htmlTag="option", value="1")
    SBot.SelectBy_Value(htmlTag="input", name="Servicetype_id", value="59")
    SBot.ClickBy_ID("356")  # Breakfast Select All
    SBot.SelectBy_Value(htmlTag="input", name="Submit", value="Save Booking") # Saving Booking
    SBot.OpenWebsite("https://events.iist.ac.in/foodbook/index.php?option=booking&task=book")

    ## Booking Lunch
    SBot.ClickBy_ID("Canteen_id")
    SBot.SelectBy_Value(htmlTag="option", value="1")
    SBot.SelectBy_Value(htmlTag="input", name="Servicetype_id", value="60")
    SBot.ClickBy_ID("361")  # Lunch Select All
    SBot.SelectBy_Value(htmlTag="input", name="Submit", value="Save Booking") # Saving Booking
    SBot.OpenWebsite("https://events.iist.ac.in/foodbook/index.php?option=booking&task=book")

    ##Booking Dinner
    SBot.ClickBy_ID("Canteen_id")
    SBot.SelectBy_Value(htmlTag="option", value="1")
    SBot.SelectBy_Value(htmlTag="input", name="Servicetype_id", value="61")
    SBot.ClickBy_ID("365")  # Dinner Select All
    SBot.SelectBy_Value(htmlTag="input", name="Submit", value="Save Booking") # Saving Booking
    SBot.OpenWebsite("https://events.iist.ac.in/foodbook/index.php?option=booking&task=book")

    ## Booking Snacks
    SBot.ClickBy_ID("Canteen_id")
    SBot.SelectBy_Value(htmlTag="option", value="1")
    SBot.SelectBy_Value(htmlTag="input", name="Servicetype_id", value="62")
    SBot.ClickBy_ID("372")  # Snacks Select All 
    SBot.ClickBy_ID("428")  # Coffee Select All 
    SBot.SelectBy_Value(htmlTag="input", name="Submit", value="Save Booking") # Saving Booking
    SBot.OpenWebsite("https://events.iist.ac.in/foodbook/index.php?option=booking&task=book")

    print("Program Executed SUccessfully!!!")