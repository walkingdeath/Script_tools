from selenium import webdriver
driver = webdriver.Chrome()
import time

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
'''点击上传数据集按键'''
driver.find_element_by_css_selector('body > navigation >nav[_ngcontent-c0]>div:nth-child(5)>a[_ngcontent-c0]').click()
driver.find_element_by_css_selector('div.upload-dataset').click()
time.sleep(1.5)
'''输入上传的数据集名称'''
driver.find_element_by_css_selector('div.form.item>div.inputContainer>input').clear()
driver.find_element_by_css_selector('div.form.item>div.inputContainer>input').send_keys(u'猫狗')
'''上传数据集选择分类'''
driver.find_element_by_css_selector('div.form.item>div.selectContainer>'
                                    'select>option:nth-child(5)').click()
time.sleep(1)
driver.find_element_by_css_selector('div.form.item>div.selectContainer>'
                                    'select>option:nth-child(1)').click()
time.sleep(1)
driver.find_element_by_css_selector('div.upload-dataset.resumable-browse>input:nth-last-child(1)').send_keys('F:\qgk\项目\公司项目\DeepTAC\深度学习数据\cat&dog123.zip')

