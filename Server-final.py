import socket
import nacl.utils
import nacl.secret
from nacl.signing import SigningKey
from nacl.signing import VerifyKey

llave= nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)


host='localhost'
port= 65515
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#funcionalidades

#6
Usuarios ={
    "726802@iteso.mx":"cripto"
}
#2
def cifradoArchivo(infoArchivo):
    key=nacl.secret.SecretBox(llave)
    cifrado= key.encrypt(bytes(infoArchivo,'utf-8'))
    f= open("proyecto-f.txt","a")
    f.write(f"Cifrado : \n{cifrado} \n")
    f.close()
    print("archivo cifrado correctamente")
    return cifrado
#3
def descifradoArchivo(infoArchivo):
    try:
        box=nacl.secret.SecretBox(llave)
        desencriptar= box.decrypt(infoArchivo)
        f=open("proyecto-f.txt","a")
        f.write(f"texto Decifrado:\n {desencriptar}\n")
        f.close()
        print("archivo decifrado correctamente")
        return desencriptar
    except Exception as e:
        print(f"error on server {e}")
#4
def signatureArchivo(sarchi): ##firma de archivo
    sign_key= SigningKey.generate()

    firmada= sign_key.sign(sarchi)
    f=open("proyecto-f.txt","a")
    f.write(f'Archivo firmado: \n {firmada} \n')
    f.close()
    print("firma correcta del archivo")
    return firmada,sign_key
#5
def VerifySign(Info, key:SigningKey): #confirmacion firma archivo
    verificacion= VerifyKey(key.verify_key.encode())
    ans=verificacion.verify(Info)
    f=open("proyecto-f.txt","a")
    f.write(f'Archivo Verificado: \n {ans} \n')
    f.close()
    print("verificacion del archivo correctamente")
    return ans
#7
def addtolog(usr, pw):
    file= open("proyecto-f.txt","a")
    if usr != "" and pw != "":
        if usr in Usuarios and pw in Usuarios.values():
            file.write(f'Entro el usuario: {usr} \n')
            return True
    file.write(f'Error, trato de entrar el usuario: {usr}')
    file.close()
    return False

if __name__=="__main__":

    serversocket.bind((host,port))
    serversocket.listen(3)

    clientsocket, address = serversocket.accept()
    print("connect from:",address)
    print("\n")
    todo= clientsocket.recv(4096).decode()
    message, user, pwd, filen= todo.split(",")


    if not addtolog(user,pwd):
        clientsocket.sendall(f'user y pass no validos'.encode())
    
    else:
        archivoc = cifradoArchivo(message)
        archivod= descifradoArchivo(archivoc)
        archivofi, llave= signatureArchivo(archivod)
        archivov = VerifySign(archivofi, llave)
    
    serversocket.close()
        