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
        for name in name_depart:
            name_list.append(name.text)
        return name_list
