from config import settings



class BasePlugins(object):

    def get_os(self):
        '''
        获取平台信息
        :return: 平台系统
        '''

        import platform
        platform_ = platform.system()
        return platform_

    def process(self, hander, hostname):

        platform_ = self.get_os()

        if platform_ == "Linux":
            return self.linux(hander, hostname)
        else:
            return self.linux(hander, hostname)

    def win(self, handler, hostname):
        raise NotImplementedError("win must be Implemented")

    def linux(self, handler, hostname):
        raise NotImplementedError("linux must be Implemented")
