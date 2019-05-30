class Memory(object):

    def process(self, handler, hostname):
        """
        获取内存信息

        :return:
        """
        result = handler.cmd('top -l 1 | head -n 10 | grep PhysMem',
                             hostname)
        return result
