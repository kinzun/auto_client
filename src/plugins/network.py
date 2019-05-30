from ..plugins import get_server_info


class Network(object):

    def process(self, handler, hostname):
        """
        获取网卡信息

        :return:
        """

        handler.cmd("ifconfig en7", hostname)

        return "网络"
