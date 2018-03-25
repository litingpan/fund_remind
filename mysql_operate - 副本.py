# -*- coding: utf-8 -*-
import pymysql.cursors
from data_base import readCurrentData

# class config(object):
#     host = ''
#     port = 0
#     user = ''
#     password = ''
#     db = ''
#     # charset = ''
#
#     def __init__(self, host, port, user, password, db, charset):
#         self.host = host
#         self.port = port
#         self.user = user
#         self.password = password
#         self.db = db
#         # self.charset = charset



# class db_connection(object):
#     __db = ''
#     __owner = ''
#
#     def __init__(self):
#         pass
#
#     def connection(self, config):
#         if self.__db == '':
#             self.__db = pymysql.connect(host=config.host, port=config.port, user=config.user, password=config.password, db=config.db, \
#                                         charset=config.charset, cursorclass=pymysql.cursors.DictCursor)
#         return self.__db
#
#     @staticmethod
#     def instance(self):
#         if self.__owner == '':
#             self.__owner = db_connection()
#         return self.__owner

# class db_connection(object):
#     __db = ''
#
#     def __init__(self):
#         self.__db = ''
#         pass
#
#     def connection(self, config):
#         self.__db = pymysql.connect(host=config.host, port=config.port, user=config.user, password=config.password, db=config.db, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
#         return self.__db



# def insertData():
# 连接MySQL数据库
connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='', db='fund_db', charset='utf-8', cursorclass=pymysql.cursors.DictCursor)
# cfg = config('127.0.0.1', 3306, 'root', '', 'fund_db', 'utf-8')
# connect = db_connection.connection(cfg)

# 通过cursor创建游标
cursor = connection.cursor()
# 创建sql 语句，并执行
datas = readCurrentData()
sql = "INSERT INTO `funds` (`id`, `code`, `name`) VALUES ('huzhiheng3@itest.info', '123456')"
cursor.execute(sql)
# 提交SQL
connection.commit()

# db_connection.instance()
# dd = db_connection




