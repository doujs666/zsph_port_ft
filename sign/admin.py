from django.contrib import admin

# Register your models here.
# 映射models中的数据到Django自带的admin后台

from sign.models import Event, Guest


class EventAdmin(admin.ModelAdmin):
    # 用EventAdmin选项注册Event模块
    list_display = ['id', 'name', 'status', 'address', 'start_time']
    search_fields = ['name']  # 搜索栏
    list_filter = ['status']  # 过滤栏


class GuestAdmin(admin.ModelAdmin):
    list_display = ['real_name', 'phone', 'email', 'sign', 'create_time', 'event']


admin.site.register(Event, EventAdmin)
admin.site.register(Guest, GuestAdmin)
