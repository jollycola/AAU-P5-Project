import socket


class Client:
    '''A client socket class'''

    def __init__(self, host, port):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = (host, port)
    # END

    def connect_to_server(self):
        '''Creates a connection to the specified server'''
        self.client_socket.connect(self.server_address)

    def wait_for_ready(self, string):
        '''Waits until the specified string is received'''
        while True:
            data = self.client_socket.recv