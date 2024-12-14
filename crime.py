#3 - Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#“Telefonou para a vítima? “
# “Esteve no local do crime?”
# “Mora perto da vítima? “
# “Devia para a vítima? “
# “Já trabalhou com a vítima? “
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como “Suspeita”, entre 3 e 4 como “Cúmplice” e 5 como “Assassino“. Caso contrário, ele será classificado como “Inocente“.
ques1 = input("Telefonou para a vitima?: (Sim/Não)").lower()
ques2 = input("Esteve no local do crime?: ").lower()
ques3 = input("Mora perto da vitima?: ").lower()
ques4 = input("Devia para a vitima?: ").lower()
ques5 = input("Ja trabalhou com a vitima?: ").lower()

soma = 0

if ques1 == "sim":
    soma+=1
elif ques2 == "sim":
    soma+=1
elif ques3 == "sim":
    soma+=1
elif ques4 == "sim":
    soma+=1
elif ques5 == "sim":
    soma+=1

if soma == 2:
    print("Suspeita")
elif soma == 3 or soma == 4:
    print("Cúmplice")
elif soma == 5:
    print("Assassino")
else:
    print("Inocente")
