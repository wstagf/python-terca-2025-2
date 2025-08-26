# 6. Faça um Programa que peça
#  uma data no formato d d / m m /aaaa
#  e determine se a mesma é uma 
#  data válida


# dd < 0
# dd > 31
# dd > 30
# mm < 0
# dd > 12
# aaa ter ate 4 digitos


data_para_validar = input("Digite uma data: ")

print(data_para_validar)
# substring
dia = int(data_para_validar[0:2])
mes = int(data_para_validar[3:5])
ano = int(data_para_validar[6:11])

print(dia)
print(mes)
print(ano)


# ## split
# dados = data_para_validar.split("/")
# print(dados)

# diaSplit = int(dados[0])
# mesSplit = int(dados[1])
# anoSplit = int(dados[2])

# print(diaSplit)
# print(mesSplit)
# print(anoSplit)
qtd_dias_no_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

existeErroNaData = False

if(dia < 0 or dia > qtd_dias_no_mes[mes-1]):
    print("dada invalida")
    existeErroNaData = True

if(mes < 0 or mes > 12):
    print("Data invalida")
    existeErroNaData = True


if(ano < 1900):
    print("Data invalida")
    existeErroNaData = True

qtd_digitos_ano = len(data_para_validar[6:11])
if(qtd_digitos_ano < 4 ):
    existeErroNaData = True

if(existeErroNaData == False):
    print("Data Valida")
