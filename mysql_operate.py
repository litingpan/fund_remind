# -*- coding: utf-8 -*-
import pymysql.cursors
import data_base
import time
import data_base
from debug_log import log_write



def insertCurrentData():
    # 连接MySQL数据库
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='', db='fund_db', charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    # 通过cursor创建游标
    cursor = connection.cursor()

    funds = data_base.getCurrentData()
    for i in range(len(funds)):
        code = funds[i][1]
        name = funds[i][2]
        day = time.strftime("%Y-") + funds[i][0]
        worth = 0
        if funds[i][5] == "--":
            pass
        else:
            worth = float(funds[i][5])
        total_worth = 0
        if funds[i][6] == "--":
            pass
        else:
            total_worth = float(funds[i][6])

        #funds表插入数据
        sql = "SELECT * FROM funds WHERE code='{}'".format(code)
        cursor.execute(sql)
        r = cursor.fetchone()
        if r:
            pass
        else:
            # 创建sql 语句，并执行
            sql = "INSERT IGNORE INTO `funds` (`code`, `name`, `create_time`) VALUES ('{}', '{}', '{}')".format(code, name, time.strftime("%Y-%m-%d %H:%M:%S"))
            cursor.execute(sql)
            # 提交SQL
            connection.commit()
            print("insert new fund:" + code)
            log_write("insert new fund:" + code)

        # funds_info表插入数据
        # 创建sql 语句，并执行
        sql = "REPLACE INTO `funds_info` ( `code`, `day`, `worth`, `total_worth`, `create_time`) VALUES ('{}','{}', {}, {}, '{}')".format(
            code, day, worth, total_worth, time.strftime("%Y-%m-%d %H:%M:%S"))
        cursor.execute(sql)
        # 提交SQL
        connection.commit()


    # 关闭数据连接
    connection.close()


def insertHistoryWorth():
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='', db='fund_db', charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()

    #查询总共有多少只基金
    sql = "SELECT code FROM funds"
    cursor.execute(sql)
    codes = cursor.fetchall()
    for c in codes:
        code = c['code']
        datas = data_base.getHistoryData(code)
        if len(datas) == 0:
            log_write('error code: ' + code)
        else:
            for j in range(len(datas)):
                day = datas[j][0]#日期
                worth = float(datas[j][1])#单位净值
                total_worth = float(datas[j][2])#累计净值
                # 查询判断是否有存在
                sql = "SELECT * FROM funds_info WHERE code='{}' AND day='{}'".format(code, day)
                cursor.execute(sql)
                # 插入数据
                r = cursor.fetchone()
                if r:
                    pass
                else:
                    # 创建sql 语句，并执行
                    sql = "INSERT IGNORE INTO `funds_info` ( `code`, `day`, `worth`, `total_worth`, `create_time`) VALUES ('{}','{}', {}, {}, '{}')".format(
                        code, day, worth, total_worth, time.strftime("%Y-%m-%d %H:%M:%S"))
                    cursor.execute(sql)
                    # 提交SQL
                    connection.commit()
        print(time.strftime("%H:%M:%S") + ': ' + code)
        time.sleep(0.1)
    # 关闭数据连接
    connection.close()







