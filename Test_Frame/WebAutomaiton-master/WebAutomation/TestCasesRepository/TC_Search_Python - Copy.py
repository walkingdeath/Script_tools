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
        self.driver = webdriver.Chrome()
        self.base_url = cc.baseUrl()
        self.testCaseInfo = TestCaseInfo(id=1,name="Test search Python",owner='qgk')
        self.testResult = TestReport()
        LogUtility.CreateLoggerFile("Test_Google_Search_Python")

    def test_searchPython(self):
        try:
            self.testCaseInfo.starttime = cc.getCurrentTime()

            #Step1: open base site
            LogUtility.Log("Open Base site"+self.base_url)
            self.driver.get(self.base_url)
            self.driver.maximize_window()
            time.sleep(2)

            #Step2: Open Login page
            # googleSearch = GoogleMainPage()
            #
            # googleSearch.inputSearchContent('Python')

            time.sleep(2)
            assert('Python' in self.driver.title)

            self.testCaseInfo.result = "Pass"

        except Exception as err:
            self.testCaseInfo.errorinfo = str(err)
            LogUtility.Log(("Got error: "+str(err)))
        finally:
            self.testCaseInfo.endtime = cc.getCurrentTime()
            self.testCaseInfo.secondsDuration = cc.timeDiff(self.testCaseInfo.starttime,self.testCaseInfo.endtime)
        pass
    def tearDown(self):
        self.driver.close()
        self.testResult.WriteHTML(self.testCaseInfo)

if __name__ == '__main__':
    unittest.main()
