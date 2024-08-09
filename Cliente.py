import socket

def start_client(address: str, port: int):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    message = input('Digite uma mensagem: ').encode()

    client_socket.sendto(message, (address, port))
    client_socket.close()

if __name__ == "__main__":
    DESTINATION = 'localhost'
    PORT = 6000
    start_client(DESTINATION, PORT)
