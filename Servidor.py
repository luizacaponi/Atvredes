import socket

def start_server(address: str, port: int):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((address, port))

    print(f'Server rodando em {address}:{port}')

    while True:
        data, client_address = server_socket.recvfrom(1024)
        print(f'{client_address} - Mensagem: {data.decode()}')

if __name__ == "__main__":
    HOST = 'localhost'
    PORT = 6000
    start_server(HOST, PORT)
