import socket

def Main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip = '127.0.0.1'
    port = 4500
    address = (ip, port)
    message = 'mymessage'
    client = socket.socket()
    client.connect(address)
    client.sendall(message.encode('utf-8'))

if __name__ == '__main__':
    Main()