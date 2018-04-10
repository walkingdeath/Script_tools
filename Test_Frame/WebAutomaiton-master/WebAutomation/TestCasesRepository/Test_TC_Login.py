from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.alert import Alert
import unittest
import time
from WebAutomation.CommonLibrary.LoginPage import LoginPage
from WebAutomation.CommonLibrary.TestCaseInfo import TestCaseInfo
from WebAutomation.CommonLibrary.TestReport import TestReport
from WebAutomation.CommonLibrary import LogUtility
from WebAutomation.CommonLibrary import CommonConfiguration as cc

class Test_TC_Login(unittest.TestCase):
    def setUp(self):
        #print(type(cc.driverPath(self)))
        # self.driver = webdriver.Chrome(cc.driverPath(self))

        self.driver = webdriver.Chrome()
        self.base_url = cc.baseUrl()
        self.testCaseInfo = TestCaseInfo(id=1, name="Test case name", owner='qgk')
        self.testResult = TestReport()
        LogUtility.CreateLoggerFile("Test_TC_Login")

    def test_A(self):
        try:
            self.testCaseInfo.starttime = cc.getCurrentTime()
            login_page = LoginPage(self.driver)
            # Step1: open base site
            LogUtility.Log("Open Base site" + self.base_url)
            #self.driver.get(self.base_url)
            login_page.open(self.base_url)
            # Step2: Open Login page

            # Step3: Enter username & password
            LogUtility.Log("Login web using username")
            login_page.set_username("username")
            login_page.set_password("password")


            time.sleep(2)
            login_page.click_SignIn()
            # Checkpoint1: Check popup dialog title
            # LogUly.Log("Check whether sign in dialog exists or not")
            # self.assertEqual(login_page.get_DiaglogTitle(), "Sign in")

            # time.sleep(3)
            # Step4: Cancel dialog
            # login_page.click_cancel()
            self.testCaseInfo.result = "Pass"

        except Exception as err:
            self.testCaseInfo.errorinfo = str(err)
            print(err)
            LogUtility.Log(("Got error: " + str(err)))
        finally:
            self.testCaseInfo.endtime = cc.getCurrentTime()
            self.testCaseInfo.secondsDuration = cc.timeDiff(self.testCaseInfo.starttime, self.testCaseInfo.endtime)
            #print(self.testCaseInfo.secondsDuration)
    def tearDown(self):
        self.driver.close()
        self.testResult.WriteHTML(self.testCaseInfo)


if __name__ == '__main__':
    unittest.main()