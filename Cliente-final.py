from socket import socket

import socket

host = 'localhost'
port = 65515

uprueba= '726802@iteso.mx'
pprueba='cripto'
fileloc= 'data.txt'

if __name__ =="__main__":

    with open(fileloc,"rb") as fdtr:
        message= fdtr.read()
    
    s= socket.socket()
    s.connect((host,port))

    s.sendall(
        f'{message},{uprueba},{pprueba},{fileloc}'.encode())
    data= s.recv(4096)
    print(data.decode())
