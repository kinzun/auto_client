from .base import BasePlugins


class Network(BasePlugins):

    def win(self, handler, hostname):
        """
        获取网卡信息

        :return:
        """

        info = handler.cmd("ifconfig en7", hostname)

        return info

    def linux(self, handler, hostname):
        info = handler.cmd("ifconfig en7", hostname)

        return info

