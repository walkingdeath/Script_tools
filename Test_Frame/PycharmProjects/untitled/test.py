from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('http://101.201.151.21:8088/ruiCms/Login.jsp')
driver.maximize_window()

#等待10秒
'''登录'''
driver.implicitly_wait(10)
driver.find_element_by_id("UserName").clear()
time.sleep(1.5)
driver.find_element_by_id("UserName").send_keys('会计')
time.sleep(1.5)
driver.find_element_by_id("Password").clear()
time.sleep(1.5)
driver.find_element_by_id("Password").send_keys('qgk')
time.sleep(1.5)
driver.find_element_by_class_name('inputButton').click()
time.sleep(1.5)
'''验证登录成功用户名'''
h = driver.window_handles
print(h)
iframe = driver.find_element_by_id('_LeftArea')
driver.switch_to.frame(iframe)
# driver.switch_to.frame('_LeftArea')
time.sleep(1.5)
driver.find_element_by_id('_Menu_456').click()
time.sleep(1.5)
driver.find_element_by_xpath('//div[@id="_ChildMenuItem_450"]/b/span').click()
# driver.find_element_by_xpath('/html/body/div[1]/div[2]/a[2]/font').click()
# driver.find_element_by_id('_ButtonOK__DialogAlert0').click()
# t =driver.find_element_by_xpath('/html/body/div/strong').text


