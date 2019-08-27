# coding:utf-8
# Create your views here.
# Django的视图文件，控制向前端页面显示的内容
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign.models import project_message
# from sign.models import mysql_page
from sign.models import mongodb_page
from sign.models import port_manage as port_manage_db
from sign.models import Precondition
from sign.models import test_case
from sign.models import db_assert
from datetime import datetime
import requests
from sign.tests import Demo
from base.base_api import BaseApi
import uuid
from base.my_sql import MysqlHelper


# 登录
def login(request):
    return render(request, 'login.html')


# 登录动作
def login_action(request):
    if request.method == "POST":
        # 寻找名为 "username"和"password"的POST参数，而且如果参数没有提交，返回一个空的字符串。
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        if username == '' or password == '':
            return render(request, "login.html", {"error": "username or password null!"})

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)  # 验证登录
            response = HttpResponseRedirect('/index/')  # 登录成功跳转发布会管理
            request.session['username'] = username  # 将 session 信息写到服务器
            return response
        else:
            return render(request, "login.html", {"error": "username or password error!"})
    # 防止直接通过浏览器访问 /login_action/ 地址。
    return render(request, "login.html")


# 首页
@login_required
def index(request):
    return render(request, "index.html")


# 退出登录
@login_required
def logout(request):
    auth.logout(request)
    response = HttpResponseRedirect('/login/')
    return response


# 项目管理
@login_required
def project_manage(request):
    project_list = project_message.objects.all()
    return render(request, "project_manage.html", {"project_list": project_list})


# 基础模板
def base(request):
    return render(request, "base.html")


# 新建和修改项目
def fix_project(request):
    project_id = request.GET.get('id', None)
    if project_id is None:
        return render(request, "fix_project.html")
    else:
        fix_project_data = project_message.objects.get(id=project_id)
        return render(request, "fix_project.html", {'fix_project_data': fix_project_data})


# 新建和修改项目表单动作
@login_required
def fix_project_action(request):
    project_id = request.GET.get('id', None)
    if request.method == 'POST':
        project_name = request.POST.get("project_name", "")
        project_type = request.POST.get("project_type", "")
        project_version = request.POST.get("project_version", "")
        port_count = request.POST.get("port_count", "")
        project_host = request.POST.get("project_host", "")
        sql_address = request.POST.get("sql_address", "")
        mongodb_address = request.POST.get("mongodb_address", "")
        explain = request.POST.get("explain", "")
        if project_id is '':
            project_message.objects.create(name=project_name, type=project_type, versions=project_version,
                                           create_time=datetime.today(), update_time=datetime.today(),
                                           port_count=port_count,
                                           host=project_host, sql_address=sql_address,
                                           mongodb_address=mongodb_address,
                                           explain=explain)
        else:
            project_message.objects.filter(id=project_id).update(name=project_name, type=project_type,
                                                                 versions=project_version, update_time=datetime.today(),
                                                                 explain=explain, port_count=port_count,
                                                                 host=project_host, sql_address=sql_address,
                                                                 mongodb_address=mongodb_address
                                                                 )
        response = HttpResponseRedirect('/project_manage/')
        return response


# 删除项目
@login_required
def delete_project_action(request):
    project_id = request.GET.get('id')
    project_message.objects.filter(id=project_id).delete()
    response = HttpResponseRedirect('/project_manage/')
    return response


# 基础配置
@login_required
def base_page_manage(request):
    return render(request, "base.html")


# 项目详情
@login_required
def project_detail(request):
    project_list = project_message.objects.all()
    return render(request, "project_detail.html", {'project_list': project_list})


# 取消操作
def cancel(request):
    response = HttpResponseRedirect('/index/')
    return response


# mysql列表页
@login_required
def mysql_manage(request):
    mysql_page_list = mysql_page.objects.all()
    return render(request, "mysql_page.html", {'mysql_page_list': mysql_page_list})


# 新建mysql_page
def fix_mysql_page(request):
    return render(request, "fix_mysql_page.html")


# 新建mysql表单动作
@login_required
def fix_mysql_page_action(request):
    if request.method == 'POST':
        mysql_name = request.POST.get("mysql_name", "")
        host = request.POST.get("host", "")
        port = request.POST.get("port", "")
        user = request.POST.get("user", "")
        password = request.POST.get("password", "")
        mysql_page.objects.create(name=mysql_name, host=host, port=port, user=user, password=password)
        response = HttpResponseRedirect('/mysql_page/')
        return response


# 删除mysql_page
@login_required
def delete_mysql_page_action(request):
    mysql_id = request.GET.get('id')
    mysql_page.objects.filter(id=mysql_id).delete()
    response = HttpResponseRedirect('/mysql_page/')
    return response


# mongodb列表页
@login_required
def mongodb_manage(request):
    mongodb_page_list = mongodb_page.objects.all()
    return render(request, "mongodb_page.html", {'mongodb_page_list': mongodb_page_list})


# 新建mongodb_page
def fix_mongodb_page(request):
    return render(request, "fix_mongodb_page.html")


# 新建mongodb表单动作
@login_required
def fix_mongodb_page_action(request):
    if request.method == 'POST':
        mongodb_name = request.POST.get("mongodb_name", "")
        host = request.POST.get("host", "")
        port = request.POST.get("port", "")
        user = request.POST.get("user", "")
        password = request.POST.get("password", "")
        mongodb_page.objects.create(name=mongodb_name, host=host, port=port, user=user, password=password)
        response = HttpResponseRedirect('/mongodb_page/')
        return response


# 删除mysql_page
@login_required
def delete_mongodb_page_action(request):
    mongodb_id = request.GET.get('id')
    mongodb_page.objects.filter(id=mongodb_id).delete()
    response = HttpResponseRedirect('/mongodb_page/')
    return response


# 快速测试
@login_required
def quest_test(request):
    return render(request, "quick_test.html")


# 快速测试表单动作
@login_required
def quest_test_action_ajax(request):
    request_raw = request.POST.get('request_raw')
    quest_test_url = request.POST.get('input_url')
    input1 = request.POST.getlist("input1[]")
    input2 = request.POST.getlist("input2[]")
    payload = request.POST.get('raw')
    headers = dict(zip(input1, input2))

    r = requests.request(request_raw, quest_test_url, data=payload, headers=headers)
    return HttpResponse(r)


# 接口管理
@login_required
def port_manage(request):
    port_list = port_manage_db.objects.all()
    return render(request, "port_manage.html", {"port_list": port_list})


# 新建和修改接口
def fix_port(request):
    port_id = request.GET.get('id', None)
    if port_id is None:
        return render(request, "fix_port.html")
    else:
        fix_port_data = port_manage_db.objects.get(id=port_id)
        keys = port_manage_db.objects.get(id=port_id).key
        new_keys = eval(keys)

        return render(request, "fix_port.html", {'fix_port_data': fix_port_data, 'new_keys': new_keys})


# 新建和修改接口表单动作
@login_required
def fix_port_action(request):
    port_id = request.GET.get('id', None)
    project_id = request.POST.get('project_id')
    project_name = project_message.objects.get(id=project_id).name
    port_name = request.POST.get('port_name')
    url = request.POST.get('url')
    request_raw = request.POST.get('request_raw')
    input1 = request.POST.getlist("input1[]")
    new_key = str(input1)
    if not input1:
        input1 = None
    if port_id is '':
        port_manage_db.objects.create(project_id=project_id, project_name=project_name, port_name=port_name,
                                      url=url, request_raw=request_raw,
                                      key=input1)
    else:
        port_manage_db.objects.filter(id=port_id).update(project_id=project_id, project_name=project_name,
                                                         port_name=port_name, url=url, request_raw=request_raw,
                                                         key=new_key)

    response = HttpResponseRedirect('/port_manage/')
    return response


# 删除接口
@login_required
def delete_port_action(request):
    port_id = request.GET.get('id')
    port_manage_db.objects.filter(id=port_id).delete()
    response = HttpResponseRedirect('/port_manage/')
    return response


# 测试用例管理
@login_required
def test_case_manage(request):
    test_case_list = test_case.objects.all()
    return render(request, "test_case_manage.html", {"test_case_list": test_case_list})


# 新建和修改测试用例
def fix_test_case(request):
    case_id = request.GET.get('id', None)
    if case_id is None:
        return render(request, "fix_test_case.html")
    else:

        # 测试用例显示
        login_status = int(test_case.objects.get(id=case_id).login_status)
        mobile = test_case.objects.get(id=case_id).mobile
        password = test_case.objects.get(id=case_id).password
        project_id = int(test_case.objects.get(id=case_id).project_id)
        project_name = project_message.objects.get(id=project_id).name
        port_id = int(test_case.objects.get(id=case_id).select_port)
        port_url = port_manage_db.objects.get(id=port_id).url
        port_name = port_manage_db.objects.get(id=port_id).port_name
        case_name = test_case.objects.get(id=case_id).test_case_name

        # 处理key和value
        case_key = eval(test_case.objects.get(id=case_id).key)
        case_value = eval(test_case.objects.get(id=case_id).value)
        payload = dict(zip(case_key, case_value))

        db_assert_list = MysqlHelper().get_db_assert(case_id)

        return render(request, "fix_test_case.html",
                      {'login_status': login_status, 'mobile': mobile, 'project_id': project_id,
                       'project_name': project_name, 'port_id': port_id, 'port_url': port_url,
                       'port_name': port_name, 'case_name': case_name, 'payload': payload,
                       'db_assert_list': db_assert_list,
                       })


# 获取前置接口值
@login_required
def get_init_port_value(request):
    select_port = request.POST.get('select_init_port')
    keys = port_manage_db.objects.get(id=select_port).key
    url = port_manage_db.objects.get(id=select_port).url
    port_init_value = {}
    port_init_value['url'] = url
    port_init_value['keys'] = keys
    return JsonResponse(port_init_value)


# 获取前置条件接口值
@login_required
def get_preposition_value(request):
    # 获取ID
    test_case_id = request.GET.get('id', None)

    # 获取前端信息
    select_login = request.POST.get('select_login')
    mobile = request.POST.get('mobile')
    password = request.POST.get('password')
    select_port = request.POST.get('select_port')
    request_raw = port_manage_db.objects.get(id=select_port).request_raw  # 请求方式
    port_url = request.POST.get('port_url')
    data_key = request.POST.getlist("data_key_list[]")
    data_value = request.POST.getlist("data_value_list[]")
    payload = dict(zip(data_key, data_value))
    project_url = request.POST.get('select_manage')  # 选择项目
    new_key = str(data_key)
    new_value = str(data_value)



    # 通过test_case_id查询id
    recondition_id = ''

    # 存储数据
    if not data_key:
        data_key = None
        data_value = None

    if test_case_id is '':
        Precondition.objects.create(login_status=select_login, mobile=mobile, password=password,
                                    project_url=project_url, select_port=select_port,
                                    port_url=port_url, key=data_key, value=data_value)
    else:
        Precondition.objects.filter(id=recondition_id).update(login_status=select_login, mobile=mobile,
                                                              password=password,
                                                              project_url=project_url, select_port=select_port,
                                                              port_url=port_url, key=new_key, value=new_value)

    # 处理信息
    base_api = BaseApi()
    api_url = base_api.api_url(project_url, port_url)
    base_api.port(request_raw, api_url, payload)
    data = base_api.get_resp_data()

    # 返回信息
    response = JsonResponse(data)
    return response


# 获取用例接口值
@login_required
def get_port_value(request):
    select_port = request.POST.get('select_port')
    keys = port_manage_db.objects.get(id=select_port).key
    url = port_manage_db.objects.get(id=select_port).url
    port_value = {}
    port_value['url'] = url
    port_value['keys'] = keys
    return JsonResponse(port_value)


# 新建和修改用例表单动作
@login_required
def fix_test_case_action(request):
    # 获取前端信息
    test_case_id = request.POST.get('case_id')
    select_login = request.POST.get('select_login')
    mobile = request.POST.get('mobile')
    password = request.POST.get('password')
    case_name = request.POST.get('case_name')
    select_port = request.POST.get('select_port')
    port_url = request.POST.get('port_url')
    data_key = request.POST.getlist("data_key_list[]")
    data_value = request.POST.getlist("data_value_list[]")
    payload = dict(zip(data_key, data_value))
    select_project = request.POST.get('select_project')
    new_key = str(data_key)
    new_value = str(data_value)

    # 获取前端验证信息
    assert_input = request.POST.getlist("assert_input[]")
    choose_assert = request.POST.getlist("choose_assert[]")
    assert_type = request.POST.getlist("assert_type[]")
    assert_input1 = request.POST.getlist("assert_input1[]")

    # # 存储数据
    # if not data_key:
    #     data_key = None
    #     data_value = None
    create_test_case_id = ''.join([each for each in str(uuid.uuid1()).split('-')])

    if test_case_id is '':
        # 没有数据存储
        test_case.objects.create(
            id=create_test_case_id,
            login_status=select_login, mobile=mobile, password=password,
            project_id=select_project, select_port=select_port,
            port_url=port_url, key=data_key, value=data_value, test_case_name=case_name,
        )
        for i in range(len(assert_input)):
            db_assert.objects.create(
                assert_input=assert_input[i], select_assert=choose_assert[i],
                assert_type=assert_type[i], assert_input1=assert_input1[i],
                test_case_id=create_test_case_id, count=i
            )

    else:
        test_case.objects.filter(id=test_case_id).update(
            login_status=select_login, mobile=mobile, password=password,
            project_id=select_project, select_port=select_port,
            port_url=port_url, key=data_key, value=data_value, test_case_name=case_name,
        )
        db_assert.objects.filter(test_case_id=test_case_id).delete()
        for i in range(len(assert_input)):
            db_assert.objects.create(
                assert_input=assert_input[i], select_assert=choose_assert[i],
                assert_type=assert_type[i], assert_input1=assert_input1[i],
                test_case_id=test_case_id, count=i
            )

    assert_list = Demo().test_aa(test_case_id)
    result_assert = {}
    result_assert['assert_list'] = assert_list
    return JsonResponse(result_assert)

