import time

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Utilities.configreader import ConfigReader
from features.pageobject.Base import BaseSettingsPage


class Addtocart(BaseSettingsPage):
    def __init__(self, driver):
        super().__init__(driver)

    def OpenPage(self, url):
        self.driver.get(url)
        self.DynamicImplicitWait(40)

    def clickclose(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("close_XPATH")

    def Click_loginhomepage(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("LOGINBUTTON_XPATH")

    def Enter_Username(self, username1):
        self.DynamicImplicitWait(40)
        self.TypeEditBox("USERNAME_XPATH", username1)

    def Enter_password(self, password1):
        self.DynamicImplicitWait(40)
        self.TypeEditBox("PASSWORD_XPATH", password1)

    def Click_login(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("loginbutton1_XPATH")

    def text_Searchbar(self, search1):
        WebDriverWait(self.driver, 40, ignored_exceptions=[StaleElementReferenceException]).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input")))
        self.DynamicImplicitWait(40)
        self.TypeEditBox("SEARCHBAR_XPATH", search1)

    def Click_SEARCHBUTTON(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("SEARCHBUTTON_XPATH")

    def Click_PRODUCT(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("PRODUCT_XPATH")
        self.windowsIDs=self.driver.window_handles
        self.parentwindowid=self.windowsIDs[0]
        childwindowid = self.windowsIDs[1]
        self.driver.switch_to.window(childwindowid)
        try:
            self.ClickButton("ADDTOCART_XPATH")
            time.sleep(5)
        except NoSuchElementException:
            pass

    def Click_ADDTOCART(self):
            self.DynamicImplicitWait(40)
            self.driver.switch_to.window(self.parentwindowid)
            time.sleep(5)
            self.ClickButton("CLICKPRODUCT_XPATH")
            self.windowsIDs = self.driver.window_handles
            self.parentwindowid = self.windowsIDs[0]
            self.subchildwindowid = self.windowsIDs[2]
            self.driver.switch_to.window(self.subchildwindowid)
            try:
                self.ClickButton("CARTADD_XPATH")
                time.sleep(5)
            except NoSuchElementException:
                pass

    def Click_PLUSBUTTON(self):
        try:
            self.DynamicImplicitWait(40)
            self.ClickButton("PLUSBUTTON_XPATH")
            time.sleep(5)
        except NoSuchElementException:
            pass


    def Click_MINUSBUTTON(self):
        try:
            self.DynamicImplicitWait(40)
            self.ClickButton("MINUSBUTTON_XPATH")
            time.sleep(5)
        except NoSuchElementException:
            pass

    def Click_SAVEFORLATER(self):
        try:
            self.DynamicImplicitWait(40)
            self.ClickButton("SAVEFORLATER_XPATH")
            time.sleep(5)
        except NoSuchElementException:
            pass

    def Click_REMOVE(self):
        try:
            self.DynamicImplicitWait(40)
            self.ClickButton("REMOVE_XPATH")
            time.sleep(5)
            self.ClickButton("END_XPATH")
            time.sleep(5)
        except NoSuchElementException:
            pass

    def Click_END(self):
        try:
            self.DynamicImplicitWait(40)
            self.ClickButton("CARTREMOVE_XPATH")
            time.sleep(5)
            self.ClickButton("ENDCART_XPATH")
            time.sleep(5)
        except NoSuchElementException:
            pass