# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

def getCurFundData():
    datas = []
    # data = {'日期':'03-09', '代码':'000001', '简称':'华夏成长', '净值':'1.1450', '累计净值':'3.5560', '日增值':'0.0100',
    #         '日增长':'0.8811', '周增':'2.1409', '月增':'9.4646', '季增':'3.0603', '半年增':'4.0782', '年增':'13.1117'}

    url = "http://data.chinafund.cn/"
    r = requests.get(url)
    if r.encoding == 'ISO-8859-1':
        encodings = requests.utils.get_encodings_from_content(r.text)
        if encodings:
            encoding = encodings[0]
        else:
            encoding = r.apparent_encoding
        html_doc = r.content.decode(encoding, 'replace')

    soup = BeautifulSoup(html_doc, 'lxml')
    tr = soup.find_all('tr', attrs={"onmouseout": "this.bgColor='#f8ffff';"})
    for i in range(len(tr)):
        tds = tr[i].find_all('td')
        data = [''] * 13  # 初始化data
        data[0] = tds[1].get_text()#日期
        data[1] = tds[2].get_text()#代码
        data[2] = tds[3].get_text()#简称
        data[3] = tds[5].get_text()#净值
        data[4] = tds[6].get_text()#累计净值
        data[5] = tds[7].get_text()#日增值
        data[6] = tds[8].get_text()#日增长
        data[7] = tds[9].get_text()#周增
        data[8] = tds[10].get_text()#月增
        data[9] = tds[11].get_text()#季增
        data[10] = tds[12].get_text()#半年增
        data[11] = tds[13].get_text()#年增
        tmp = tds[15].find_all('a')
        data[12] = tmp[1].get('href')#网址链接
        datas.append(data)
    for i in range(len(tr)):
        print(datas[i])
    return datas


def getHistoryFundData(code):
    datas = []
    url = "http://info.chinafund.cn/fund/" + code + "/jjjz/"
    r = requests.get(url)
    if r.encoding == 'ISO-8859-1':
        encodings = requests.utils.get_encodings_from_content(r.text)
        if encodings:
            encoding = encodings[0]
        else:
            encoding = r.apparent_encoding
        html_doc = r.content.decode(encoding, 'replace')

    soup = BeautifulSoup(html_doc, 'lxml')
    trs = soup.find_all(id='lsjz')
    tr = trs[0].find_all('tr')
    for i in range(1, len(tr)):
        tds = tr[i].find_all('td')
        data = [''] * 3  # 初始化data
        data[0] = tds[0].get_text()#日期
        data[1] = tds[1].get_text()#单位净值
        data[2] = tds[2].get_text()#累计净值
        datas.append(data)
    for i in range(len(tr)-1):
        print(datas[i])
    return datas


