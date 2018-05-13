#!/usr/bin/env python
# encoding: utf-8

"""
-------------------------------------------------
   File Name：     monkey_test
   Description :
   Author :        Meiyo
   date：          2018/5/7 17:56
-------------------------------------------------
   Change Activity:
                   2018/5/7:
------------------------------------------------- 
"""
__author__ = 'Meiyo'

from device_manage import get_devices, get_monkey_pid, stop_monkey_pid
import yaml
import io
import os
import logging

def check_format(file_path, content):
    """ check the format if valid
    """
    if not content:
        # testcase file content is empty
        err_msg = u"Testcase file content is empty: {}".format(file_path)
        logging.error(err_msg)
        raise FileNotFoundError

    elif not isinstance(content, (list, dict)):
        # testcase file content does not match testcase format
        err_msg = u" file content format invalid: {}".format(file_path)
        logging.error(err_msg)
        raise Exception(err_msg)


def load_yaml_file(yaml_file):
    """ load yaml file and check file content format
    """
    with io.open(yaml_file, 'r', encoding='utf-8') as stream:
        yaml_content = yaml.load(stream)
        check_format(yaml_file, yaml_content)
        return yaml_content


def get_monkey_command(file_name, app):
    """ get the command for monkey
    """
    monkey_command = 'monkey -p '

    file_path = os.path.join(os.getcwd(), file_name)
    file_content = load_yaml_file(file_path)

    try:
        command_config = file_content.get(app)
        monkey_command += command_config.get('packageName', 'com.***')
        monkey_command = monkey_command + ' --throttle ' + str(command_config.get('throttle', 500))
        monkey_command = monkey_command + ' -s ' + str(command_config.get('seed', 2000))
        monkey_command = monkey_command + ' --ignore-timeouts --ignore-crashes  --monitor-native-crashes -v -v -v '
        monkey_command = monkey_command + str(command_config.get('count', 10000))
        # the path of log file
        monkey_command = monkey_command + ' > ' + '/sdcard/monkeylog.txt'

        return monkey_command
    except Exception as ex:
        print('获取monkey参数失败: %s', ex)


def start_monkey(file_name, app_name):
    """ start running monkey
    """
    devices = get_devices()
    if not devices:
        print("未获取到设备")
        exit(0)

    command = get_monkey_command(file_name, app_name)
    command = 'adb -s ' + ''.join(devices) + ' shell ' + "\"" + command + "\""
    logging.info(command)
    print(command)

    os.popen(command)


def stop_moneky(device_id):
    """ stop running monkey
    """
    monkey_pid = get_monkey_pid()
    if not monkey_pid:
        stop_monkey_pid(monkey_pid)
        logging.info("关闭" + device_id + "monkey")
    else:
        logging.info("没有正在执行的monkey")


if __name__ == '__main__':
    # start_monkey()
    stop_moneky('48decad2')
