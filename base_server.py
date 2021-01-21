import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

servidor.bind(('', 12000))


while True:
    mensagem_bytes, endereco_ip_ciente = servidor.recvfrom(2048)
    servidor.sendto(mensagem_bytes, endereco_ip_ciente)
    mesagem = mensagem_bytes.decode()
    print(mesagem)
