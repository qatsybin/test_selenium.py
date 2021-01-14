#!/usr/bin/env python
# -*- coding:utf-8 -*-
from test_po.page.base_page import BasePage
from test_po.page.main_page import MainPage


class TestAddDepart:
    def setup_class(self):
        pass

    def test_add_department(self):
        # 实例化MainPage类
        main = MainPage()
        result = main.goto_add_department().add_department().get_list()
        assert "霍格沃兹学院" in result
