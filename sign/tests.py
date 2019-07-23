# -*- coding:utf-8 -*-
from django.test import TestCase
# 创建Django测试用例
# Create your tests here.

import unittest
from sign.models import Precondition
from sign.models import test_case
from sign.models import db_assert
from sign.models import port_manage
from base.base_api import BaseApi
from sign.models import project_message
from base.my_sql import MysqlHelper


class Demo(TestCase):

    def setUp(self):
        print('setUp')

    # b = self.assert_Equal(2 + 5, 9, '234')
    # a = self.longMessage
    # print(b)

    def test_aa(self, case_id):
        # 读取数据

        project_id = test_case.objects.get(id=case_id).project_id
        project_url = project_message.objects.get(id=project_id).host
        port_url = test_case.objects.get(id=case_id).port_url
        port_id = test_case.objects.get(id=case_id).select_port
        request_raw = port_manage.objects.get(id=port_id).request_raw
        case_key = eval(test_case.objects.get(id=case_id).key)
        case_value = eval(test_case.objects.get(id=case_id).value)
        payload = dict(zip(case_key, case_value))

        # 处理信息
        base_api = BaseApi()
        api_url = base_api.api_url(project_url, port_url)

        base_api.port(request_raw, api_url, payload)

        # 返回信息
        code = base_api.get_status_code()
        data = base_api.get_resp_data()

        # 获取assert
        get_assert_list = MysqlHelper().get_db_assert(case_id)
        assert_list = []
        for i in get_assert_list:
            first = i['assert_input']
            db_select_assert = i['select_assert']
            db_assert_type = i['assert_type']
            db_assert_input1 = i['assert_input1']

            if db_assert_type == 'data':
                second = data[db_assert_input1]

            if db_select_assert == 'assertEqual':
                result_assert = self.assert_Equal(first, second)
                assert_list.append(result_assert)

        return assert_list


# if __name__ == '__main__':
#     # unittest.main()
#     # 构造测试集
#     suit = unittest.TestSuite()
#     suit.addTest(TestMath("test_case"))
#     # 执行测试
#     runner = unittest.TextTestRunner()
#     runner.run(suit)

import unittest
import HTMLTestRunner_KZ
import time

# class DemoTest(unittest.TestCase):
#
#     def test_one(self):
#         print('第一条case')
#
#     def test_two(self):
#         print('第二条case')
#
#
# if __name__ == '__main__':
#     print("开始main")
#     suite = unittest.TestSuite()
#     suite.addTest(DemoTest('test_one'))
#     suite.addTest(DemoTest('test_two'))
#     import os
#     file_path = os.path.join(os.path.dirname(__file__), "wer")
#     print(file_path)
#     REPORT_FILE_NAME = file_path + '/' + time.strftime("%Y%m%d%H%M%S") + '_ess.html'
#     print(REPORT_FILE_NAME)
#     fp = open(REPORT_FILE_NAME, 'wb+')
#
#     runner = HTMLTestRunner_KZ.HTMLTestRunner(stream=fp, title='123', description='132',
#                                             )
#     runner.run(suite)
#
#     fp.close()
#     print(123)
