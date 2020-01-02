import time

import requests
import json
import pathlib
from pathlib import Path

from .base import BaseHandler
from ..plugins import get_server_info

from config import settings
from lib.auth import gen_sign
from lib.security import encrypt


class AgentHandler(BaseHandler):

    def cmd(self, command, hostname=None):
        import subprocess
        return subprocess.getoutput(command)

    def handler(self):
        '''
        处理 Agent 模式下资产采集: 网卡 内存 硬盘 ...
        :return:
        '''

        # 调度 plugins.disk / plugins.network
        # 1. 通过调用 get_server_info 网卡 内存 硬盘 ...

        info = get_server_info(self)

        # 2. 获取本地文件唯一标示

        if not Path(settings.CERT_FILE_PATH).exists():
            # 新服务器 应该在数据库增加数据。
            info["type"] = "create"
        else:
            with open(settings.CERT_FILE_PATH, "r", encoding='utf-8') as f:
                cert = f.read()

            if cert == info["basic"]['data']['hostname']:
                # 主机名未更新，汇报给 API ，API 做更新。
                info["type"] = "update"
            else:
                info["cert"] = cert
                info["type"] = "host_update"

        # 3. 发送到 API

        ctime = int(time.time() * 1000)

        r1 = requests.post(
            url=self.asset_api,

            params={'sign': gen_sign(ctime), 'ctime': ctime},
            # 可以加头，类型
            data=encrypt(json.dumps(info).encode('utf-8')),

            headers={
                'Content-Type': 'application/json'
            }
        )
        print(info)


        print(r1)

        # response = r1.json()
        # print(r1.json())
        # 4. 唯一标识更新
        # if response['status']:
        #     with open(settings.CERT_FILE_PATH, 'w', encoding='utf-8') as f:
        #         f.write(response['data'])
