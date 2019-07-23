# -*- coding:utf-8 -*-
import base.base_mysql as base_mysql
from base.base_mysql import local_execute


class MysqlHelper(object):

    # def get_single_query_list(self):
    #     """
    #     获取等待分配窗口信息用户列表
    #     :return:
    #     """
    #     single_list = base_mysql.execute(
    #         'select distinct user_id from (select * from lot_order where project_id is null and '
    #         '(order_status = 0 or order_status = 1)) t limit 0,5', is_fetchone=False)
    #     return single_list

    def get_db_assert(self, case_id):
        """
        获取case_id
        :param case_id:
        :return:
        """
        db_assert_list = base_mysql.local_execute('SELECT * FROM sign_db_assert where test_case_id=%s',
                                                  params=case_id, is_fetchone=False)
        return db_assert_list
