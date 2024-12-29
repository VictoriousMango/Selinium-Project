'''
Testiing Feature

'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium .webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import config
from Bot import bot
import time
import config

class Victorious(bot):
    def __init__(self):
        super().__init__()
    
    def SendingMail(self, Receiver, Subject, Content):
        self._OpenWebsite('https://mail.google.com/')
        # Log in
        email_input = driver.find_element(By.ID, 'identifierId')
        email_input.send_keys(EMAIL)
        email_input.send_keys(Keys.RETURN)
        time.sleep(2)  # Wait for the next page to load

        password_input = driver.find_element(By.NAME, 'password')
        password_input.send_keys(PASSWORD)
        password_input.send_keys(Keys.RETURN)
        time.sleep(5)  # Wait for the inbox to load

        # Click the Compose button
        compose_button = driver.find_element(By.XPATH, '//div[@role="button" and text()="Compose"]')
        compose_button.click()
        
        # You can add more code here to fill in the email details if needed


if __name__ == "__main__":
    # VicBot = Victorious()
    # method = [func for func in dir(VicBot) if callable(getattr(VicBot, func)) and not func.startswith("_")]
    # methods = dict()
    # for i in range(len(method)):
    #     methods[i] = method[i]
    # methods[len(method)] = "exit"
    # exit = False
    
    # while not exit:
    #     for i in methods:
    #         print(f'{i} : {methods[i]}')
    #     choice = int(input("Enter your choice: "))
    #     if methods[choice] == "exit":
    #         exit = True
    #     elif methods[choice] == "SendingMail":
    #         VicBot.SendingMail(
    #             Receiver="Yadashesh@gmail.com", 
    #             Subject="Testing",
    #             Content="This is a test mail"
    #             )
    driver = webdriver.Chrome()
    driver.get("https://mail.google.com/")
    time.sleep(3)
    email_input = driver.find_element(By.ID, 'identifierId')
    email_input.send_keys("yadashesh@gmail.com")
    email_input.send_keys(Keys.RETURN)
    time.sleep(2)  # Wait for the next page to load

    password_input = driver.find_element(By.NAME, 'password')
    password_input.send_keys("yada@0208")
    password_input.send_keys(Keys.RETURN)
    time.sleep(5)  # Wait for the inbox to load

    # Click the Compose button
    compose_button = driver.find_element(By.XPATH, '//div[@role="button" and text()="Compose"]')
    compose_button.click()
    print("Program Executed SUccessfully!!!")