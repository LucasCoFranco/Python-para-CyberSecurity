#4 - Um funcionário de uma empresa recebe aumento salarial anualmente. Sabe-se que: Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00; Em 1996 recebeu aumento de 1,5% sobre seu salário inicial; A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.
ano_contratacao = 1995
salario_inicial = 1000
ano_atual = int(input("Informe o ano atual: "))

anos = ano_atual - ano_contratacao

porcentagem = 1.5/100

for a in range(anos):
    porcentagem *= 2

salario_final = salario_inicial * (1 + porcentagem)
print(salario_final)