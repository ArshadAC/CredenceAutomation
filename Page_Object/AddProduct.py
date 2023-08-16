import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException as Ec


class AddProduct:
    Click_AppleMackbook_XPATH = (By.XPATH,"//h3[normalize-space()='Apple Macbook Pro']")
    Click_Addtocart_XPATH = (By.XPATH,"//input[@value='Add to Cart']")
    Dropdown_Qty_XPATH = (By.XPATH,"//select[@class='quantity']")
    Click_Continue_XPATH = (By.XPATH,"//a[@class='btn btn-primary btn-lg']")
    Click_Headphone_XPATH = (By.XPATH,"//h3[normalize-space()='Headphones']")
    Click_AddHeadphone_XPATH = (By.XPATH,"//input[@value='Add to Cart']")
    Dropdown_Qty1_XPATH = (By.XPATH,"//select[@class='quantity']")
    Click_checkout_XPATH = (By.XPATH,"//a[@class='btn btn-success btn-lg']")
    Text_Firstname_XPATH = (By.XPATH,"//input[@id='first_name']")
    Text_Lastname_XPATH = (By.XPATH,"//input[@id='last_name']")
    Text_PhoneNumber_XPATH = (By.XPATH,"//input[@id='phone']")
    Text_Address_XPATH = (By.XPATH,"//textarea[@id='address']")
    Text_Zip_Code_XPATH = (By.XPATH,"//input[@id='zip']")
    Dropdown_State_XPATH = (By.XPATH,"//select[@id='state']")
    Text_Owner_XPATH = (By.XPATH,"//input[@id='owner']")
    Text_CVV_XPATH = (By.XPATH,"//input[@id='cvv']")
    Text_Card_Number_XPATH = (By.XPATH,"//input[@id='cardNumber']")
    Dropdown_Exp_Year_XPATH = (By.XPATH,"//select[@id='exp_year']")
    Dropdown_Exp_Month_XPATH = (By.XPATH,"//select[@id='exp_month']")
    Click_Continue_Chekout_XPATH = (By.XPATH,"//button[@id='confirm-purchase']")
    Order_Status_XPATH = (By.XPATH,"//p[@class='lead w-lg-50 mx-auto']")

    def __init__(self, driver):
        self.driver = driver

    def Click_AppleMackbook(self):
        self.driver.find_element(*AddProduct.Click_AppleMackbook_XPATH).click()

    def Click_Addtocart(self):
        self.driver.find_element(*AddProduct.Click_Addtocart_XPATH).click()

    def Dropdown_Qty(self,qty):
        Qty = Select(self.driver.find_element(*AddProduct.Dropdown_Qty_XPATH))
        Qty.select_by_index(qty)

    def Click_Continue(self):
        self.driver.find_element(*AddProduct.Click_Continue_XPATH).click()

    def Click_Headphone(self):
        self.driver.find_element(*AddProduct.Click_Headphone_XPATH).click()

    def Click_Addheadphone(self):
        self.driver.find_element(*AddProduct.Click_AddHeadphone_XPATH).click()

    def Dropdown_Qty1(self,qty1):
        Qty1 = Select(self.driver.find_element(*AddProduct.Dropdown_Qty1_XPATH))
        Qty1.select_by_index(qty1)

    def Click_Checkout(self):
        self.driver.find_element(*AddProduct.Click_checkout_XPATH).click()

    def Enter_Firstname(self,firstname):
        self.driver.find_element(*AddProduct.Text_Firstname_XPATH).send_keys(firstname)

    def Enter_Lastname(self,lastname):
        self.driver.find_element(*AddProduct.Text_Lastname_XPATH).send_keys(lastname)

    def Enter_PhoneNo(self,phoneno):
        self.driver.find_element(*AddProduct.Text_PhoneNumber_XPATH).send_keys(phoneno)

    def Enter_Address(self,address):
        self.driver.find_element(*AddProduct.Text_Address_XPATH).send_keys(address)

    def Enter_Zipcode(self,zipcode):
        self.driver.find_element(*AddProduct.Text_Zip_Code_XPATH).send_keys(zipcode)

    def Dropdown_State(self,state):
        State = Select(self.driver.find_element(*AddProduct.Dropdown_State_XPATH))
        State.select_by_index(state)

    def Enter_Owner(self,owner):
        self.driver.find_element(*AddProduct.Text_Owner_XPATH).send_keys(owner)

    def Enter_CVV(self,cvv):
        self.driver.find_element(*AddProduct.Text_CVV_XPATH).send_keys(cvv)

    def Enter_CardNo(self,cardno):
        self.driver.implicitly_wait(5)
        self.driver.find_element(*AddProduct.Text_Card_Number_XPATH).send_keys(cardno)
        self.driver.find_element(*AddProduct.Text_Card_Number_XPATH).send_keys(cardno)
        self.driver.find_element(*AddProduct.Text_Card_Number_XPATH).send_keys(cardno)
        self.driver.find_element(*AddProduct.Text_Card_Number_XPATH).send_keys(cardno)

    def Dropdown_Year(self,year):
        Year = Select(self.driver.find_element(*AddProduct.Dropdown_Exp_Year_XPATH))
        Year.select_by_index(year)

    def Dropdown_Month(self,month):
        Month = Select(self.driver.find_element(*AddProduct.Dropdown_Exp_Month_XPATH))
        Month.select_by_index(month)

    def Click_FinalCheckout(self):
        self.driver.find_element(*AddProduct.Click_Continue_Chekout_XPATH).click()

    def Order_Status(self):
        self.driver.implicitly_wait(10)
        try:
            self.driver.find_element(*AddProduct.Order_Status_XPATH)
            return True
        except Ec:
            return False
