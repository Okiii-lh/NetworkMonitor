
"""
 @Time: 2021/04/08 下午4:17
 @Author: LiuHe
 @File: main.py
 @Describe: 检测网络是否联通 不连通启动 NetKeeper 进行联网
"""

from __future__ import print_function
import ctypes, sys, os
import time
import logging
import traceback

# 配置日志信息 程序出现异常 将异常写入日志
logging.basicConfig(filename='net_monitor.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def is_admin():
    """
    获取管理员权限
    :return:
    """
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception as e:
        # 出现异常 将异常写入日志文件
        logging.debug(traceback.format_exc())
        return False


def open_app(app_dir):
    """
    启动 应用
    :param app_dir: 应用路径
    :return:
    """
    os.startfile(app_dir)


# TODO 该程序会弹出命令行窗口，并且每ping一次，就会产生一个窗口
while True:
    try:
        if is_admin():
            try:
                # ping baidu.com 检查网络连接情况 如果断网 返回值 != 0
                state_code = os.system('ping www.baidu.com')
                print(state_code)
                if state_code:
                    # 先杀掉NetKeeper进程
                    os.system("taskkill /F /IM NK.exe")
                    # 启动NetKeeper进程
                    app_dir = r'D:\NetKeeper\NetKeeper\NetKeeper.exe'  # 指定应用程序目录
                    open_app(app_dir)
                    time.sleep(60)
            except Exception as e:
                print(e)
        else:
            # 如果没有获取管理员权限 则强制获取管理员权限 根据不同的python版本进行获取 py3 or py2
            if sys.version_info[0] == 3:
                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
            else:
                ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__),
                                                    None, 1)
        # 每两分钟检测一次
        time.sleep(120)
    except Exception as e:
        # 出现异常 将异常写入日志文件 追加的形式
        logging.debug(traceback.format_exc())
