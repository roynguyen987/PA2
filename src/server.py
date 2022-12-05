from ssl import SOL_SOCKET

from _socket import SO_REUSEADDR

from src.clientworker import ClientWorker
from tournament import Tournament

from socket import socket, AF_INET, SOCK_STREAM


class Server:

    def __init__(self, port, backlog):
        self.port = port
        self.backlog = backlog
        self.tournament = Tournament("", "", "")
        self.connection_counter = 0
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        print("socket created")
        self.cw = ClientWorker("", "", "")



    def run_server(self):

        serversocket = socket(AF_INET, SOCK_STREAM)  # create a socket object
        serversocket.bind(('localhost', 10003))  # bind to the port
        serversocket.listen(5)  # queue up to 5 requests
        while True:
            clientsocket, addr = serversocket.accept()  # Wait for a client connection
            print("Got a connection from {}".format(str(addr)))  # Print the client addess

            msg = "Thank you for connecting\r\n"

            clientsocket.send(msg.encode('ascii'))
            message = clientsocket.recv(1024).decode()
            print(message)



            clientsocket.close()
        serversocket.close()








    def display_message(self, message):
        print("[SER]" + message)

