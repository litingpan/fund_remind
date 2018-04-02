# -*- coding: utf-8 -*-
import data_base
import analysis
import time
from debug_log import log_write
from email_remind import sendEmail
import datetime
from data_type import Fund
import mysql_operate

# log_write("start------------------------->")

# datas = data_base.getCurrentData()
# data_base.saveCurrentData(datas)
# data_base.saveHistoryDatas(datas)

# data_base.getHistoryData('002145')

# data_base.readHistoryDatas()
# data_base.readCurrentData()

# 基金推荐
# history_datas = data_base.readHistoryDatas()
# tmp = data_base.getCurrentData()
# data_base.saveCurrentData(tmp)
# cur_datas = data_base.readCurrentData()
# funds = analysis.deleteErrData(history_datas, cur_datas, "2017-09-01")
# analysis.fundRecommand(funds, 0.5)

#保存到数据库
# mysql_operate.insertCurrentData()
# mysql_operate.insertHistoryWorth()

#推荐基金
# refe_datas = data_base.readReferData()
# cur_datas = data_base.getCurrentData()
# recommend = analysis.fundRecommand2(refe_datas, cur_datas, 0.05)
# content = analysis.formatText(recommend)
# print(content)


def main():
    log_write("start------------------------->")
    print(time.strftime("%H:%M:%S") + "：start...")

    time_thresh = datetime.datetime.strptime("22:00:00", "%H:%M:%S")
    while True:
        cur_time = datetime.datetime.strptime(time.strftime("%H:%M:%S"), "%H:%M:%S")
        if cur_time > time_thresh:
            #基金提醒
            cur_datas = data_base.getCurrentData()
            # cur_datas = data_base.readCurrentData()
            data_base.saveCurrentData(cur_datas)
            usr_datas = data_base.readUsrData()
            err, loss, sale = analysis.fundRemind(cur_datas, usr_datas)
            content = analysis.formatText(err, loss, sale)

            #基金推荐
            refe_datas = data_base.readReferData()
            recommend = analysis.fundRecommand2(refe_datas, cur_datas, 0.6)
            content += analysis.formatText2(recommend)
            print(content)
            sendEmail(content)

            #保存到数据库
            mysql_operate.insertCurrentData()
            break
        else:
            time.sleep(60)
            pass






    log_write("---------------------------->end")
    print(time.strftime("%H:%M:%S") + "：finish")


if __name__ == "__main__":
    main()