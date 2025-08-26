
# 5. Tendo como dado de entrada a altura (h)
#  de uma pessoa e seu sexo,
#  construa um algoritmo que calcule seu peso ideal,
#  utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7


altura = float(input("Digite sua altura: "))

sexo = input("Digite M para masculino e F para feminimo: ")

pesoideal = 0

if(sexo == "M" or sexo =="m"): 
  print("é masculino")
  
  pesoideal = (72.7*altura) - 58
elif (sexo == "F" or sexo =="f"): 
    print("é feminimo")
    pesoideal = (62.1*altura) - 44.7
else:
    print("digitado errado") 

print(altura + altura)
print(sexo)
print("Seu peso ideal é")
print(pesoideal)

