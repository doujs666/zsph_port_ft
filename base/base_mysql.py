# -*- coding:utf-8 -*-
import pymysql.cursors
import base.settings as settings


def execute(sql, params=None, db=settings.TEST_DEFAULT_DB, is_fetchone=True):
    # Connect to the database
    connection = pymysql.connect(host=settings.TEST_MYSQL_CONFIG['host'],
                                 port=settings.TEST_MYSQL_CONFIG['port'],
                                 user=settings.TEST_MYSQL_CONFIG['user'],
                                 password=settings.TEST_MYSQL_CONFIG['password'],
                                 db=db,
                                 autocommit=True,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    # logger.info('Executing SQL：' + str(sql) + ',params:' + str(params))
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql, params)
            if is_fetchone:
                return cursor.fetchone()
            else:
                return cursor.fetchall()
    except:
        connection.rollback()
    finally:
        connection.close()


def local_execute(sql, params=None, db=settings.DJANGO_DEFAULT_DB, is_fetchone=True):
    # 链接django数据库
    connection = pymysql.connect(host=settings.DJANGO_MYSQL_CONFIG['host'],
                                 port=settings.DJANGO_MYSQL_CONFIG['port'],
                                 user=settings.DJANGO_MYSQL_CONFIG['user'],
                                 password=settings.DJANGO_MYSQL_CONFIG['password'],
                                 db=db,
                                 autocommit=True,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql, params)
            if is_fetchone:
                return cursor.fetchone()
            else:
                return cursor.fetchall()
    except:
        connection.rollback()
    finally:
        connection.close()
