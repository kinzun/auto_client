class BaseResponse(object):

    def __init__(self, ):
        self.status = True
        self.error = False
        self.data = None

    @property
    def dict(self):
        return self.__dict__



