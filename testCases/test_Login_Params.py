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
    # Email = ReadConfig.getEmail()
    # Password = ReadConfig.getPassword()
    log = LogGenerator.loggen()

    def test_Login_Params_003(self,setup,getDataforlogin):
        self.driver = setup
        self.log.info("test_homePageTitle_001 is Started")
        self.log.info("Opening Browser")
        self.driver.get(self.Url)
        self.log.info("Opening URl")
        self.lp = loginPage(self.driver)
        self.lp.ClickLoginButton()
        self.log.info("Click on Loging Button")
        self.lp.EnterEmailaddress(getDataforlogin[0])
        # self.lp.EnterEmailaddress(self.Email)
        self.log.info("Entering EmailID--->" + getDataforlogin[0])
        # self.lp.EnterEmailaddress("credtest@gmail.com")
        self.lp.EnterPassword(getDataforlogin[1])
        # self.lp.EnterPassword(self.Password)
        self.log.info("Entering Password" + getDataforlogin[1])
        # self.lp.EnterPassword("cred123")
        self.lp.ClickLogin()
        self.log.info("Click on Login Button")

        StatusList = []
        if self.lp.Login_Status() == True:
            if getDataforlogin[2] == "Pass":
                self.driver.save_screenshot("E:\\Automation Project\\credence\\screenshot\\test_Login_002_Pass.png")
                self.lp.Click_credence_button()
                self.log.info("Click on Credence Button")
                self.lp.Click_Logout()
                self.log.info("Click on Logout Button")
                self.log.info("test_Login_Params_003 is passed")
                StatusList.append("Pass")

            elif getDataforlogin[2] == "Fail":
                self.driver.save_screenshot("E:\\Automation Project\\credence\\screenshot\\test_Login_002_Fail.png")
                self.lp.Click_credence_button()
                self.log.info("Click on Credence Button")
                self.lp.Click_Logout()
                self.log.info("Click on Logout Button")
                self.log.info("test_Login_Params_003 is failed")
                StatusList.append("Fail")

        else:
           if getDataforlogin[2] == "Pass":
               self.driver.save_screenshot("E:\\Automation Project\\credence\\screenshot\\test_Login_002_fail.png")
               self.log.info("test_Login_Params_003 Failed")
               StatusList.append("Fail")

           elif getDataforlogin[2] == "Fail":
               self.driver.save_screenshot("E:\\Automation Project\\credence\\screenshot\\test_Login_002_fail.png")
               self.log.info("test_Login_Params_003 Failed")
               StatusList.append("Pass")

        print(StatusList)
        if "Fail" not in StatusList:
            self.log.info("Test_Passed")

        else:
            self.log.info("Test Failed")

        self.driver.close()
        self.log.info("test_Login_Params is completed")

