# -*- coding:utf-8 -*-
"""
 @Time: 2020/11/30 下午4:17
 @Author: LiuHe
 @File: test.py
 @Describe: 测试文件 用来测试每个单元的有效性
"""
import os
import time
import traceback
import logging

logging.basicConfig(filename='net_monitor.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# 测试ssh响应时间
# start_time = time.time()
# state_code = os.system('ssh -o ConnectTimeout=30 root@192.168.1.x\'sudo reboot\'')
# print(state_code)
# end_time = time.time()
# print(end_time - start_time)


# 测试远程控制windows重启
# os.system('net rpc shutdown -r -f -I 192.168.1.x -U administrator%123')

# 测试日志问题
# try:
#     raise Exception('异常')
# except Exception as e:
#     logging.debug(traceback.format_exc())
