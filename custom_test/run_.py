#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import requests


def get_info():
    # 1. 获取资产信息 硬盘 网卡，内容

    import subprocess

    disk = subprocess.getoutput('df')
    info = {'hostname': 'c1', 'menroy': disk}


def x2():
    # 2. 日志处理(堆栈信息）

    # 3. 自动发现
    # 如果只是物理机，sn 做唯一标示
    # 物理 + 虚拟机 1. 系统 + 调用 ( oepnstack api)  : 2. 主机名做唯一标记(
    # 以文件，新旧 主机名。 一起发送。再做更改)
    pass


''' 
拆分。
业务功能多个，不易维护。
设计思想:开放封闭原则.如果业务变了，
封闭： 不要修改源码。源码封闭
开发： 对配置文件开放
'''


def agent(info):
    '''
    获取当前服务器的资产信息提交给 api
    :return:
    '''

    # info = get_info()

    url = "http://127.0.0.1:8000/api/asset/"  # 需要加杠
    r1 = requests.post(url=url,
                       data=json.dumps(info).encode("utf-8"),
                       # json=info
                       # data={'k1': 'v1', 'k2': 'v2'},
                       # 如果 http
                       )

    return r1


# agent()


def task(host):
    info = {'hostname': host, 'disk': "..."}
    url = "http://127.0.0.1:8000/api/asset/"  # 需要加杠
    r1 = requests.post(url=url,
                       data=json.dumps(info).encode("utf-8"),
                       )

    return r1


def ssh():
    # 1 获取未采集服务器列表
    url = "http://127.0.0.1:8000/api/asset/"  # 需要加杠
    r = requests.get(url=url)  #
    # print(r1.text)
    # print(type(r1.text))
    # print(type(r1.content))
    # 转换为 json
    # print(type(r1.json()))
    # print(r1.json())
    # print(r1)

    from concurrent.futures import ThreadPoolExecutor
    pool = ThreadPoolExecutor(10)
    for host in r.json():
        pool.submit()
        # 每一台主机，调用 ssh 或 salt 接口远程连接上 主机执行命令，获取结果
        info = {'hostname': host, "disk": "..."}
        # 通过 requests 发送 post 请求 将资产数据提交 api
        ret_one = agent(info)
        print(ret_one.text)
        pool.s


ssh()
