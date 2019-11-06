import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('192.168.137.249', 42069)
sock.connect(server_address)

try:
    message = 'hello ev3'
    sock.sendall(message.encode())

    amount_recieved = 0
    amount_expected = len(message)

    while amount_recieved < amount_expected:
        data = sock.recv(16)
        amount_recieved += len(data)

        print("Recieved %s" % data)


finally:
    print("closing socket")
    sock.close()
