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

        info = get_server_info(self)
        print(info)
        # print('agent', info)
