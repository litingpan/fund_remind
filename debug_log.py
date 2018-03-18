# -*- coding: utf-8 -*-
import time
file_name = "log/" + time.strftime("%Y-%m") + "_log.txt"

def log_write(str):
    log = open(file_name, 'a')
    log.write(time.strftime("%H:%M:%S") + ': '+ str + '\n')
    log.close()