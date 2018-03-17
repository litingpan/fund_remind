# -*- coding: utf-8 -*-
import data_base
import analysis
import time
from debug_log import log_write


log_write("start------------------------->")

# datas = data_base.getCurrentData()
# data_base.saveCurrentData(datas)
# data_base.saveHistoryDatas(datas)

# data_base.getHistoryData('002145')

data_base.readHistoryDatas()
data_base.readCurrentData()
log_write("---------------------------->end")



print("finish")