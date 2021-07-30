import time
import numbers
from config.codeMessageConfig import getCodeMessageConfig

class responseMessage:
    def __init__(self):
        self.code = 0
        self.total = 0
        self.message = 0
        self.timestamp = time.time()
        self.data = []

    def s_data(self, data):
        if data is None:
            self.__initCodeMessage(404)
            return self
        if isinstance(data, list):
            self.data = data
        else:
            _data = []
            _data.append(data)
            self.data = _data
        self.total=len(self.data)
        return self
    
    def s_code(self,code):
        self.__initCodeMessage(code)
        return self;

    def customMes(self,message):
        if message is not None and message!="":
            self.message=message
        return self

    def total(self,total):
        if isinstance(total, numbers.Number):
            self.total=total    
        return self

    def __initCodeMessage(self, code):
        switch = {200: "操作成功",
                  403: "无效访问",
                  413: "强制退出",
                  404: "没有数据",
                  500: "系统错误",
                  0: "操作失败",
                  }
        switch.update(getCodeMessageConfig())
        _message=switch.get(code,None)
        if _message is not None:
            self.code=code
            self.message=_message
        else:
            self.code=-1
            self.message="无效code"
