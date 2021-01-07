#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json

import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestNiho():
    def setup_method(self):
        chrome_args = webdriver.ChromeOptions()
        chrome_args.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome()

    # def teardown_method(self):
    #     self.driver.quit()
    def test_cookie(self):
        # cookies = self.driver.get_cookies()
        # with open("cookie.json", "w") as f:
        #     json.dump(cookies, f)
        # 打开目标页面
        self.driver.get("https://work.weixin.qq.com/")
        # 读取本地的cookie文件并取值，登录
        with open("cookie.json", "r") as f:
            cookies = json.load(f)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        time.sleep(3)
        # 点击通讯录tab
        self.driver.find_element(By.XPATH, "//*[@id='menu_contacts']").click()
        time.sleep(3)
        # 点击客户联系tab
        self.driver.find_element(By.XPATH, "//*[@id='menu_customer']").click()
