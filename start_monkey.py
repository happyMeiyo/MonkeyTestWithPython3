#!/usr/bin/env python
# encoding: utf-8

"""
-------------------------------------------------
   File Name：     monkey_test
   Description :
   Author :        Meiyo
   date：          2018/5/12 18:07
-------------------------------------------------
   Change Activity:
                   2018/5/12:
------------------------------------------------- 
"""
__author__ = 'Meiyo'


import sys
from monkey_util.monkey import start_monkey

print(sys.argv)

len = len(sys.argv)

file_name = sys.argv[1] if len > 1 else 'command_config.yml'
app_name = sys.argv[2] if len > 2 else 'Caibao_dev'

start_monkey(file_name, app_name)
