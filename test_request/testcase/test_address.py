#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pytest

from test_request.test_jkkj import Address


class TestAddress:
    def setup(self):
        self.address = Address()

    @pytest.mark.parametrize("userid, mobile", [('wanglaowu123', '13488889999'),
                                                ('wanglaowu456', '13488889998')])
    def test_add_members(self, userid, mobile):
        name = "王老五"
        department = [1]
        # 数据清理
        self.address.delete_members(userid)
        # 创建成员
        self.address.add_members(userid=userid, name=name, mobile=mobile, department=department)
        # 查询结果
        r = self.address.search_members(userid=userid)
        # 对比结果
        assert r.get("name", "userid 添加失败") == name

    def test_search_members(self):
        pass
