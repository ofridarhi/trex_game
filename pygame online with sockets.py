from audioop import add
from re import T
import socket
from sqlite3 import connect
import threading
from xmlrpc.client import TRANSPORT_ERROR

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSEGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn,addr):
    print(F"[NEW CONNECTION] {addr} connected")

    connected = True
    while connect:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSEGE:
                connected = False

        print(f"[{addr}] {msg}")
    conn.close()

def start():
    print(f"[LISTENING] Server is listening on {SERVER}")
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handlge_client, args=(conn, addr))
        thread.start()
        print(F"[ACTIVE CONNECTIONS] {threading.activeCount() -1}")

print("[STARTING] server is starting...") 
start()
