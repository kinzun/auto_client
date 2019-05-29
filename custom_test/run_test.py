#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import requests


def x2():
    # 2. 日志处理(堆栈信息）

    # 3. 自动发现
    # 如果只是物理机，sn 做唯一标示
    # 物理 + 虚拟机 1. 系统 + 调用 ( oepnstack api)  : 2. 主机名做唯一标记(
    # 以文件，新旧 主机名。 一起发送。再做更改)
    pass


def get_info():
    # 1. 获取资产信息 硬盘 网卡，内容

    import subprocess
    disk = subprocess.getoutput('df')
    info = {'hostname': 'c1', 'menroy': disk}


def agent(info):
    '''
    获取当前服务器的资产信息提交给 api
    :return:
    '''
    # info = get_info()
    url = "http://127.0.0.1:8000/api/asset/"  # 需要加杠
    r1 = requests.post(url=url,
                       data=json.dumps(info).encode("utf-8"),
                       )
    return r1


def task(host):
    # 每一台主机，调用 ssh 或 salt 接口远程连接上 主机执行命令，获取结果
    info = {'hostname': host, "disk": "..."}
    # 通过 requests 发送 post 请求 将资产数据提交 api
    ret_one = agent(info)
    print(ret_one.text)


def ssh():
    # 1 获取未采集服务器列表
    url = "http://127.0.0.1:8000/api/asset/"  # 需要加杠
    host_list = requests.get(url=url)  # 主机列表

    from concurrent.futures import ThreadPoolExecutor
    pool = ThreadPoolExecutor(10)

    for host in host_list.json():
        pool.submit(task, host)


ssh()
