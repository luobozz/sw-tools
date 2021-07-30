import requests



# payload = {"push_ip":"192.168.1.25", "push_port":1935, "app":"live"}
headers = {
    'content-type': "application/x-www-form-urlencoded"
}

# way,url,data,successCondition,printCallBack
class testModal:
    def __init__(self):
        self.way="GET"
        self.url=None
        self.data={}
        self.successCondition=None
        self.printCallBack=None
        self.isSuccess=False
        self.result=""

    def s_way(self,way):
        self.way="GET" if way==None or way=='' else way
        return self;

    def s_url(self,url):
        self.url="" if url==None or url=='' else url
        return self;

    def s_data(self,data):
        self.data={} if data==None or data=='' else data
        return self;

    def s_successCondition(self,successCondition):
        self.successCondition=None if successCondition==None or type(successCondition).__name__=="function" else successCondition
        return self;

    def s_printCallBack(self,printCallBack):
        self.printCallBack=None if printCallBack==None or type(printCallBack).__name__=="function" else printCallBack
        return self;

    def doTest(self):
        if self.url==None:
            self.isSuccess=False
            return
        response = requests.request(self.way, self.url, data=self.data, headers=headers)
        print(response)
        if(self.printCallBack):
            self.printCallBack(response,True)
        else:
            print(self.url,response,self.isSuccess)

def rdTest():
    host="http://192.168.1.25:5000"
    def setPushUrlSuccessCallback(res):
        return res=="ok";
    def setPushUrlPrintCallback(httpRes,testRes):
        print("setPushUrl",httpRes,testRes)

    setPushUrl=testModal().s_way("POST").s_url(host+"/site/reportStreamService/config").s_data('{"push_ip":"192.168.1.25", "push_port":1935, "app":"live"}').s_successCondition(setPushUrlSuccessCallback).s_printCallBack(setPushUrlPrintCallback);
    setPushUrl.doTest()


if __name__ == '__main__':
    rdTest()
