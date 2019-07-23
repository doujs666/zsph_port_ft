# -*- coding:utf-8 -*-
from base.base_api import BaseApi


class LoginApi(BaseApi):
    """
    登录接口
    """
    url = 'authentication/login'

    def build_custom_param(self, data):
        return {'mobile': data['mobile'], 'password': ['password']}

