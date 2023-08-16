import time

import self
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException as Ec

# driver = webdriver.Chrome()
# driver.get("https://automation.credence.in/")
# time.sleep(2)
#
# driver.find_element(By.XPATH,"//a[normalize-space()='Login']").click()
# driver.find_element(By.ID,'email').send_keys("credtest1@gmail.com")
# driver.find_element(By.ID,'password').send_keys('cred123')
# driver.find_element(By.XPATH,"//button[@type='submit']").click()
# time.sleep(2)
class loginPage:
    button_Login_XPATH = (By.XPATH,"//a[normalize-space()='Login']")
    text_email_address_id = (By.ID,"email")
    text_password_id = (By.ID, "password")
    button_login_XPATH = (By.XPATH,"//button[@type='submit']")
    blogpost_XPATH = (By.XPATH,"//a[@class='btn btn-primary btn-lg']")
    button_credence_XPATH = (By.XPATH,"//a[@role='button']")
    button_Logout_XPATH = (By.XPATH,"//a[normalize-space()='Logout']")

    def __init__(self, driver):
        self.driver = driver

    def ClickLoginButton(self):
        self.driver.find_element(*loginPage.button_Login_XPATH).click()

    def EnterEmailaddress(self, emailaddress):
        self.driver.find_element(*loginPage.text_email_address_id).send_keys(emailaddress)

    def EnterPassword(self,password):
        self.driver.find_element(*loginPage.text_password_id).send_keys(password)

    def ClickLogin(self):
        self.driver.find_element(*loginPage.button_login_XPATH).click()

    def Login_Status(self):
        try:
            self.driver.find_element(*loginPage.blogpost_XPATH)
            return True

        except Ec:
            return False


    def Click_credence_button(self):
        self.driver.find_element(*loginPage.button_credence_XPATH).click()
    def Click_Logout(self):
        self.driver.find_element(*loginPage.button_Logout_XPATH).click()