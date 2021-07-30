import socket
def net_is_used(port,ip='127.0.0.1'):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        s.connect((ip,port))
        s.shutdown(2)
        return True
    except:
        return False

print(net_is_used(5000,"192.168.1.42"))
