import socket
import time
timeout = 0.3
socket.setdefaulttimeout(timeout)
def net_is_used(port,ip='127.0.0.1'):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        times=time.time()
        print(ip,":",port)
        s.connect((ip,port))
        s.shutdown(2)
        return True
    except:
        return False
    # finally:
    #     # print(time.time()-times,"\n")
