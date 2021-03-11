#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests


class BasePage:
    def __init__(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwaf66eaa60b74536f&corpsecret=K4QMvCs00L4J1HBKYfXakPsCqHOALt1B7lIIw3CFu1Q"
        r = requests.get(url).json()
        self.token = r['access_token']
        # 声明一个session
        self.s = requests.Session()
        # 把token放入到session中，每次参数都有token
        self.s.params = {'access_token': self.token}

    def send(self, *args, **kwargs):
        # 用session发request
        r = self.s.request(*args, **kwargs)
        return r.json()
