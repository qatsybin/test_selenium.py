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

    def add_member(self, name, id, tel):
        self.driver.implicitly_wait(5)
        # 点击添加成员
        self.find(By.XPATH,'//*[@class="ww_operationBar"]/a[1]').click()
        # self.find(By.CSS_SELECTOR,
        #           '#main>div>div>div:nth-child(2)>div>div:nth-child(2)>div:nth-child(3)>div:nth-child(1)>a.qui_btn.ww_btn.js_add_member').click()
        # 输入姓名
        self.find(By.ID, 'username').send_keys(name)
        # 输入账号
        self.find(By.ID, 'memberAdd_acctid').send_keys(id)
        # 输入手机号
        self.find(By.ID, 'memberAdd_phone').send_keys(tel)
        toast1 = self.find(By.CSS_SELECTOR,'.member_edit_sec>div.member_edit_item_Account>div>div').text
        if toast1 == f"该帐号已被“{name}”占有":
            id = id + '1'
            self.find(By.ID, 'memberAdd_acctid').clear()
            self.find(By.ID, 'memberAdd_acctid').send_keys(id)
        toast2 = self.find(By.XPATH, '//*[@class="member_edit_formWrap "]/div[2]/div[1]/div/div[2]').text
        print(toast2)
        if toast2 == f'该手机已被“{name}”占有':
            tel = tel + 1
            self.find(By.ID, 'memberAdd_phone').clear()
            self.find(By.ID, 'memberAdd_phone').send_keys(tel)
        # 点击保存
        self.find(By.CSS_SELECTOR, '#main>div>div>div:nth-child(2)>div>div:nth-child(4)>div>form>div:nth-child(3)>a.qui_btn.ww_btn.js_btn_save').click()
        return ContactPage(self.driver)
