#5 - A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.
num_ant = 1
num_atual = 1
prox_num = 0

serie = int(input("Digite o numero de serie que deseja saber: "))
for i in range(10):
    prox_num = num_ant + num_atual
    num_ant = num_atual
    num_atual = prox_num
    print(num_ant)