import socket
import threading
from dictionary import object_dictionary


LOCALHOST = '127.0.0.1'
PORT = 5000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Server started")
print("Waiting for client request..")

def run(conn,Address):
    while True:
        data = conn.recv(2048)
        msg = data.decode()
        if any([True for k, v in object_dictionary.items() if v == msg]):
            print('ACCESS GRANTED',{Address})
            send_yes(conn)
        else:
            print('ACCESS DENIED',{Address})
            send_no(conn)

def send_yes(conn):
    data1 = 'ACCESS GRANTED'
    conn.sendall(data1.encode())  # send data to the client

def send_no(conn):
    data2 = 'ACCESS DENIED'
    conn.sendall(data2.encode())  # send data to the client

def receive():
    while True:
        server.listen()
        conn, Address = server.accept()
        print('Connected to:',Address)
        thread=threading.Thread(target=run,args=(conn,Address))
        thread.start()

if __name__ == '__main__':
    receive()
