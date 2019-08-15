from config import settings

from lib.module_string import import_string


def get_server_info(handler, hostname=None):
    '''
    循环所有的插件，获取所有的资产信息，然后返回
    :param handler:
    :return:
    '''

    '''
    "disk": "src.plugins.disk.Disk",
    "memory": "src.plugins.memory.Memory",
    "network": "src.plugins.network.Network",
    '''

    info = {}
    for name, path in settings.PLUGIN_DICT.items():
        cls = import_string(path)
        obj = cls()
        result = obj.process(handler, hostname)
        info[name] = result

    # {'disk':'硬盘'，'memory':'内存','network':网卡}



    return info
