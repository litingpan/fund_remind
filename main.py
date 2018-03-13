# -*- coding: utf-8 -*-
import data_base
import analysis

# datas = data_base.getCurFundData()
# worth = analysis.analyzeFund(datas)

code = "000001"
data_base.getHistoryFundData(code)
print("finish")