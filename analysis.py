# -*- coding: utf-8 -*-


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