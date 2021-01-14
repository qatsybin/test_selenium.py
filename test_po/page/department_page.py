#!/usr/bin/env python
# -*- coding:utf-8 -*-
from time import sleep

from selenium.webdriver.common.by import By

from test_po.page.base_page import BasePage
from test_po.page.contact_page import ContactPage


class AddDepartPage(BasePage):
    def add_department(self):
        # 点击添加按钮
        self.driver.find_element(By.CSS_SELECTOR, '.member_colLeft_top_addBtn').click()
        # 下拉列表选择添加部门
        self.driver.find_element(By.CSS_SELECTOR, '.js_create_party').click()
        sleep(2)
        # 获取弹窗，并输入部门
        self.driver.find_element(By.XPATH, '//*[@name="name"]').send_keys("霍格沃兹学院")
        sleep(2)
        # 下拉列表选择部门
        self.driver.find_element(By.CSS_SELECTOR, '.js_parent_party_name').click()
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR,
                                 '.qui_dialog_body.ww_dialog_body [id="1688851247749683_anchor"]').click()
        sleep(2)
        self.driver.find_element(By.XPATH, '//*[@class="qui_dialog_foot ww_dialog_foot"]/a[1]').click()
        sleep(2)
        self.driver.refresh()
        sleep(5)
        return ContactPage(self.driver)
