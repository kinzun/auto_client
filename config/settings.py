import os

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ENGINE_HANDLERS = {
    'agent': 'src.engine.agent.AgentHandler',
    'ssh': 'src.engine.ssh.SSHHandler',
    'salt': 'src.engine.salt.SaltHandler',
}

# ENGINE = "ssh"
ENGINE = "agent"

########   SSH 模式 ######3

# 私钥地址
SSH_PRIVATE_KEY = ""
SSH_PORT = 22
SSH_USER = "cmdb"

########   插件  ######3


PLUGIN_DICT = {
    "basic": "src.plugins.basic.Basic",
    "cpu": "src.plugins.cpu.Cpu",
    "memory": "src.plugins.memory.Memory",
    "disk": "src.plugins.disk.Disk",
    "network": "src.plugins.network.Network",
    "board": "src.plugins.main_board.MainBoard",
}
########   插件  ######3
DEBUG = True
# ASSET_API = "http://127.0.0.1:8000/cmdb/assets/"
ASSET_API = "http://127.0.0.1:8000/api/asset/"

########   日志路径  ######3

LOG_FILE_PATH = os.path.join(BASEDIR, "log", "cmdb.log")

########   唯一标识路径 ######3

CERT_FILE_PATH = os.path.join(BASEDIR, "config", "cert")

# URL 认证 key
URL_AUTH_KEY = '60xXhoPGZ39z'

# 公钥
PUB_KEY = ""
