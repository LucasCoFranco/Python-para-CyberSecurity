#1 - Faca um programa que peca dois numeros ao usuario e mostre qual
#o maior e qual o menor

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

if n1 > n2:
    print("O maior numero e ", n1)
else:
    print("O maior numero e ", n2)
#2 - Escreva um programa em Python que recebe um inteiro e diga se
#e par ou impar

num = int(input("Digite um numero: "))

if num % 2 == 0:
    print(f"O numero {num} e par")
else:
    print(f"O numero {num }e impar")

#3- Faca um programa que verifique o estado civil de uma pessoa.
#Se a letra digitada e "C"(Casado),"S"(Solteiro),"D"(Divorciado),
#"V"(Viuvo) ou "O"(outros). Conforme a letra escrita pelo usuario
#seu programa deve escrever o estado civi, exemplo:
#Usuario digita C
#seu programa deve responder:
# C - Casado

estado = input("Digite a letra referente ao estado civil - C (Casado), S(Solteiro), D (Divorciado),V (Viuvo) ou O(outros): ")

if estado == "C":
    print("C-Casado")
elif estado == "S":
    print("S-Solteiro")
elif estado == "D":
    print("D-Divorciado")
elif estado == "V":
    print("V-Viuvo")
elif estado == "O":
    print("O-Outros")
else:
    print("Letra nao identificada")