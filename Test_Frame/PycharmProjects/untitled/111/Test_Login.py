__author__ = 'xua'

from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.alert import Alert
import unittest
import time
from LoginPage import LoginPage
from TestCaseInfo import TestCaseInfo
from TestReport import TestReport


class Test_Login(unittest.TestCase):
    # Setup
    def setUp(self):
        # self.driver = webdriver.Firefox()

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://172.16.34.150:81/#/login"
        # test case information
        self.testcaseinfo = TestCaseInfo(id="3", name="Login to floor manager lite using sbxadmin", owner="xua")
        self.testResult = TestReport()

    def test_Login(self):
        try:
            #self.testcaseinfo.starttime = str(time.asctime())
            # Step1: open base site
            self.driver.get(self.base_url)
            # Step2: Open Login page
            login_page = LoginPage(self.driver)
            # Step3: Enter username
            login_page.set_username("admin")
            time.sleep(2)
            # Step4: Enter password
            login_page.set_password("admin")
            time.sleep(2)
            # 勾选自动登录
            login_page.remenber_pwd()
            time.sleep(2)
            #点击登录按键
            login_page.click_SignIn()
            time.sleep(2)

            # Checkpoint1: Check popup dialog title
            #self.assertEqual(login_page.get_DiaglogTitle(), "Sign in", "Not Equal")
            # Step5: Cancel dialog
            #login_page.click_cancel()

            self.testcaseinfo.result = "Pass"
        except Exception as err:
            self.testcaseinfo.errorinfo = str(err)
        finally:
            self.testcaseinfo.endtime = str(time.asctime())

    # tearDown
    def tearDown(self):
        self.driver.close()
        # write test result
        self.testResult.WriteHTML(self.testcaseinfo)


if __name__ == "__main__":
    unittest.main()