# -*- coding: utf-8 -*-
from debug_log import log_write


def isDigitalString(data):
    for i in range(3, len(data)):
        if data[i] == '--':
            return False
    return True


def analyzeFund(datas):
    worth_purchase = []
    for i in range(len(datas)):
        data = datas[i]
        if isDigitalString(data):
            f = float(data[11])
            e = f - float(data[6])#一天前的值
            d = f - float(data[7])#一周前的值
            c = f - float(data[8])#一个月前的值
            b = f - float(data[9])#一个季度前的值
            a = f - float(data[10])#半年前的值
            # if (float(data[3]) > 1.3 and float(data[4]) >1.5 and a > b and b < c and d < c and e < d ):
            if (b > c and d > e):
                worth_purchase.append(data)
    return worth_purchase

# #获取当前数据的单位净值
# def extractCurDataValue(datas):



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








# def fundRecommand(history_datas, cur_datas):
#     datas = []


