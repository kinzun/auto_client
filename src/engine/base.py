class BaseHandler(object):

    def cmd(self, command, hostname=None):
        raise NotImplementedError("cmd must be Implemented")

    def handler(self):
        '''
        约束所有派生类都必须实现 handler 方法
        :return:
        '''

        raise NotImplementedError("handler must be Implemented")
