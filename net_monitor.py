# -*- coding:utf-8 -*-
"""
 @Time: 2020/11/30 下午3:25
 @Author: LiuHe
 @File: net_monitor.py
 @Describe: 网络检测
"""
import os
from playsound import playsound
import time
import logging
import traceback

# 配置日志信息
logging.basicConfig(filename='net_monitor.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# 设置重连标志位 判断网络是否已重连
reconnect_flag = False

while True:
    try:
        # ping 百度网址，查看状态码
        state_code = os.system('ping -c 2 www.baidu.com')
        if state_code:
            # 如果断网，则进行语音提示，进行重连，一分钟后重新进行检测
            playsound('duanwangle.mp3')
            # 尝试连接乌班图，重启机器，因为乌班图没有netkeeper，必须重启进入windows
            # 设置连接响应时间为30秒
            result_code = os.system('ssh -O ConnectTimeout=30 liuh@192.168.1.120 \'sudo reboot\'')
            if result_code:
                # 连接失败
                playsound('connect_except.mp3')
            else:
                # 将重连标记为设为True
                reconnect_flag = True
            time.sleep(60)
        else:
            if reconnect_flag:
                playsound('reconnect.mp3')
        # 每隔十秒检测一次
        time.sleep(10)
    except Exception as e:
        playsound('shell_except.mp3')
        # 将错误写入日志
        logging.debug(traceback.format_exc())
