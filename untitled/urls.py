"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from static.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sign import views
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # route包含URL模式的字符串, view调用指定的视图函数
    path('admin/', admin.site.urls),
    path('login/', views.login),  # 登录
    path('login_action/', views.login_action),  # 登录动作
    path('index/', views.index),  # 首页
    path('logout/', views.logout),  # 登出
    path('project_manage/', views.project_manage),  # 项目管理
    path('base/', views.base),     # base
    url(r'^delete_project/$', views.delete_project_action),  # 删除项目
    url(r'^update_project/$', views.fix_project),  # 修改和新建
    url(r'^update_project_action/$', views.fix_project_action),  # 修改和新建动作
    url(r'^project_detail/$', views.project_detail),  # 项目详情页
    url(r'^cancel_action/$', views.cancel),  # 取消动作


    path('mysql_page/', views.mysql_manage),  # mysql列表页
    path('fix_mysql_page/', views.fix_mysql_page),  # 新建mysql配置
    path('fix_mysql_page_action/', views.fix_mysql_page_action),  # 新建mysql动作
    url(r'^delete_mysql_page/$', views.delete_mysql_page_action),  # 删除mysql
    path('mongodb_page/', views.mongodb_manage),  # mongodb列表页
    path('fix_mongodb_page/', views.fix_mongodb_page),  # 新建mongodb
    path('fix_mongodb_page_action/', views.fix_mongodb_page_action),  # 新建mongodb动作
    url(r'^delete_mongodb_page/$', views.delete_mongodb_page_action),  # 删除mongodb
    path('quest_test/', views.quest_test),  # 快速测试
    path('quest_test_action_ajax/', views.quest_test_action_ajax),  # ajax返回

    # 接口管理
    path('port_manage/', views.port_manage),  # 接口管理
    url(r'^delete_port/$', views.delete_port_action),  # 删除接口
    url(r'^update_port/$', views.fix_port),  # 修改和新建
    url(r'^update_port_action_ajax/$', views.fix_port_action),  # 修改和新建动作

    # 处理前置条件
    path('get_init_port_value/', views.get_init_port_value),  # 获取port_init_value
    path('get_preposition_value/', views.get_preposition_value),  # 获取前置条件接口返回

    # 测试用例
    path('test_case_manage/', views.test_case_manage),  # 项目管理
    url(r'^update_test_case/$', views.fix_test_case),  # 修改和新建
    url(r'^update_test_case_action_ajax/', views.fix_test_case_action),  # 修改和新建动作
    path('get_port_value/', views.get_port_value),  # 获取port_value

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

