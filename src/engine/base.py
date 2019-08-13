import json
import requests
from config import settings
from ..plugins import get_server_info


class BaseHandler(object):

    def __init__(self):
        self.asset_api = settings.ASSET_API

    def cmd(self, command, hostname=None):
        raise NotImplementedError("cmd must be Implemented")

    def handler(self):
        '''
        约束所有派生类都必须实现 handler 方法
        :return:
        '''

        raise NotImplementedError("handler must be Implemented")


class SaltandSSHhanders(BaseHandler):

    def handler(self):
        '''
        处理 SSH 模式下资产采集
        :return:
        '''

        # 1. 获取 的主机列表
        from concurrent.futures import ThreadPoolExecutor

        # url = "http://127.0.0.1:8000/api/asset/"  # 需要加杠
        url = self.asset_api

        hostname_list_raw = requests.get(url=url)  #
        hostname_list = hostname_list_raw.json()

        pool = ThreadPoolExecutor(10)
        for hostname in hostname_list:
            pool.submit(self.task, hostname)





    def task(self, hostname):
        info = get_server_info(self, hostname)
        print(info)



        r1 = requests.post(
            url=self.asset_api,
            data=json.dumps(info).encode('utf-8'),
            headers={
                'Content-Type': 'application/json'
            }
            # data=info
        )

        print(r1.text)
