from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('http://172.16.34.150:81/#/login')
# driver.maximize_window()

#等待10秒
'''登录'''
driver.implicitly_wait(10)
driver.find_element_by_id("username").clear()
# time.sleep(1.5)
driver.find_element_by_id("username").send_keys('admin')
# time.sleep(1.5)
driver.find_element_by_id("password").clear()
# time.sleep(1.5)
driver.find_element_by_id("password").send_keys('admin')
# time.sleep(1.5)
driver.find_element_by_id('submit').click()
# time.sleep(1.5)

'''新建实时流通道--通过输入通道方式'''
driver.find_element_by_class_name('back').click()
driver.find_element_by_name('appName').clear()
#输入项目名称
driver.find_element_by_name('appName').send_keys('输入通道新建实施项目')
#选择项目类别--实时流分析
driver.find_element_by_xpath("//div[@id='appManage']/div/div/div[2]/select/option[1]").click()
time.sleep(1.5)
driver.find_element_by_xpath("//div[@id='appManage']/div/div/div[2]/select/option[2]").click()
time.sleep(1.5)
driver.find_element_by_xpath("//div[@id='appManage']/div/div/div[2]/select/option[1]").click()
#通道配置--导入通道
driver.find_element_by_xpath("//*[@id='appManage']/div/div/div[3]/span[1]/span[2]/img").click()
driver.find_element_by_xpath("//input[@id='file']").send_keys(r"F:\qgk\项目\公司项目\深瞳\离线分析视频\template.xlsx")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="appManage"]/div/div/div[4]/a[1]').click()


# driver.find_element_by_xpath("//input[@name='channelName' and @type = 'text']").clear()
# driver.find_element_by_xpath("//input[@name='channelName' and @type = 'text']").send_keys('香港HK')




# '''验证登录成功用户名'''
# h = driver.window_handles
# print(h)
# iframe = driver.find_element_by_id('_LeftArea')
# driver.switch_to.frame(iframe)
# # driver.switch_to.frame('_LeftArea')
# time.sleep(1.5)
# driver.find_element_by_id('_Menu_456').click()
# time.sleep(1.5)
# driver.find_element_by_xpath('//div[@id="_ChildMenuItem_450"]/b/span').click()
# # driver.find_element_by_xpath('/html/body/div[1]/div[2]/a[2]/font').click()
# # driver.find_element_by_id('_ButtonOK__DialogAlert0').click()
# # t =driver.find_element_by_xpath('/html/body/div/strong').text
