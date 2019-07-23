from sign.models import project_message
from sign.models import host_page
from sign.models import mysql_page
from sign.models import mongodb_page
from sign.models import port_manage
import json
from django.core import serializers


def navigation_bar(request):
    project_list = project_message.objects.all()
    new_project_list = json.loads(serializers.serialize('json', project_list, ensure_ascii=False))
    host_list = host_page.objects.all()
    mysql_list = mysql_page.objects.all()
    mongodb_list = mongodb_page.objects.all()
    port_list = port_manage.objects.all()
    new_port_list = json.loads(serializers.serialize('json', port_list, ensure_ascii=False))
    db_select_assert_list = ['assertEqual','assertNotEqual']
    db_assert_type_list = ['data', 'mysql']

    return {
        "project_list": project_list,
        "new_project_list": new_project_list,
        "host_list": host_list,
        "mysql_list": mysql_list,
        "mongodb_list": mongodb_list,
        "port_list": port_list,
        "new_port_list": new_port_list,
        "db_select_assert_list": db_select_assert_list,
        "db_assert_type_list": db_assert_type_list,
    }
