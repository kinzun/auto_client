from .base import SaltandSSHhanders

from config import settings


class SSHHandler(SaltandSSHhanders):

    def cmd(self, command, hostname=None):
        '''
        调用 parmiko 远程连接主机并执行命令(),
        :param command: 主机名
        :param hostname: 要执行的命令
        :return:
        '''
        import paramiko

        private_key = paramiko.RSAKey.from_private_key_file(settings.SSH_PRIVATE_KEY)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=hostname, port=settings.SSH_PORT, username=settings.SSH_USER, pkey=private_key)
        stdin, stdout, stderr = ssh.exec_command(command)
        result = stdout.read()
        ssh.close()
        return result
