import socket
from _thread import *
import sys

server = "192.168.1.164" #poner aca tu ipv4, dale Javi, animate

port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Esperando para obtener una conexion, por favor espere...")   

def threaded_client(conn):
    conn.send(str.encode("Conectado"))
    respuesta = ""
    while True:
        try:
            data = conn.recv(2048) #latencia
            respuesta = data.decode("utf-8")
            if not data:
                print ("Desconectado")
                break
            else:
                print('Recibido: ' + respuesta)
                print ('Enviando: ' + respuesta)
            conn.sendall(str.encode(respuesta))
        except:
            break

    print("Conexion perdida")
    conn.close()
    
    while True:
        conn, addr = s.accept()
        print("Conectado a :", addr)

        start_new_thread(threaded_client, (conn,))

class network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.1.164"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.id = self.connect()
        print(self.id)
    def connect(self):
        try:
            self.client.connect (self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

n = network()