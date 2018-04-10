from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('http://172.16.34.150/#/login')
'''登录操作'''
driver.find_element_by_css_selector('input#username').clear()
driver.find_element_by_css_selector('input#username').send_keys('admin')
driver.find_element_by_css_selector('input#password').clear()
driver.find_element_by_css_selector('input#password').send_keys('admin')
driver.find_element_by_css_selector('input#submit').click()
time.sleep(1.5)
# driver.get('http://172.16.34.150/#/datasets')
# '''验证登录成功'''
# driver.find_element_by_xpath('//div[@class = "header"]/div[1]/span').click()
# driver.find_element_by_css_selector('div.header>div:nth-child(1)>span').click()
# tittle = driver.find_element_by_css_selector('body > navigation > div > p').text
'''点击进入数据集管理Tab'''
driver.find_element_by_css_selector('body > navigation >nav[_ngcontent-c0]>div:nth-child(5)>a[_ngcontent-c0]').click()
time.sleep(1)
'''点击删除数据集按键'''
driver.find_element_by_css_selector('table.table>tbody>tr:nth-child(2)>td:nth-child(7)>img.icon').click()
time.sleep(0.5)
'''取消删除'''
driver.find_element_by_css_selector('div.op.item>div.cancel.btn').click()
time.sleep(1.5)
'''点击删除按键'''
driver.find_element_by_css_selector('table.table>tbody>tr:nth-child(2)>td:nth-child(7)>img.icon').click()
time.sleep(1.5)
driver.find_element_by_css_selector('div.op.item>div.sure.btn').click()

