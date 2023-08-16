import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from Page_Object.LoginPage import loginPage
from Page_Object.AddProduct import AddProduct
from utilities.readProperties import ReadConfig
from utilities.Logger import LogGenerator

class Test_Login:

    Url = ReadConfig.getUrl()
    Email = ReadConfig.getEmail()
    Password = ReadConfig.getPassword()
    Firstname = ReadConfig.getFirstname()
    Lastname = ReadConfig.getLastname()
    log = LogGenerator.loggen()

    def test_addProduct_003(self,setup):
        self.driver = setup
        self.log.info("test_addProduct_003 is Sarted")
        self.log.info("Opening Browser")
        self.driver.get(self.Url)
        self.log.info("Opening Url--->" + self.Url)
        self.driver.maximize_window()
        self.lp = loginPage(self.driver)
        self.lp.ClickLoginButton()
        self.log.info("Click on Login Button")
        self.lp.EnterEmailaddress(self.Email)
        self.log.info("Enter Email Address--->" + self.Email)
        # self.lp.EnterEmailaddress("credtest@gmail.com")
        self.lp.EnterPassword(self.Password)
        self.log.info("Enter Password--->" + self.Password)
        # self.lp.EnterPassword("cred123")
        self.lp.ClickLogin()
        self.ap = AddProduct(self.driver)
        time.sleep(5)
        self.ap.Click_AppleMackbook()
        self.log.info("Click on ApppleMackbook")
        self.ap.Click_Addtocart()
        self.ap.Dropdown_Qty(1)
        self.log.info("Select Qty")
        time.sleep(5)
        self.ap.Click_Continue()
        self.log.info("Click on Continue")
        time.sleep(5)
        self.ap.Click_Headphone()
        self.log.info("Click on headPhone")
        self.ap.Click_Addheadphone()
        self.log.info("Click on Add Headphone")
        self.ap.Dropdown_Qty1(2)
        self.log.info("Select Qty ")
        time.sleep(10)
        self.ap.Click_Checkout()
        self.log.info("Click on checkout")
        self.ap.Enter_Firstname(self.Firstname)
        self.log.info("Enter Firstname--->" + self.Firstname)
        # self.ap.Enter_Firstname("Credence")
        self.ap.Enter_Lastname(self.Lastname)
        self.log.info("Enter Lastname--->" + self.Lastname)
        # self.ap.Enter_Lastname("IT")
        self.ap.Enter_PhoneNo("9890945263")
        self.log.info("Enter Mobile Number")
        self.ap.Enter_Address("Katraj Pune")
        self.log.info("Enter Address")
        self.ap.Enter_Zipcode("411046")
        self.log.info("Enter Zipcode")
        self.ap.Dropdown_State(1)
        self.ap.Enter_Owner("Tushar")
        self.log.info("Enter Owner")
        self.ap.Enter_CVV("257")
        self.log.info("Enter CVV")
        self.ap.Enter_CardNo("4716")
        self.log.info("Enter Card number")
        self.ap.Enter_CardNo("1089")
        self.log.info("Enter card number")
        self.ap.Enter_CardNo("9971")
        self.log.info("Enter card number")
        self.ap.Enter_CardNo("6531")
        self.log.info("Enter card number")
        self.ap.Dropdown_Year(3)
        self.log.info("Select Year")
        self.ap.Dropdown_Month(2)
        self.log.info("Select Month")
        self.ap.Click_FinalCheckout()
        self.log.info("Click on Final Checkout")
        time.sleep(5)
        if self.driver.title == "CredKart":
            self.log.info("test_addProduct_003 Passed")
            assert True
        else:
            self.log.info("test_addProduct_003 Failed")
            assert False



