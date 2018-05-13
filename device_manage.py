#!/usr/bin/env python
# encoding: utf-8

"""
-------------------------------------------------
   File Name：     device_manage
   Description :
   Author :        Meiyo
   date：          2018/5/7 17:55
-------------------------------------------------
   Change Activity:
                   2018/5/7: Create file
------------------------------------------------- 
"""
__author__ = 'Meiyo'

import os


# 执行adb命令
def call_adb(command):
    command_text = 'adb %s' % command
    print(command_text)

    with os.popen(command_text, "r") as result:
        command_result = result.read()

    return command_result


# 获取连接设备
def get_devices():
    command_result = call_adb("devices")
    devices = command_result.partition('\n')[2].replace('\n', '').split('\tdevice')
    return [device for device in devices if len(device) > 2]


def get_monkey_pid():
    command_result = call_adb("shell \"ps | grep monkey\"")
    monkey_pid = ''
    if command_result:
        content = command_result.partition(' ')[2]
        monkey_pid = content.strip(' ').partition(' ')[0]

    return monkey_pid


def stop_monkey_pid(monkey_pid):
    command_result = call_adb("shell kill -9 " + monkey_pid)
    print(command_result)


if __name__ == '__main__':
    devices = get_devices()
    for info in devices:
        print(info)


