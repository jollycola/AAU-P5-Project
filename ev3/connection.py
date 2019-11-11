#!/usr/bin/env pybricks-micropython

import socket


class Connection:

    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = (host, port)

    def connection_to_server(self):
        print("Connecting to server on '%s:%s'" % self.server_address)
        self.sock.connect(self.server_address)

    def start_server(self):
        print("Starting server on '%s:%s'" % self.server_address)
        self.sock.bind(self.server_address)
        self.sock.listen(5)

    def stop_server(self):
        print("Stopping server")
        self.sock.close()

    def wait_for_connection(self):
        while True:
            self.connection, self.client_address = self.sock.accept()
            if self.connection:
                print("Connection from ", self.client_address)
                return


    def send_data_to_client(self, message):
        assert(self.connection)
        self.connection.send(message.encode())


    def send_data_to_server(self, message):
        self.sock.send(message)


    def wait_for_data(self):
        assert(self.connection)
        try:
            while True:
                data = self.connection.recv(16)
                print("Received %s" % data.decode())

                if data:
                    return self.parse_data(data)
                else:
                    print("No more data")
                    break
        except Exception:
            self.connection.close()
        # END


    def parse_data(data: str):
        strings = data.split(",")
        assert(len(strings) == 3)
        return (float(strings[0]), float(strings[1]), float(strings[2]))
    # END
