# 3 - Contagem de Vogais:

# Crie uma função que conte o número de vogais em uma string. Utilize um loop para percorrer a string e verificar cada caractere:
lista_vogais = ["a", "e", "i", "o", "u"]

def contar_vogais(texto):
    quantidades_vogais = 0
    for letra in texto:
        if letra in lista_vogais:
            quantidades_vogais +=1
    print(quantidades_vogais)

contar_vogais("teste")