import socket
import threading
import time
import random

class network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.1.164"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.connect = self.connect()

    def connect(self):
        try:
            self.client.connect (self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

