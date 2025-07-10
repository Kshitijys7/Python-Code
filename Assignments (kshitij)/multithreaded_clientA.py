import socket
#from client_led import call_led

def client_program():
    host = '127.0.0.1'   # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = input(" -> ")  # take input

    while True:
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response
        if data == 'ACCESS GRANTED':
            print('Thanks..')
        else:
            data != 'ACCESS GRANTED'
        print('Received from server: ' + data)  # show in terminal
        message = input(" -> ")  # again take input



if __name__ == '__main__':
    client_program()
