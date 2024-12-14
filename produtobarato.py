#2 - Faça um programa que pergunte o preço de três produtos e informe qual produto
#você deve comprar, sabendo que a decisão é sempre pelo mais barato.
prod1 = float(input("Digite o valor do primeiro produto: "))
prod2 = float(input("Digite o valor do segundo produto: "))
prod3 = float(input("Digite o valor do ultimo produto: "))

print("")
print("")
print("")
print("")
if prod1 < prod2 and prod1 < prod3:
    print("O menor valor é o primeiro produto")
elif prod2 < prod3:
    print("O menor valor é o segundo produto")
else:
    print("O menor valor é o terceiro produto")
print("")
print("")
print("")
print("")