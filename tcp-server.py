from email.headerregistry import Address
from http import server
import socket
import nacl.utils

n = nacl.utils.random(2)
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 65515

serversocket.bind((host,port))

serversocket.listen(3)

while True:
    print("esperando conexion")
    clientsocket, address = serversocket.accept()

    try:
        print("connect from:",address)
        clientsocket.send(nacl.utils.random(2))
    except Exception as e:
        print("error on server",e)
    finally: 
        clientsocket.close()
