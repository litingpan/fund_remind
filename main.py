# -*- coding: utf-8 -*-
import data_base
import analysis
import time
from debug_log import log_write
import datetime
from data_type import Fund


# log_write("start------------------------->")

# datas = data_base.getCurrentData()
# data_base.saveCurrentData(datas)
# data_base.saveHistoryDatas(datas)

# data_base.getHistoryData('002145')

# data_base.readHistoryDatas()
# data_base.readCurrentData()

#基金推荐
# datas = data_base.getCurrentData()
# usr_datas = data_base.readUsrData()
# analysis.fundRemind(datas, usr_datas)





def main():
    log_write("start------------------------->")


    # history_datas = data_base.readHistoryDatas()
    # cur_datas = data_base.readCurrentData()
    # funds = analysis.deleteErrData(history_datas, cur_datas, "2017-09-01")
    # data_base.saveFundData(funds)
    funds = data_base.readFundData()
    analysis.fundRecommand(funds, 0.5)

    # funds = []
    # f = Fund("00001")
    # f.addName("华夏")
    # f.addValue("2017-03-08", 1.34)
    # f.addValue("2017-03-07", 1.0)
    # f.addValue("2017-03-06", 1.1)
    # funds.append(f)
    # analysis.fundRecommand(funds, 0.95)


    # begin_date = "2017-04-13"
    # date_thresh = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
    # for i in range(len(funds)):
    #     kv = funds[i].values
    #     for k in list(kv):
    #         date = datetime.datetime.strptime(k, "%Y-%m-%d")
    #         if date < date_thresh:
    #             funds[i].values.pop(k)

    print("sdfs")

log_write("---------------------------->end")



# print("finish")


if __name__ == "__main__":
    main()