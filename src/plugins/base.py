class BasePlugins(object):

    def process(self, hander, hostname):
        import platform

        platform_ = platform.system()

        if platform_ == "Linux":
            return self.linux(hander, hostname)
        else:
            return self.linux(hander, hostname)

    def win(self, handler, hostname):
        raise NotImplementedError("win must be Implemented")

    def linux(self, handler, hostname):
        raise NotImplementedError("linux must be Implemented")
