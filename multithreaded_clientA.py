import socket
#from client_led import call_led

def client_program():
    host = '127.0.0.1'   # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # instantiate
    client_socket.connect((host, port))  # connect to the server

    id=input('Enter your id:')


    #message = input(" -> ")  # take input

    while True:
        client_socket.send(id.encode())  # send message
        data = client_socket.recv(2048).decode()  # receive response
        if data=='Enter username':
            username = input('Enter your username:')
            client_socket.send(username.encode())  # send message
            data = client_socket.recv(2048).decode()  # receive response

            if data == 'ACCESS GRANTED':
                print('thanks....')
                #call_led()
            else:
                data != 'ACCESS GRANTED'
                print('Received from server: ' + data)  # show in terminal

        else:
            print('Invalid id..')

        client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()