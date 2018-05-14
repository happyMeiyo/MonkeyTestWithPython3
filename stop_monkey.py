#!/usr/bin/env python
# encoding: utf-8

"""
-------------------------------------------------
   File Name：     stop_monkey
   Description :
   Author :        Meiyo
   date：          2018/5/14 19:46
-------------------------------------------------
   Change Activity:
                   2018/5/14:
------------------------------------------------- 
"""
__author__ = 'Meiyo'

from monkey_util.monkey import stop_moneky
from monkey_util.device_manage import get_devices

devices = get_devices()
if not devices:
    print("未获取到设备")
    exit(0)

for each in devices:
    stop_moneky(each)

