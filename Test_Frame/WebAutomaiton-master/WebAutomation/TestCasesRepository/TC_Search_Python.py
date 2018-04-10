import unittest
#from selenium import webdriver
from WebAutomation.WebPages.GoogleMainPage import GoogleMainPage
from WebAutomation.CommonLibrary.CommonConfiguration import CommonConfiguration
from WebAutomation.CommonLibrary.TestCaseInfo import TestCaseInfo
from WebAutomation.CommonLibrary.TestReport import TestReport
from _datetime import datetime
from WebAutomation.CommonLibrary.LogUtility import LogUtility
import time


cc = CommonConfiguration()
LogUly = LogUtility()
class Test_TC_Login(unittest.TestCase):

    def setUp(self):
        self.base_url = cc.baseUrl()
        self.testCaseInfo = TestCaseInfo(id=1,name="Test search Python",owner='xua')
        self.testResult = TestReport()
        LogUly.CreateLoggerFile("Test_Google_Search_Python")

    def test_searchPython(self):
        try:
            self.testCaseInfo.starttime = cc.getCurrentTime()

            #Step1: open base site
            LogUly.Log("Open Base site"+self.base_url)
            googleSearch = GoogleMainPage()
  
            googleSearch.open(self.base_url)
            #self.driver.get(self.base_url)
            #self.driver.maximize_window()
            #Step2: Open Login page
         

            googleSearch.inputSearchContent('Python')

            time.sleep(2)
            title = googleSearch.getTitle()
            
            assert('Python' in title)
            print(title)

            self.testCaseInfo.result = "Pass"

        except Exception as err:
            self.testCaseInfo.errorinfo = str(err)
            LogUly.Log(("Got error: "+str(err)))
        finally:
            self.testCaseInfo.endtime = cc.getCurrentTime()
            self.testCaseInfo.secondsDuration = cc.timeDiff(self.testCaseInfo.starttime,self.testCaseInfo.endtime)
        pass
    def tearDown(self):
        #self.driver.close()
        self.testResult.WriteHTML(self.testCaseInfo)

if __name__ == '__main__':
    unittest.main()
