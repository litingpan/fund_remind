# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time
from debug_log import log_write

#网站交互
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains  # 引入ActionChains鼠标操作类
from selenium.webdriver.common.keys import Keys  # 引入keys类操作
import os
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException

abspath = os.path.abspath(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

def getCurrentData():
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
    # for i in range(len(tr)):
    #     print(datas[i])
    return datas

def saveCurrentData(datas):
    if len(datas) == 0:
        return
    file_name = datas[0][0]
    f = open("data2/"+ file_name + ".txt", 'w')
    for i in range(len(datas)):
        for j in range(len(datas[i])):
            f.write(datas[i][j] + ' ')
        f.write('\n')



def getHistoryData(code):
    datas = []
    url = "http://info.chinafund.cn/fund/" + code + "/jjjz/"

    # r = requests.get(url)
    # #如果网址重定向
    # if r.url != url or r.status_code != 200:
    #     log_write("open " + url + " fail, status_code = " + str(r.status_code))
    #     print(r.status_code)
    #     return datas
    # if r.encoding == 'ISO-8859-1':
    #     encodings = requests.utils.get_encodings_from_content(r.text)
    #     if encodings:
    #         encoding = encodings[0]
    #     else:
    #         encoding = r.apparent_encoding
    #     html_doc = r.content.decode(encoding, 'replace')

    #网站交互
    # browser = webdriver.Chrome(abspath)
    browser = webdriver.Chrome(abspath, chrome_options=chrome_options)
    browser.implicitly_wait(30)
    try:
        browser.get(url)
    except TimeoutException:
        print(code + ": Time out")
        log_write(code + ": Time out")
        return datas
    error = False
    if browser.current_url != url:
        error = True
        print(url + "url redirection")
    else:
        try:
            date = browser.find_element_by_id("startdate")
            date.clear()
            date.send_keys("2017-01-01")
            browser.find_element_by_id("Button1").click()
            html_doc = browser.page_source
        except NoSuchElementException:
            error = True
            print("No element")
            log_write(code + ": No element")
    browser.quit()
    if error:
        return datas

    soup = BeautifulSoup(html_doc, 'lxml')
    trs = soup.find_all(id='lsjz')
    if len(trs) == 0:
        return datas
    else:
        tr = trs[0].find_all('tr')
        for i in range(1, len(tr)):
            tds = tr[i].find_all('td')
            data = [''] * 3  # 初始化data
            data[0] = tds[0].get_text()#日期
            data[1] = tds[1].get_text()#单位净值
            data[2] = tds[2].get_text()#累计净值
            datas.append(data)
        # for i in range(len(tr)-1):
        #     print(datas[i])
        return datas

def saveHistoryDatas(cur_datas):
    for i in range(2495, len(cur_datas)):
        code = cur_datas[i][1]
        datas = getHistoryData(code)
        if len(datas) == 0:
            log_write('error code: ' + code)
        else:
            f = open("data/" + str(i+1) + ".txt", 'a')
            for j in range(len(datas)):
                f.write(code + ' ')#基金代码
                f.write(datas[j][0] + ' ')#日期
                f.write(datas[j][1] + ' ')#单位净值
                f.write(datas[j][2] + '\n')#累计净值
            f.close()
        print(time.strftime("%H:%M:%S") + ': ' + str(i+1))
        time.sleep(0.1)