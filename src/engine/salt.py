from .base import SaltandSSHhanders


class SaltHandler(SaltandSSHhanders):

    def cmd(self, command, hostname=None):
        '''
        调用 salttack 远程连接主机并执行命令(saltsack master)
        :param command: 主机名
        :param hostname: 要执行的命令
        :return:
        '''
        import salt.client
        local = salt.client.LocalClient()
        result = local.cmd(hostname, 'cmd.run', [command])
        return result[hostname]
