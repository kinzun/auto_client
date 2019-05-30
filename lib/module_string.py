import importlib


def import_string(path):
    '''
    根据字符串形式去导入路径中的对象

    :param path: src.engine.ssh.SSHHandler'
    :return:
    '''

    # modelue_path =''src.engine.agent.',
    # cls_name = 'AgentHandler'
    module_path, cls_name = path.rsplit('.', maxsplit=1)
    module = importlib.import_module(module_path)
    cls = getattr(module, cls_name)

    return cls
