'''Faça um programa que apresente o menu de opções a seguir, que permita ao usuário
escolher a opção desejada, receba os dados necessários para executar a operação e
mostre o resultado. Verificar a possibilidade de opção inválida e não se preocupar com
as restrições, como salário inválido.
Menu de opções:
● 1. Novo salário
● 2. Férias
● 3. Décimo terceiro
● 4. Sair
Digite a opção desejada :
Na Opção 1: receber o salário de um funcionário, calcular e mostrar o novo salário
usando as regras a seguir.
Salários Percentagem de aumento
Até R$ 350,00 15%
De R$ 350,00 a R$ 600,00 10%
Acima de R$ 600,00 5%
Na opção 2: receber o salário de um funcionário, calcular e mostrar o valor de suas
férias. Sabe-se que as férias equivalem ao seu salário acrescido de l/2.
Na opção 3: receber o salário de um funcionário e o número de meses de trabalho na
empresa, no máximo 12, calcular e mostrar o valor do décimo terceiro. Sabe-se que o
décimo terceiro equivale ao seu salário multiplicado pelo número de meses de trabalho
dividido por 12.
Na opção 4: sair do programa.
'''
opcao = ""
while opcao != "4":
    print("#")
    print("#")
    print("#")
    print("#")
    print("#")
    print("#")
    print("● 1. Novo salário")
    print("● 2. Férias")
    print("● 3. Décimo terceiro")
    print("● 4. Sair")
    opcao = input("Qual opcao voce deseja: ")

    if opcao == "1":
        salario = int(input("Digite o salario: "))
        if salario < 350:
            salario *= 1.15
            print("Novo salario: ".format(round(salario, 2)))
            print("Novo salario: %.2f" % salario)
        elif salario >= 350 and salario <= 600:
            salario *= 1.10
            print("Novo salario: ",salario)
        else:
            salario *= 1.05
            print("Novo salario: ",salario)
    elif opcao == "2":
        salario += salario/2
        print("Valor das ferias: ", salario)
    elif opcao == "3":
        meses = 0
        while meses > 12:
            meses = int(input("quantos meses de trabalho voce teve trabalhou: "))
            salario = (salario* meses)/12
            print("Valor do decimo terceiro: ", salario)
    elif opcao == "4":
        print("Voce saiu")
        break
    else:
        print("Opcao invalida.\n Escolha um numero valido: ")