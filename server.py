import socket


MSG_SIZE = 1024

class Server:
    def __init__(self):
        ip = "localhost" # "127.0.0.1"
        port = 1337
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((ip, port))
        self.server_socket.listen()
        self.clients = {}  # {"192.168.1.1": [socket, "Ron"], "10.0.0.1": [socket, "Nick"]}
    
    def connect_client(self):
        client_socket, client_address = self.server_socket.accept()
        print(f"Client ({client_address}) connected!")
        client_socket.send(b"Hello, please enter your name: ")
        client_name = client_socket.recv(MSG_SIZE).decode()
        client_socket.send(f"Welcome {client_name}, enjoy chatting around".encode())
        self.clients[client_address] = [client_socket, client_name]


if __name__ == "__main__":
    server = Server()
    server.connect_client()