#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
将多个文件都需要调用的类/方法放到这
"""
import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, base_driver=None):
        # 使用selenium.webdriver.remote.webdriver，可以联想出点后面的提示
        base_driver: WebDriver
        # 避免打开多个测试窗口
        if base_driver is None:
            self.driver = webdriver.Chrome()
            self._cookie_login()
        else:
            self.driver = base_driver
        self.driver.implicitly_wait(5)

    def _cookie_login(self):
        self.driver.get("https://work.weixin.qq.com/")
        # 读取本地的cookie文件并取值，登录
        with open("cookie.json", "r") as f:
            cookies = json.load(f)
        # 注入cookie
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(3)
        # 点击通讯录tab
        self.driver.find_element(By.XPATH, "//*[@id='menu_contacts']").click()
        sleep(3)
