import socket
rec = 8*2
host = 'localhost'
port = 65515

def client():
    s = socket.socket()
    s.connect((host,port))
    try:
        while True:
            number = s.recv(rec)
            print(number)
            break
    except Exception as e:
        print("error de cliente "+e)
    
    finally:
        s.close()
if __name__ == "__main__":
    client()