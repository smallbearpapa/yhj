# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
#声明浏览器对象
browser=webdriver.PhantomJS()
try:
    #访问页面
    browser.get("https://www.baidu.com")
    #打印页面标题
    print(browser.title)
    #打印页面源代码
    print(browser.page_source)
    input=browser.find_element_by_id("kw")
    input.send_keys("Python")
    input.send_keys(Keys.ENTER)
    wait=WebDriverWait(browser,10)
    wait.until(EC.presence_of_element_located((By.ID,"content_left")))
    print(browser.current_url)
    print(browser.get_cookies())
    #查找单个元素
    browser=webdriver.PhantomJS()
    browser.get("http://www.taobao.com")
    input_first=browser.find_element_by_id("q")
    input_second=browser.find_element_by_css_selector("#q")
    print(input_first)
    print(input_second)
    #多个元素
    lis=browser.find_elements_by_css_selector(".service-bd li")
    print(lis)
    lis=browser.find_elements(By.CSS_SELECTOR,".service-bd li")
    print(lis)
    #元素交互操作
    import time
    browser=webdriver.PhantomJS()
    browser.get("http:///www.taobao.com")
    input=browser.find_element_by_id('q')
    input.send_keys("iphone")
    time.sleep(1)
    input.clear()
    input.send_keys("ipad")
    button=browser.find_elements_by_class_name("btn-search")
    #button.click()
    print("button",button)
    #获取文本值
    browser=webdriver.PhantomJS()
    browser.get("http://www.zhihu.com/explore")
    input=browser.find_element_by_class_name("zu-top-add-question")
    print(input.text)
    #获取ID
    print(input.id)
    #获取位置
    print(input.location)
    #获取标签名称
    print(input.tag_name)
    #获取在浏览器中的大小
    print(input.size)
    #显示等待
    browser=webdriver.PhantomJS()
    browser.get("https://www.taobao.com/")
    #传入最长等待时间，为10秒
    wait=WebDriverWait(browser,10)
    input=wait.until(EC.presence_of_element_located((By.ID,"q")))
    button=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".btn-search")))
    print(input,button)
finally:
    browser.close()