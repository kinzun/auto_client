from .base import BasePlugins


class Memory(BasePlugins):

    def win(self, handler, hostname):
        '''
        获取内存信息
        :param handler:
        :param hostname:
        :return:
        '''
        result = handler.cmd('top -l 1 | head -n 10 | grep PhysMem',
                             hostname)
        return result

    def linux(self, handler, hostname):
        '''
        获取内存信息
        :param handler:
        :param hostname:
        :return:
        '''
        result = handler.cmd('top -l 1 | head -n 10 | grep PhysMem',
                             hostname)
        return result
