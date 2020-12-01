# -*- coding:utf-8 -*-
"""
 @Time: 2020/11/30 下午4:17
 @Author: LiuHe
 @File: test.py
 @Describe: 测试文件 用来测试每个单元的有效性
"""
import os
import time

# 测试ssh响应时间
# start_time = time.time()
# state_code = os.system('ssh -o ConnectTimeout=30 liuh@192.168.1.120 \'sudo reboot\'')
# print(state_code)
# end_time = time.time()
# print(end_time - start_time)


# 测试远程控制windows重启
# os.system('net rpc shutdown -r -f -I 192.168.1.120 -U administrator%123')