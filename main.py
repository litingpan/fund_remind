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





def main():
    log_write("start------------------------->")
    print(time.strftime("%H:%M:%S") + "：start...")

    #基金推荐
    # history_datas = data_base.readHistoryDatas()
    # tmp = data_base.getCurrentData()
    # data_base.saveCurrentData(tmp)
    # cur_datas = data_base.readCurrentData()
    # funds = analysis.deleteErrData(history_datas, cur_datas, "2017-09-01")
    # analysis.fundRecommand(funds, 0.5)

    # 基金提醒
    # time_thresh = datetime.datetime.strptime("22:00:00", "%H:%M:%S")
    # while True:
    #     cur_time = datetime.datetime.strptime(time.strftime("%H:%M:%S"), "%H:%M:%S")
    #     if cur_time > time_thresh:
    #         cur_datas = data_base.getCurrentData()
    #         # cur_datas = data_base.readCurrentData()
    #         data_base.saveCurrentData(cur_datas)
    #         usr_datas = data_base.readUsrData()
    #         err, loss, sale = analysis.fundRemind(cur_datas, usr_datas)
    #         content = analysis.formatText(err, loss, sale)
    #         print(content)
    #         sendEmail(content)
    #         break
    #     else:
    #         time.sleep(60)
    #         pass

    mysql_operate.insertCurrentData()
    mysql_operate.insertHistoryWorth()




    log_write("---------------------------->end")
    print(time.strftime("%H:%M:%S") + "：finish")


if __name__ == "__main__":
    main()