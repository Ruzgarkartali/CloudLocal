import socket

def Main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    name = socket.gethostname()
    ip = '127.0.0.1'
    port = 4500
    address = (ip, port)
    server.bind(address)
    server.listen(1)

    while True:
        client, addr = server.accept()
        print('Start listening on', ip, ':', port)
        print('Received connection from', addr[0], ':', addr[1])
        while True:
            data = client.recv(1024).decode('utf-8')
            print('Received', data, 'from the client')

            # DO something.....
            client.send('Goodbye'.encode('utf-8'))
            client.close()
            break
if __name__ == '__main__':
    Main()