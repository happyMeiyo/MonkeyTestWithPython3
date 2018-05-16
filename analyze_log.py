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
import fileinput

file_dir = os.path.join(os.getcwd(), 'log')

for log_path, dirs, log_files in os.walk(file_dir):
    for each_file in log_files:
        file_path = os.path.join(log_path, each_file)
        with fileinput.input(file_path) as log:
            for line in log:
                if re.findall("ANR", line) or re.findall("CRASH", line) or re.findall("Exception", line):
                    print(log.filename(), log.lineno(), line, end='')

