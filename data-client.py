import socket

host = 'localhost'
port = 65515
size= 2048
def filesender():
    s= socket.socket()
    s.connect((host,port))
    archivo = open("tcp/data.txt","r")
    info  = archivo.read()
    s.send("data.txt".encode())
    print("enviando data del archivo")
    s.send(info.encode())
    print("archivo mandado correctamente")
    archivo.close()
    s.close()


if __name__ == "__main__":
    filesender()