# -*- coding: utf-8 -*-
import data_base
import analysis
import time
from debug_log import log_write


log_write("start------------------------->")

# datas = data_base.getCurrentData()
# data_base.saveCurrentData(datas)
# data_base.saveHistoryDatas(datas)

data_base.getHistoryData('000001')


log_write("---------------------------->end")





print("finish")