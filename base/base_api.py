# -*- coding: utf-8 -*-
# from base.base_log import BaseLogger
import json
import requests
from base import settings


# logger = BaseLogger(__name__).get_logger()


class BaseApi(object):
    ajax = False

    def __init__(self):
        self.response = None
        self.headers = settings.API_HEADERS

    def api_url(self, base_url, api_url):
        """
        拼接url
        :return:
        """
        url = "{0}{1}".format(base_url, api_url)
        return url

    def port(self, request_raw, url, payload=None):
        """
        请求方式：POST
        :param:
        :return:
        """
        headers = settings.API_HEADERS
        self.response = requests.request(request_raw, url, json=payload, headers=headers)
        return self.response

    def get_status_code(self):
        """
        返回请求状态码
        :return:
        """
        return self.response.status_code

    def get_resp_data(self):
        """
        获取回参中data
        :return:
        """
        return json.loads(self.response.text)

    # def get_resp_header(self):
    #     """
    #     获取回参中header
    #     :return:
    #     """
    #     if self.response:
    #         return json.loads(self.response.text)['header']

    def get_resp_result(self):
        """
        获取回参中result
        :return:
        """
        return json.loads(self.response.text)['result']

    # def get_resp_banners(self):
    #     """
    #     获取回参中banners
    #     :return:
    #     """
    #     if self.response:
    #         return json.loads(self.response.text)['data']['banners']
