from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage():
    def __init__(self,driver):
        self.driver=driver

        self.username_textbox_id = "txtUsername"
        self.password_textbox_id = "txtPassword"
        self.login_button_id = "btnLogin"

    def enter_username(self,username):
        self.driver.find_element(by=By.ID, value=self.username_textbox_id).clear()
        self.driver.find_element(by=By.ID, value=self.username_textbox_id).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(by=By.ID, value=self.password_textbox_id).clear()
        self.driver.find_element(by=By.ID, value=self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(by=By.ID, value=self.login_button_id).click()

