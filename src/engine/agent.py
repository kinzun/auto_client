import requests
import json

from .base import BaseHandler
from ..plugins import get_server_info

from config import settings


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
        # 2. 发送到 API
        r1 = requests.post(
            url=self.asset_api,
            # 可以加头，类型
            data=json.dumps(info).encode('utf-8'),
            headers={
                'Content-Type': 'application/json'
            }
            # data=info
        )
        print(r1)
