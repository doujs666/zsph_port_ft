# Create your views here.
# Django的视图文件，控制向前端页面显示的内容
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign.models import Event


def login(request):
    return render(request, "login.html")


# 登录
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            response = HttpResponseRedirect('/index/')
            # response.set_cookie('user', username, 3200)
            # request.session['user'] = username
            return response
        else:
            return render(request, 'login.html', {'error': 'username or password error'})


# 首页
@login_required
def index(request):
    username = request.COOKIES.get('user', '')
    # username = request.session.get('user', '')
    return render(request, 'index.html', {'user': username})


# 发布会系统
@login_required
def event_message(request):
    event_list = Event.objects.all()
    username = request.session.get('url', '')
    return render(request, 'event_manage.html', {'user': username, 'events': event_list})


# 测试页面
def test(request):
    return render(request, 'test.html')
