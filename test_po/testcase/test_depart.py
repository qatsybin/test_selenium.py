#!/usr/bin/env python
# -*- coding:utf-8 -*-
from test_po.page.base_page import BasePage
from test_po.page.main_page import MainPage


class TestAddDepart:
    def setup_class(self):
        self.main = MainPage()

    def test_add_department(self):
        # 实例化MainPage类

        result = self.main.goto_add_department().add_department("LG5期学员").get_list()
        assert "LG5期学员" in result
