# -*- coding:utf-8 -*-

from base.base_api import BaseApi
from base.login_api import LoginApi
import requests
import base.settings as settings


class LoginBaseApi(BaseApi):

    def __init__(self, mobile, password, *args, **kwargs):
        super(LoginBaseApi, self).__init__(*args, **kwargs)
        self.mobile = mobile
        self.password = password

    def get_token(self):
        """
        获取token
        :return:
        """
        login_api = LoginApi()
        login_api.post({"mobile": self.mobile, "password": self.password})
        token = login_api.get_resp_data()['token']
        return token

    def get(self, data=None):
        """
        请求方式：GET
        :param data:
        :return:
        """
        token = self.get_token()
        s = requests.session()
        settings.API_HEADERS["access-token"] = token
        hander = settings.API_HEADERS
        if data == None:
            new_url = self.api_url()
        else:
            new_url = self.api_url() + data
        self.response = s.get(url=new_url, headers=hander)
        return self.response

    def post(self, payload=None):
        """
        请求方式：POST
        :param payload:
        :return:
        """
        token = self.get_token()
        request_data = self.format_param(payload)
        s = requests.session()
        # s.cookies.set(token)
        settings.API_HEADERS["access-token"] = token
        hander = settings.API_HEADERS
        self.response = s.post(url=self.api_url(), json=request_data, headers=hander)
        return self.response

    def put(self, payload=None):
        """
        请求方式：PUT
        :param payload:
        :return:
        """
        token = self.get_token()
        request_data = self.format_param(payload)
        s = requests.session()
        settings.API_HEADERS["access-token"] = token
        hander = settings.API_HEADERS
        self.response = s.put(url=self.api_url(), json=request_data, headers=hander)
        return self.response
