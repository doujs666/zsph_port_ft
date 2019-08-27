# -*- coding: utf-8 -*
from django.db import models


# Django的模型文件，创建用用程序数据表模型（对应数据库的相关操作）
# Create your models here.


# 项目信息
class project_message(models.Model):
    name = models.CharField(max_length=10)  # 项目名称
    type = models.CharField(max_length=10)  # 项目类型
    versions = models.CharField(max_length=10)  # 项目版本
    update_time = models.DateField('events time')  # 更新时间
    port_count = models.IntegerField()  # 接口数量
    create_time = models.DateField(auto_now=True)  # 创建时间（自动获取当前时间）
    host = models.CharField(max_length=30)  # ip地址
    sql_address = models.CharField(max_length=10)  # sql地址
    mongodb_address = models.CharField(max_length=10)  # mongodb地址
    explain = models.TextField()  # 说明

    def __str__(self):
        return self.name


# host配置
class host_page(models.Model):
    name = models.CharField(max_length=10)  # 名称
    host = models.GenericIPAddressField()  # ip地址
    port = models.CharField(max_length=10)  # 端口

    def __str__(self):
        return self.name


# mysql配置
class mysql_page(models.Model):
    name = models.CharField(max_length=20)  # 名称
    host = models.CharField(max_length=50)  # ip地址
    port = models.CharField(max_length=20)  # 端口
    user = models.CharField(max_length=20)  # user
    password = models.CharField(max_length=20)  # password

    def __str__(self):
        return self.name


# mongodb配置
class mongodb_page(models.Model):
    name = models.CharField(max_length=20)  # 名称
    host = models.CharField(max_length=50)  # ip地址
    port = models.CharField(max_length=20)  # 端口
    user = models.CharField(max_length=20)  # user
    password = models.CharField(max_length=20)  # password

    def __str__(self):
        return self.name


# 接口
class port_manage(models.Model):
    project_name = models.CharField(max_length=20)  # 项目名称
    project = models.ForeignKey(project_message, on_delete=models.CASCADE)  # 关联project
    port_name = models.CharField(max_length=20)  # 接口名称
    url = models.CharField(max_length=100)  # url
    request_raw = models.CharField(max_length=10)  # request_raw
    key = models.CharField(max_length=100, blank=True, null=True, default=None)  # key

    def __str__(self):
        return self.port_name


# 测试用例
class test_case(models.Model):
    # 测试用例
    id = models.CharField(max_length=35, primary_key=True)
    test_case_name = models.CharField(max_length=15)  # 用例名称
    login_status = models.CharField(max_length=5)  # 登录状态
    mobile = models.CharField(max_length=11)  # 手机号
    password = models.CharField(max_length=6)  # 密码
    project_id = models.CharField(max_length=100)  # 项目id
    select_port = models.CharField(max_length=20)  # 选择接口
    port_url = models.CharField(max_length=50)  # 接口url
    key = models.CharField(max_length=100, blank=True, null=True, default=None)  # key
    value = models.CharField(max_length=100, blank=True, null=True, default=None)  # value

    def __str__(self):
        return self.test_case_name


# 前置条件
class Precondition(models.Model):
    login_status = models.CharField(max_length=5, blank=True, null=True, default=None)  # 登录状态
    mobile = models.CharField(max_length=11, blank=True, null=True, default=None)  # 手机号
    password = models.CharField(max_length=6, blank=True, null=True, default=None)  # 密码
    project_url = models.CharField(max_length=100)  # 项目url
    select_port = models.CharField(max_length=20)  # 选择接口
    port_url = models.CharField(max_length=50)  # 接口url
    key = models.CharField(max_length=100, blank=True, null=True, default=None)  # key
    value = models.CharField(max_length=100, blank=True, null=True, default=None)  # key
    test_case = models.ForeignKey(test_case, on_delete=models.CASCADE)  # 关联test_case


# assert
class db_assert(models.Model):
    # 验证
    assert_input = models.CharField(max_length=100, blank=True, null=True, default=None)  # input
    select_assert = models.CharField(max_length=30, blank=True, null=True, default=None)  # assert
    assert_type = models.CharField(max_length=30, blank=True, null=True, default=None)  # assert_type
    assert_input1 = models.CharField(max_length=100, blank=True, null=True, default=None)  # input1
    test_case = models.ForeignKey(test_case, max_length=36, on_delete=models.CASCADE)  # 关联test_case
    count = models.IntegerField()  # 计数
