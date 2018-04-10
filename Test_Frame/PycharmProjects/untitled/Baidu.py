from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://www.baidu.com')
# above = driver.find_element_by_css_selector('div#u1>a[name="tj_settingicon"]')


# driver.find_element_by_css_selector('div#u1>a[name="tj_settingicon"]').click()
# hidden_submenu = driver.find_element_by_css_selector('div.bdpfmenu>div.bdnuarrow>a:nth-child(1)')
# ActionChains(driver).move_to_element(above).perform()

# driver.find_element_by_link_text('搜索设置').click()

# driver.find_element_by_css_selector('div#wrapper>div:nth-child(7)>a:nth-child(1)').click()

# style = driver.find_element_by_css_selector('div#wrapper>div.bdpfmenu').get_attribute('style')
# print(style)


link = driver.find_element_by_link_text('设置')
ActionChains(driver).move_to_element(link).perform()
driver.find_element_by_css_selector('#wrapper > div.bdpfmenu > a.setpref').click()
# driver.find_element_by_link_text('搜索设置').click()


