import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    mensagem_envio = input("Digite a mensagem: ")
    cliente.connect((IP, 12000))
    cliente.sendto(mensagem_envio.encode(), (IP, 12000))
