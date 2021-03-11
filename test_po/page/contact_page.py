#!/usr/bin/env python
# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By

from test_po.page.base_page import BasePage


class ContactPage(BasePage):
    def goto_add_department(self):
        pass

    def get_list(self):
        name_depart = self.driver.find_elements(By.XPATH, '//*[@class="jstree-anchor"]')
        name_list = []
        for names in name_depart:
            name_list.append(names.text)
        return name_list

    def get_memlist(self, name):

        self.find(By.ID,'memberSearchInput').send_keys(name)
        get_name = self.find(By.XPATH, '//*[@class="member_display_cover_detail_top"]/div[1]').text
        return get_name


