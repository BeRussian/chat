import socket


MSG_SIZE = 1024

class Client:
    def __init__(self):
        server_ip = "localhost"  # should be the real server's ip
        server_port = 1337
        self.connect(server_ip, server_port)

    def connect(self, ip, port):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.connect((ip, port))
        name_prompt = server_socket.recv(MSG_SIZE).decode()
        name = input(name_prompt)
        server_socket.send(name.encode())
        server_msg = server_socket.recv(MSG_SIZE).decode()
        print(server_msg)


if __name__ == "__main__":
    client = Client()