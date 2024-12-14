from socket import *

#           localhost
endereco = "127.0.0.1"
porta = 43210

obj_socket = socket(AF_INET, SOCK_STREAM)
obj_socket.bind((endereco, porta))
obj_socket.listen(2)
print("Aguardando cliente...")

while True:
    conexao, cliente = obj_socket.accept()
    print("Conectando com: ", cliente)

    while True:
        mesangem = str(conexao.recv(1024))
        #b'text'
        #texto
        print("Recebi: ", str(mesangem)[2:-1])

        msg = bytes(input("Mensagem: "), 'utf-8')
        obj_socket.send(msg)
        break
    conexao.close()