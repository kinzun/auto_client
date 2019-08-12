from config import settings


class BasePlugins(object):

    def __init__(self):
        self.debug = settings.DEBUG
        self.base_dir = settings.BASEDIR

    def get_os(self):
        '''
        获取平台信息
        :return: 平台系统
        '''

        import platform
        platform_ = platform.system()
        return platform_

    def process(self, handler, hostname):

        platform_ = self.get_os()

        if platform_ == "Linux":
            return self.linux(handler, hostname)
        else:
            return self.linux(handler, hostname)

    def win(self, handler, hostname):
        raise NotImplementedError("win must be Implemented")

    def linux(self, handler, hostname):
        raise NotImplementedError("linux must be Implemented")
