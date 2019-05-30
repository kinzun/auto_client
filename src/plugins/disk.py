from .base import BasePlugins


class Disk(BasePlugins):

    def win(self, handler, hostname):
        result = handler.cmd('df -h', hostname)

        return result

    def linux(self, handler, hostname):
        result = handler.cmd('df -h', hostname)

        return result
