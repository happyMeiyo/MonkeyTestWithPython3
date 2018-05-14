#!/usr/bin/env python
# encoding: utf-8

"""
-------------------------------------------------
   File Name：     analyze_result
   Description :
   Author :        Meiyo
   date：          2018/5/14 19:48
-------------------------------------------------
   Change Activity:
                   2018/5/14:
------------------------------------------------- 
"""
__author__ = 'Meiyo'

import re
import os

file_dir = os.getcwd() + '\log'

for log_path, dirs, log_files in os.walk(file_dir):
    for each_file in log_files:
        with open(log_path + '\\' + each_file, encoding="utf-8") as log:
            lines = log.readlines()
            for line in lines:
                if re.findall("ANR", line):
                    print(log_path + each_file + "存在anr错误:" + line)
                if re.findall("CRASH", line):
                    print(log_path + each_file + "存在crash错误:" + line)
                if re.findall("EXCEPTION", line):
                    print(log_path + each_file + "存在crash错误:" + line)

