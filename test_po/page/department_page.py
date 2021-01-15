#!/usr/bin/env python
# -*- coding:utf-8 -*-
from time import sleep

from selenium.webdriver.common.by import By

from test_po.page.base_page import BasePage
from test_po.page.contact_page import ContactPage


class AddDepartPage(BasePage):
    def add_department(self, name):
        # 点击添加按钮
        self.find(By.CSS_SELECTOR, '.member_colLeft_top_addBtn').click()
        # 下拉列表选择添加部门
        self.find(By.CSS_SELECTOR, '.js_create_party').click()
        sleep(2)
        # 获取弹窗，并输入部门
        self.find(By.XPATH, '//*[@name="name"]').send_keys(name)
        sleep(2)
        # 下拉列表选择部门
        self.find(By.CSS_SELECTOR, '.js_parent_party_name').click()
        sleep(2)
        self.find(By.CSS_SELECTOR, '.qui_dialog_body.ww_dialog_body [id="1688851247749683_anchor"]').click()
        sleep(2)
        self.find(By.XPATH, '//*[@class="qui_dialog_foot ww_dialog_foot"]/a[1]').click()
        sleep(2)
        toast = self.find(By.ID, 'js_tips')
        text = toast.get_attribute('textContent')
        if text == '该部门已存在':
            return ContactPage(self.driver)
        else:
            self.driver.refresh()
            sleep(5)
            return ContactPage(self.driver)
