#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests

from test_request.api.base import BasePage


class Address(BasePage):
    def add_members(self, userid, name, mobile, department, **kwargs):
        url_add = f"https://qyapi.weixin.qq.com/cgi-bin/user/create"
        body = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department
        }
        body.update(kwargs)
        return self.send("post", url_add, json=body)

    def search_members(self, userid):
        url_r = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?userid={userid}"
        return self.send("get", url_r)

    def update_members(self, userid, name, mobile, department, **kwargs):
        url_up = f"https://qyapi.weixin.qq.com/cgi-bin/user/update"
        body = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department,
        }
        body.update(kwargs)
        return self.send("post", url_up, json=body)

    def delete_members(self, userid):
        url_del = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?userid={userid}"
        return self.send("get", url_del)
