from selenium import webdriver
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://172.16.34.150/#/login')
import time

'''成功登录'''
driver.find_element_by_css_selector('input#username').clear()
driver.find_element_by_css_selector('input#username').send_keys('admin')
driver.find_element_by_css_selector('input#password').clear()
driver.find_element_by_css_selector('input#password').send_keys('admin')
driver.find_element_by_css_selector('input#submit').click()
time.sleep(1.5)
'''跳转到训练任务管理Tab'''
driver.get('http://172.16.34.150/#/jobcreation')
'''进入新建任务界面'''
# driver.find_element_by_css_selector('jobcreation[_nghost-c7]>div>div>div>div>div:nth-child(2)>a.back').click()
driver.find_element_by_css_selector('jobcreation[_nghost-c7] a.back').click()
# driver.find_element_by_css_selector('jobcreation[_nghost-c7]>a.back').click()
'''输入任务名称'''
driver.find_element_by_css_selector('div#step_content>div.allContent>div:nth-child(1) input').clear()
driver.find_element_by_css_selector('div#step_content>div.allContent>div:nth-child(1) input').send_keys('字母图像分类')
'''场景选择--图像分类'''
driver.find_element_by_css_selector('div#step_content>div.allContent>div:nth-child(2) select>option[value="3"]').click()
time.sleep(1)
'''算法链选择'''
driver.find_element_by_css_selector('div#step_content>div.allContent>div:nth-child(3) select>option[value="image classification unittest"]').click()
'''输入CPU核数和物理内存'''



