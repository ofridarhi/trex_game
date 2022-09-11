from re import T
import socket
import threading
from xmlrpc.client import TRANSPORT_ERROR

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn,addr):
    pass

def start():
    server.listen()
    while True:
        conn, addr = server.accept


print("[STARTING] server is starting...") 
start()