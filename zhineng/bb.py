# coding=utf-8

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import re


def login(driver):
    WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("kw")).send_keys(u"selenium")
    WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("su")).click

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("https://www.baidu.com/")
    login(driver)

