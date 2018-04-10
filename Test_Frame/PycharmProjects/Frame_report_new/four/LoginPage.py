from four.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class LoginPage(BasePage):

    """description of class"""
    # page element identifier
    usename = (By.ID, 'username')
    password = (By.ID, 'password')
    #dialogTitle = (By.XPATH, "//h3[@class=\"modal-title ng-binding\"]")
    #cancelButton = (By.XPATH, '//button[@class=\"btn btn-warning ng-binding\"][@ng-click=\"cancel()\"]')
    okButton = (By.XPATH, '//*[@id="submit"]')

    # Get username textbox and input username
    def set_username(self, username):
        name = self.driver.find_element(*LoginPage.usename)
        name.send_keys(username)

        # Get password textbox and input password, then hit return

    def set_password(self, password):
        pwd = self.driver.find_element(*LoginPage.password)
        pwd.send_keys(password + Keys.RETURN)

        # Get pop up dialog title

    # def get_DiaglogTitle(self):
    #     digTitle = self.driver.find_element(*LoginPage.dialogTitle)
    #     return digTitle.text

        # Get "cancel" button and then click

    # def click_cancel(self):
    #     cancelbtn = self.driver.find_element(*LoginPage.cancelButton)
    #     cancelbtn.click()

        # click Sign in

    def click_SignIn(self):
        okbtn = self.driver.find_element(*LoginPage.okButton)
        okbtn.click()