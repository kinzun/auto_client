result = {"status": True, "error": False, "data": None}

try:
    result["status"] = True
except Exception as e:
    pass

print(result)


class BaseResponse(object):

    def __init__(self, ):
        self.status = True
        self.error = False
        self.data = None

    @property
    def dict(self):
        return result.__dict__


result = BaseResponse()

try:
    result.status = 'test'
except Exception as e:
    pass

print(result.dict)
