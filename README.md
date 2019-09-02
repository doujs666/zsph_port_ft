# 接口测试平台从开始到放弃
# python3.7 Django 2.1.7框架
体验地址：http://106.12.177.228:8000/login  请体验用户不要删除已有数据<br>
账号：test2 密码：test2

## 系统声明：
---
1.本系统采用Django REST framework编写接口，前端页面采用bootstrap3<br>
2.初步学习web开发，接口统一采用基于方法的方式编写，后续引入权限系统，并修改成基于类的方法<br></br>
3.后期改为估计改为容易上手的vue+elementUI

## 使用方法：
---
### 1.安装Python3环境（未在Python2上运行后，不知道有没有问题）<br>
### 2.下载代码到本地并解压<br>
### 3.cmd到根目录下安装相关依赖包<br>
```bash
pip install -r requirements.txt<br>
pip install https://github.com/darklow/django-suit/tarball/v2
```
### 4.安装mysql数据库
```python
DATABASES = {
    'default': {
        static
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE':static,     # 数据库类型，mysql
        'NAME':'api_test',            #  database名
        'USER':'root',               # 登录用户
        'PASSWORD':'123456',        #  登录用户名
        'HOST':'127.0.0.1',        # 数据库地址
        'PORT':'3306'              # 数据库端口
    }
}
```
### 5.cmd到根目录下，让 Django 知道我们在我们的模型有一些变更<br>
```bash
python manage.py makemigrations
```
### 6.创造或修改表结构<br>
```bash
python manage.py migrate 
```
### 7.创建超级用户，用于登录后台管理<br>
```bash
python manage.py createsuperuser
```
### 8.安装VUE环境，下载node.js并配置环境，下载npm包管理器<br>
### 9.cmd进入frontend目录下，运行npm install安装相关依赖包<br>
### 10.打包<br>
```bash
npm run build
```
### 11.运行启动django服务<br>
```bash
python manage.py runserver 0.0.0.0:8000
```
### 12.现在就可以访问 http://106.12.177.228:8000/login 进行登录， http://106.12.177.228:8000/admin 为后台管理平台<br>

