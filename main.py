# -*- coding: utf-8 -*-
import data_base
import analysis

datas = data_base.getFundData()
worth = analysis.analyzeFund(datas)
print("finish")