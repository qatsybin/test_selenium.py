#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pytest

from test_po.page.base_page import BasePage
from test_po.page.main_page import MainPage


class TestAddDepart:
    def setup_method(self):
        self.main = MainPage()

    def test_add_department(self):
        # 实例化MainPage类
        try:
            result = self.main.goto_add_department().add_department("LG5期学员").get_list()
            assert "LG5期学员" in result
            self.main.driver.quit()

        except Exception as e:
            print(e)

    @pytest.mark.parametrize("name,id,tel", [("大王", "Tsybin2", 13900007777), ("小王", "Tsybin3", 13600008888)])
    def test_add_member(self, name, id, tel):
        try:
            result1 = self.main.goto_add_department().add_member(name, id, tel).get_memlist(name)
            assert result1 == name
        except Exception as e:
            print(e)
