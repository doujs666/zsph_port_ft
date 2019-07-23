import time
# 配置文件

# Mysql配置
TEST_MYSQL_CONFIG = {'host': 'test-zsph.mysql.rds.aliyuncs.com', 'port': 3306, 'user': 'credit_test',
                     'password': '1XPFrpm^D!8#lxbWa3'}
TEST_DEFAULT_DB = 'credit_test'

# django数据库配置
DJANGO_MYSQL_CONFIG = {'host': '127.0.0.1', 'port': 3306, 'user': 'root',
                       'password': '12345678'}
DJANGO_DEFAULT_DB = 'test'

# 请求HEADERS配置
API_HEADERS = {'Cache-Control': "no-cache", "Content-Type": "application/json"}


REPORT_FILE_NAME = './wer/' + time.strftime("%Y%m%d%H%M%S") + '_result.html'