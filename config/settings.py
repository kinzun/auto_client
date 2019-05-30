import os

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ENGINE_HANDLERS = {
    'agent': 'src.engine.agent.AgentHandler',
    'ssh': 'src.engine.ssh.SSHHandler',
    'salt': 'src.engine.salt.SaltHandler',
}

ENGINE = "agent"

########   SSH 模式 ######3

# 私钥地址
SSH_PRIVATE_KEY = ""
SSH_PORT = 22
SSH_USER = "cmdb"

########   插件  ######3


PLUGIN_DICT = {
    "disk": "src.plugins.disk.Disk",
    "memory": "src.plugins.memory.Memory",
    "network": "src.plugins.network.Network",
}
########   插件  ######3
DEBUG = True
