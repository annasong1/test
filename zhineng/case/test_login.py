#coding=utf-8
import  unittest
from selenium import webdriver
from selenium import *
from selenium.webdriver.support.wait import WebDriverWait
import ddt
import time
import readexcel
import os
from src.untils.config import Config
from src.untils.file_reader import yamlreader
import yaml
from src.untils.log import Logger
from src.test.common.base import browser
from src.test.common.base import base


BASE_PATH = os.path.dirname(os.path.dirname(__file__))
filepath = os.path.join(BASE_PATH, 'data', 'aa.xlsx')
sheetname="Sheet1"
testdata=readexcel.readexcel(filepath,sheetname).data_dirct()
mylogger=Logger('TestMyLog').getlog()

@ddt.ddt
class login(unittest.TestCase):

    URL = Config().get('D:\\aa\\zhineng\\config\\config.yml','URL')



    @ddt.data(*testdata)
    def testLogin01(self,data):
        U"测试百度搜索"
        self.driver = browser('chrome')
        base(self.driver).open_url(self.URL)


        mylogger.info(u"打开浏览器")
        WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id("kw")).send_keys(data["username"])
        self.driver.find_element("id", "su").click()
        time.sleep(6)
        aa=self.driver.title
        print aa
        self.assertIn(u"测试", self.driver.title)


    def tearDown(self):
         self.driver.quit()


if __name__ == "__main__":
    unittest.main()

