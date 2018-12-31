import json

class BaseResponse(object):
    def __init__(self,status=200,msg = 'success',data =None):
        self.status = status
        self.msg = msg
        self.data = data

    @property
    def dict(self):
        result = 'status:{},msg:{},data:{}'.format(self.status,self.msg,json.dumps(self.data))
        return result
