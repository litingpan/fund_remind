# -*- coding: utf-8 -*-
from debug_log import log_write
from data_type import Fund
import time
import datetime

FUND_MIN_VALUE = -100.0 #最小净值
FUND_MAX_VALUE = 100.0 #最大净值

# def isDigitalString(data):
#     for i in range(3, len(data)):
#         if data[i] == '--':
#             return False
#     return True
#
#
# def analyzeFund(datas):
#     worth_purchase = []
#     for i in range(len(datas)):
#         data = datas[i]
#         if isDigitalString(data):
#             f = float(data[11])
#             e = f - float(data[6])#一天前的值
#             d = f - float(data[7])#一周前的值
#             c = f - float(data[8])#一个月前的值
#             b = f - float(data[9])#一个季度前的值
#             a = f - float(data[10])#半年前的值
#             # if (float(data[3]) > 1.3 and float(data[4]) >1.5 and a > b and b < c and d < c and e < d ):
#             if (b > c and d > e):
#                 worth_purchase.append(data)
#     return worth_purchase

#基金卖出提醒
def fundRemind(cur_datas, usr_datas):
    # values = usr_datas.deepcopy()
    values = usr_datas.copy()
    for i in range(len(usr_datas)):
        code = usr_datas[i][0]
        flag = False
        for j in range(len(cur_datas)):
            if code == cur_datas[j][1]:
                values[i].append(cur_datas[j][3])
                flag = True
                break
        if not flag:
            values[i].append("--")
            log_write(code + "can't find!")
    #数据分析
    error = [] #出现错误
    loss = [] #损失
    sale = [] #可卖出
    for i in range(len(values)):
        if values[i][6] == "--":
            values[i].append("--")
            error.append(values[i])
            continue
        cur_value = float(values[i][6])
        pre_value = float(values[i][3])
        ratio = (cur_value - pre_value)/pre_value
        loss_ratio = float(values[i][4])
        sale_ratio = float(values[i][5])
        if ratio < loss_ratio:
            values[i].append(str(ratio))
            loss.append(values[i])
        if ratio > sale_ratio:
            values[i].append(str(ratio))
            sale.append(values[i])
    # ["基金代码", "基金名称", "买入日期", "买入净值", "预设跌幅", "预设涨幅", "当前涨跌幅度"]
    return error, loss, sale

def formatText(error, loss, sale):
    content = "有问题基金：\n"
    for i in range(len(error)):
        c = error[i][0] + " " + error[i][1] + " " + error[i][6] + "\n"
        content += c
    content += "需止损基金：\n"
    for i in range(len(loss)):
        c = loss[i][0] + " " + loss[i][1] + " " + loss[i][6] + "\n"
        content += c
    content += "可卖出基金：\n"
    for i in range(len(sale)):
        c = sale[i][0] + " " + sale[i][1] + " " + sale[i][6] + "\n"
        content += c
    return content




#历史 datas = [["基金代码", "日期", "单位净值", "累计净值"],...]

# 当前data = {'日期':'03-09', '代码':'000001', '简称':'华夏成长', '净值':'1.1450', '累计净值':'3.5560', '日增值':'0.0100',
#         '日增长':'0.8811', '周增':'2.1409', '月增':'9.4646', '季增':'3.0603', '半年增':'4.0782', '年增':'13.1117'}

def getFundIndex(funds, code):
    for i in range(len(funds)):
        if code == funds[i].code:
            return i
    return -1

#数据合并，删除错误数据，转换格式。历史数据和当前数据不能有重复
#begin_date: 保留这个日期之后的数据
#返回funds = [{code, 名称, {日期-净值,...}}...]
def deleteErrData(history_datas, cur_datas, begin_date):
    print("deleteErrData begin: " + time.strftime("%H:%M:%S"))
    funds = []
    #添加历史数据
    for i in range(len(history_datas)):
        if history_datas[i][2] == "--":
            pass
        else:
            ind = getFundIndex(funds, history_datas[i][0])
            if ind < 0:
                f = Fund(history_datas[i][0])
                f.setName("名称未知")#初始化基金名称
                f.addValue(history_datas[i][1], float(history_datas[i][2]))
                funds.append(f)
            else:
                funds[ind].addValue(history_datas[i][1], float(history_datas[i][2]))
    #添加当前数据
    for i in range(len(cur_datas)):
        ind = getFundIndex(funds, cur_datas[i][1])
        if ind < 0:
            #如果再加入，有5273只基金，没加入有3142只基金
            # f = Fund(cur_datas[i][1])
            # f.setName(cur_datas[i][2])
            # if cur_datas[i][3] != "--":
            #     f.addValue(cur_datas[i][0], float(cur_datas[i][3]))
            # funds.append(f)
            pass
        else:
            funds[ind].setName(cur_datas[i][2])
            if cur_datas[i][3] != "--":
                funds[ind].addValue(cur_datas[i][0], float(cur_datas[i][3]))

    #删除begin_date这个日期之前的数据
    date_thresh = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
    for i in range(len(funds)-1, -1, -1):
        for k in list(funds[i].values):
            date = datetime.datetime.strptime(k, "%Y-%m-%d")
            if date < date_thresh:
                funds[i].values.pop(k)
        #如果净值数据为空
        if funds[i].getValLen() == 0:
            funds.pop(i)

    print("deleteErrData finish: " + time.strftime("%H:%M:%S"))
    return funds

def minFundValue(fund):
    min = FUND_MAX_VALUE
    for v in fund.values.values():
        if v < min:
            min = v
    return min

def maxFundValue(fund):
    max = FUND_MIN_VALUE
    for v in fund.values.values():
        if v > max:
            max = v
    return max

#返回最新净值
def curFundValue(fund):
    cur_date = datetime.datetime.strptime("2017-03-10", "%Y-%m-%d")
    cur_value = 0.0001
    for k, v in fund.values.items():
        date = datetime.datetime.strptime(k, "%Y-%m-%d")
        if date > cur_date:
            cur_date = date
            cur_value = v
    return cur_value


#基金买入推荐, ratio为跌幅
def fundRecommand(funds, ratio):
    worth_purchase = []#[基金代码， 名称，幅度比例]
    for i in range(len(funds)):
        max = maxFundValue(funds[i])
        cur = curFundValue(funds[i])
        r = (max - cur)/max
        w = []
        if r > ratio:
            w.append(funds[i].code)
            w.append(funds[i].name)
            w.append(r)
            w.append(max)
            w.append(cur)
            worth_purchase.append(w)
            print(w[0] + " " + w[1] + ", ratio = " + str(w[2]) + ", max = " + str(w[3]) + ", cur = " + str(w[4]))
    return worth_purchase










































