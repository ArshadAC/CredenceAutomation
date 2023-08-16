import time
import pytest
from selenium import webdriver
from Page_Object.LoginPage import loginPage
from utilities.Logger import LogGenerator
from utilities.readProperties import ReadConfig


class Test_Login:

    # URL = "https://automation.credence.in/"
    # Email_Address = "credtest1@gmail.com"
    # Password = "cred123"
    Url = ReadConfig.getUrl()
    Email = ReadConfig.getEmail()
    Password = ReadConfig.getPassword()
    log = LogGenerator.loggen()

    # def test_HomePageTitle_001(self,setup):
    #     self.driver = setup
    #     self.log.info("test_homePageTitle_001 is Started")
    #     self.log.info("Opening Browser")
    #     self.driver.get(self.Url)
    #     self.log.info("Opening URl")
    #     act_title = self.driver.title
    #     if act_title == "CredKart":
    #         assert True
    #
    #     else:
    #         assert False

    def test_Login_002(self,setup):
        self.driver = setup
        self.log.info("test_homePageTitle_001 is Started")
        self.log.info("Opening Browser")
        self.driver.get(self.Url)
        self.log.info("Opening URl")
        self.lp = loginPage(self.driver)
        self.lp.ClickLoginButton()
        self.log.info("Click on Loging Button")
        self.lp.EnterEmailaddress(self.Email)
        self.log.info("Entering EmailID--->" + self.Email)
        # self.lp.EnterEmailaddress("credtest@gmail.com")
        self.lp.EnterPassword(self.Password)
        self.log.info("Entering Password--->" + self.Password)
        # self.lp.EnterPassword("cred123")
        self.lp.ClickLogin()
        self.log.info("Click on Login Button")
        if self.lp.Login_Status() == True:
            self.driver.save_screenshot("E:\\Automation Project\\credence\\screenshot\\test_Login_002_Pass.png")
            self.lp.Click_credence_button()
            self.log.info("Click on Credence Button")
            self.lp.Click_Logout()
            self.log.info("Click on Logout Button")

            assert True
        else:
            self.driver.save_screenshot("E:\\Automation Project\\credence\\screenshot\\test_Login_002_fail.png")
            assert False

        self.driver.close()
        self.log.info("test_Login_002 is completed")

        # if self.driver.title == "CredKart":
        #     self.log.info("test_Login_002 Passed")
        #     assert True
        # else:
        #     self.log.info("test_Login_002 Failed")
        #     assert False

