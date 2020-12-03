# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.support import ui

from TEST1.password.Password import Password
from selenium.webdriver.support.select import Select
browser = webdriver.Chrome()
def main():
    username = "1"
    password = "2"
    url = "https://login.huawei.com/login/?redirect=http%3A%2F%2Fcbuilder.huawei.com%3A9080%2Funistar%2Fdpm%2FpublishData%21showPublishData.action&lang=en&msg=1&v=V3.44"
    browser.get(url)
    #窗口最大化
    browser.maximize_window()
    sleep(2)
    #输入用户名密码
    login = browser.find_element_by_xpath("//*[@id='uid']")
    login.click()
    username = Password(username)
    #print("输出一",username)
    login.send_keys(username)
    sleep(2)
    login = browser.find_element_by_xpath("//*[@id='password']")
    login.click()
    password = Password(password)
    #print("输出二",password)
    login.send_keys(password)
    #点击登录
    browser.find_element_by_xpath("//*['@id=page-input-holder-pwd']/form/div/input").click()
    sleep(2)
    oprate()
def oprate():
    #发布数据包
    for i in range(2):
        browser.find_element_by_xpath("//*[@id='singleWhole_release_data']/img").click()
        sleep(2)

    #下拉框处理
    #产品线
    for i in range(2):
        xpath = ["//*[@id='productLine']","//*[@id='datapackage']"]
        values = ["12","EPIPENG"]
        #print(xpath[0])
        Product_Line = browser.find_element_by_xpath(xpath[i])
        #print(xpath[i])
        sleep(2)
        select = Select(Product_Line)
        select.select_by_value(values[i])
        sleep(3)
    #选择数据包版本及价格版本
    dr = browser.find_element_by_xpath("//*[@id='dataPackageVersionButton']").click()
    #加上延时判断，等待页面刷新
    #wait = ui.WebDriverWait(dr, 5)
    #wait.until(lambda driver: dr.find_element_by_xpath("/html/body/div[1]/table/tbody/tr[2]/td[1]/input"))
    sleep(5)
    #切换frame到当前窗口
    #browser.find_element_by_xpath("//*[@id='mask']")
    browser.switch_to.frame("jd_iframe")
    #鼠标操作
    '''Mouse=browser.find_element_by_xpath("//*[@id='showAllVersion']")

    #鼠标悬停
    ActionChains(browser).move_to_element(Mouse).perform()
    sleep(2)
    #双击元素
    ActionChains(browser).double_click(Mouse).perform()
    sleep(2)'''
    #xpath定位
    browser.find_element_by_xpath("//*[@id='showAllVersion']").click()
    sleep(2)

    browser.find_element_by_xpath("//*[@id='selectCfgDataVersion']/div[4]/div/div[16]/div[1]/input").click()
    sleep(2)
    browser.switch_to.default_content()
    try :
        browser.find_element_by_xpath("//*[@id='_jd_dialog_m_t']")
    except:
        print("定位成功")
    else:
        print("定位失败")
    app = browser.find_element_by_xpath("//*[@id='saveButton']")
    app.submit()
# print(browser.page_source)
    print(browser.current_url)
    print(browser.current_window_handle)
    sleep(3)
    browser.quit()
if __name__ == '__main__':
    main()