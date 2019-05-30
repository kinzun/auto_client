class Disk(object):



    def process(self, handler, hostname):
        """
        获取硬盘信息

        :return:
        """
        result = handler.cmd('df -h', hostname)

        return result
