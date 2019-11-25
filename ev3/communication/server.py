import socket

from pybricks.tools import (print, wait, StopWatch)

class Server:
    '''Server socket class'''

    def __init__(self, host, port):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = (host, port)

    def start_server(self):
        print("Starting server on '%s:%s'" % self.server_address)
        
        while True:
            try:
                self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.server_socket.bind(self.server_address)
                self.server_socket.listen(5)
                print("Server started!")
                return
            except OSError as error:
                print(str(error) + " trying again")
                wait(10000)

    def stop_server(self):
        print("Stopping server")
        self.server_socket.close()

    def wait_for_connection(self):
        while True:
            self.connection, self.client_address = self.server_socket.accept()
            if self.connection:
                print("Connection from ", self.client_address)
                return

    def send_data_to_client(self, message):
        assert(self.connection)
        self.connection.send(message.encode())

    def wait_for_data(self):
        assert self.connection
        print("assert complete")
        try:
            while True:
                print("start receiving data")
                data = self.connection.recv(16) 
                print("Received %s" % data.decode())

                if data:
                    return self.parse_data(data.decode())
                else:
                    print("No more data")
                    break
        except Exception:
            self.connection.close()
        # END

    def parse_data(self, data):
        print("data: " + data)
        strings = data.split(",")
        assert(len(strings) == 3)
        print(strings)
        return (float(strings[0]), float(strings[1]), float(strings[2]))
    # END
