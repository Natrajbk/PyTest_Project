import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import allure

from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
from Utils import utils

@pytest.mark.usefixtures("test_setup")
class TestLogin():
    def test_login(self):
        driver=self.driver
        #driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.get(utils.URL)
        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login()

        #driver.find_element(by=By.ID, value="txtUsername").send_keys("Admin")
        # driver.find_element(by=By.ID, value="txtPassword").send_keys("admin123")
        # driver.find_element(by=By.ID, value="btnLogin").click()

    def test_logout(self):
        driver=self.driver
        homepage=HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()
        # x=driver.title()
        # print("title is",x)
        # assert x=="OrangeHRM"

        # driver.find_element(by=By.ID, value="welcome").click()
        # driver.find_element(by=By.LINK_TEXT, value="Logout").click()

# if __name__=="__main__":
#     TestLogin()