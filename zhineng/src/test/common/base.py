#encoding=utf-8
from selenium import webdriver

def browser(browser):
    try:
        if browser=="chrome":
            driver=webdriver.Chrome()
            return driver
        elif browser=="firefox":
            driver=webdriver.Firefox()
            return driver
        elif browser=="ie":
            driver=webdriver.Ie()
            return driver
        else:
            print "没有找到对应的浏览器"
    except Exception as msg:
        print "%s"%msg

class base():
    def __init__(self,driver):
        self.driver=driver

    def open_url(self,url):
        self.driver.get(url)

    def find_element(self):



