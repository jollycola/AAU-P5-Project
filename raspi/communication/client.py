'''Module handling the client side of the server/client socket connection'''
import socket

PORT_RANGE = (1234, 1235, 1236, 1237, 1238)

class Client:
    '''A client socket class'''

    def __init__(self, host):
        self.host = host
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_to_server(self):
        '''Creates a connection to the specified server'''
        i = 0

        while True:
            server_address = (self.host, PORT_RANGE[i % len(PORT_RANGE)])
            try:
                self.client_socket.connect(server_address)
                print("Connected to server")
                return
            except OSError:
                print("Could not connect with: %i" % PORT_RANGE[i % len(PORT_RANGE)])
                i += 1

    def wait_for_string(self, string):
        '''Waits until the specified string is received'''
        while True:
            data = self.client_socket.recv(16).decode()
            print("Received %s, expected %s" % (data, string))
            assert data == string
            break

    def send_data_to_server(self, data):
        '''Sends data to the server'''
        # assert self.connection is not None
        self.client_socket.send(data.encode())
