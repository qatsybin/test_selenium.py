#!/usr/bin/env python
# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By

from test_po.page.base_page import BasePage
from test_po.page.department_page import AddDepartPage


class MainPage(BasePage):
    def goto_contact(self):
        pass

    def goto_add_department(self):
        # self.driver.find_element(By.XPATH, '//*[@id="menu_contacts"]/span').click()

        return AddDepartPage(self.driver)
