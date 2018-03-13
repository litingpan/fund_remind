# -*- coding: utf-8 -*-
import data_base
import analysis

datas = data_base.getCurFundData()
worth = analysis.analyzeFund(datas)
print("finish")