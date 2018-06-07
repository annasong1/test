#coding=utf-8
from selenium import webdriver
import time
import random
from selenium.webdriver.common.action_chains import ActionChains
import unittest
import HTMLTestRunner
import os
import time
from selenium.webdriver.support.wait import WebDriverWait
import xlrd
from selenium.webdriver.support import expected_conditions as EC
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import csv
import ddt

class test(unittest.TestCase):
    def testBaidu(self):
        driver=webdriver.Firefox()
        driver.get("https://www.baidu.com/")
        WebDriverWait(driver,10).until(lambda x:x.find_element_by_id("kw")).send_keys(u"selenium")
        WebDriverWait(driver,10).until(lambda x:x.find_element_by_id("su")).click
        time.sleep(3)
        ele_string = driver.find_element_by_xpath("//*[@id='1']/h3/a").text
        if (ele_string == u"Selenium - Web Browser Automation"):
            print "测试成功，结果和预期结果匹配！"
            self.assertTrue(1)
        else:
            print "结果不匹配"
            self.assertTrue(0)
case_path=os.getcwd()
now=time.strftime("%Y_%m_%d %H_%M_%S")
report_path=os.path.join(case_path,now+'result.html')


def all_case():
    discover=unittest.defaultTestLoader.discover(case_path,pattern="aa.py",top_level_dir=None)
    return discover

if __name__ == '__main__':
    fp=open(report_path,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='ceshi',description='ceshi')
    runner.run(all_case())
    fp.close()

