#1 - Cálculo de Área:

# Crie uma função que calcule a área de um retângulo, recebendo como parâmetros a base e a altura. Crie outra função que calcule a área de um círculo, recebendo como parâmetro o raio. Utilize estruturas condicionais para permitir que o usuário escolha qual forma deseja calcular a área

def retangulo_area(numero1, numero2):
    print(numero1 * numero2)

def circulo_area(numero1):
    #CONSTANTE
    #Para criar valores que não mudam nunca, deve-se colocar o nome da variavel em maiusculo
    PI = 3.14
    print(numero1 * numero1 * PI)

pergunta = int(input("Qual area voce deseja calcular? 1-retangulo 2-circulo : "))

if pergunta == 1:
    num1 = int(input("Digite o primeiro numero do retangulo: "))
    num2 = int(input("Digite o segundo numero do retangulo: "))
    retangulo_area(num1, num2)

elif pergunta == 2:
    num1 = int(input("Digite o raio do circulo"))
    circulo_area(num1)

else: 
    print("Numero invalido")
