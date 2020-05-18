#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests


class HttpRequests():
    '''对requests库封装的GET、POST、PUT等方法调用类'''

    def __init__(self, url, data=None, type='GET', cookie=None, headers=None, proxies=None):
        self.url = url
        self.data = data
        self.type = type
        self.cookie = cookie
        self.headers = headers
        self.proxies = proxies
        self.send_request()

    def send_request(self):
        '''setup a request'''

        if self.url == None or self.url == '':
            raise ('The url should not empty!')
        if self.type == 'POST':
            self.req = requests.post(self.url, data=self.data, headers=self.headers, proxies=self.proxies)
        elif self.type == 'GET':
            if self.data == None:
                self.req = requests.get(self.url, headers=self.headers, proxies=self.proxies)
            else:
                self.req = requests.get(self.url, params=self.data, headers=self.headers, proxies=self.proxies)
        elif self.type == 'PUT':
            self.req = requests.put(self.url, data=self.data, headers=self.headers, proxies=self.proxies)
        else:
            self.req = None
            raise ('The http request type NOT support now!')

    def get_code(self):
        try:
            return self.req.status_code
        except:
            raise ('get code fail')

    def get_url(self):
        try:
            return self.req.url
        except:
            raise ('get url fail')

    def get_text(self):
        try:
            return self.req.text
        except:
            raise ('get text fail')

    def get_headers(self):
        try:
            return self.req.headers
        except:
            raise ('get headers fail')

    def get_cookie(self):
        headers = self.get_headers()
        if 'set-cookie' in headers:
            return headers['set-cookie']
        else:
            return None
