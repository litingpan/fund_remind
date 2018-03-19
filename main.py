# -*- coding: utf-8 -*-
import data_base
import analysis
import time
from debug_log import log_write
from email_remind import sendEmail
import datetime
from data_type import Fund


# log_write("start------------------------->")

# datas = data_base.getCurrentData()
# data_base.saveCurrentData(datas)
# data_base.saveHistoryDatas(datas)

# data_base.getHistoryData('002145')

# data_base.readHistoryDatas()
# data_base.readCurrentData()



# funds = []
# f = Fund("00001")
# f.addName("华夏")
# f.addValue("2017-03-08", 1.34)
# f.addValue("2017-03-07", 1.0)
# f.addValue("2017-03-06", 1.1)
# funds.append(f)
# analysis.fundRecommand(funds, 0.95)



def main():
    log_write("start------------------------->")
    print("start...")

    #基金推荐
    # history_datas = data_base.readHistoryDatas()
    # cur_datas = data_base.readCurrentData()
    # funds = analysis.deleteErrData(history_datas, cur_datas, "2017-09-01")
    # data_base.saveFundData(funds)
    # funds = data_base.readFundData()
    # analysis.fundRecommand(funds, 0.5)

    # 基金提醒
    time_thresh = datetime.datetime.strptime("22:00:00", "%H:%M:%S")
    while True:
        cur_time = datetime.datetime.strptime(time.strftime("%H:%M:%S"), "%H:%M:%S")
        if cur_time > time_thresh:
            cur_datas = data_base.getCurrentData()
            # cur_datas = data_base.readCurrentData()
            usr_datas = data_base.readUsrData()
            err, loss, sale = analysis.fundRemind(cur_datas, usr_datas)
            content = analysis.formatText(err, loss, sale)
            print(content)
            sendEmail(content)
            break
        else:
            time.sleep(60)
            pass





    log_write("---------------------------->end")
    print("finish")


if __name__ == "__main__":
    main()