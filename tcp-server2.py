from email.headerregistry import Address
import socket


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 65515
Size= 2048
def servidor():
    serversocket.bind((host,port))
    serversocket.listen(3)
    while True:
        print("esperando conexion")  
        try:
            clientsocket, address = serversocket.accept()
            print("connect from:",address)
            nombre = clientsocket.recv(Size).decode()
            print(nombre)
            name= open(nombre, "w")
            document = clientsocket.recv(Size).decode()
            name.write(document)
            print("archivo guardado exitosamente!")
            name.close()
            clientsocket.close()
        except Exception as e:
            print("error on server")

if __name__=="__main__":
    servidor()
