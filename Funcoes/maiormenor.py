# 2 - Maior e Menor Número:

# Crie uma função que receba uma lista de números e retorne o maior e o menor valor. Utilize um loop para percorrer a lista e encontrar os valores extremos.

def calcular_maior_menor(lista):
    maior_valor = 0
    menor_valor = 0
    while True:
        valor = input("Valor")
        if valor == "FIM":
            break
        else:
            lista.append(valor)

    for num in lista:
        if num > maior_valor:
            maior_valor = num

        if num < menor_valor:
            menor_valor = num

    print(maior_valor, menor_valor)

calcular_maior_menor()