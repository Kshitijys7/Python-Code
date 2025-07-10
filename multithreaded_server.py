import logging
import socket
from threading import Thread
from dictionary import object_dictionary,key_list


class ClientThread(Thread):
    def __init__(self, Address, clientsocket):
        Thread.__init__(self)
        self.new_client = clientsocket
        print("New connection added: ", Address)

    def run(self):
        print("Connection from : ", Address)
        while True:
            data = self.new_client.recv(2048)
            msg1 = data.decode()
            print(msg1)
            for i in key_list:
                if(i==msg1):
                    self.send_username()
                    data = self.new_client.recv(2048)
                    msg2 = data.decode()
                    if(object_dictionary.get(msg1)==msg2):
                        print('ACCESS GRANTED')
                        self.send_yes()
                    else:
                        logging.error('ACCESS DENIED')
                        self.invalid_username()

            #if any([True for k, v in object_dictionary.items() if v == msg]):
            #if(msg=='1'):
            #    print('ACCESS GRANTED')
            #   self.send_yes()
            #else:
            #    logging.error('ACCESS DENIED')
            #    self.send_no()

    def send_username(self):
        data0='Enter username'
        conn.sendall(data0.encode())

    def invalid_id(self):
        data4='Invalid id..'
        conn.sendall(data4.encode())

    def invalid_username(self):
        data5='Invalid username..'
        conn.sendall(data5.encode())

    def send_yes(self):
        data1 = 'ACCESS GRANTED'
        conn.sendall(data1.encode())  # send data to the client

    def send_no(self):
        data2 = 'ACCESS DENIED'
        conn.sendall(data2.encode())  # send data to the client



LOCALHOST = '127.0.0.1'
PORT = 5000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Server started")
print("Waiting for client request..")
while True:
    server.listen(1)
    conn, Address = server.accept()
    newthread = ClientThread(Address, conn)
    newthread.start()
