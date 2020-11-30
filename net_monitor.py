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


while True:
    try:
        # ping 百度网址，查看状态码，如果
        state_code = os.system('ping -c 2 www.baidu.com')
        if state_code:
            playsound('duanwangle.mp3')
    except Exception as e:
        playsound('jiaobenchucuo.mp3')
