from utils.cmdHelper import *
from utils.netHelper import *
import platform
import re

class service:
    def test(self):
        arpList=cmd("arp -a").exec()
        port=554
        ipList=[]
        for arpStr in arpList:
            pattern = re.compile(r'((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})).1(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2}))')
            mc=pattern.search(arpStr)
            if(mc):
                ip=mc.group()
                if(net_is_used(port,ip)):
                    ipList.append(ip)
        return(ipList)
    def psmSniffer(self):
        arpList=cmd("arp -a").exec()
        port=5000
        ipList=[]
        for arpStr in arpList:
            pattern = re.compile(r'((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})).1(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2}))')
            mc=pattern.search(arpStr)
            if(mc):
                ip=mc.group()
                if(net_is_used(port,ip)):
                    ipList.append(ip)
        return(ipList)