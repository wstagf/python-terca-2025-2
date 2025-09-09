# range(x) cria sequência de 0 a x (exclusive).

# range(start, end) cria de start antes de  end.

# range(start, end, step) cria de start antes de  end, porem com passo de step.



print('Tabuada de 4 vezes de 1 a 10')

# codigo gerado pela IA, muito avancado, utiliza poucas linhas para fazer o
# trem tudo... nao e bom para comecar a aprender
# for i in range(1, 11): # for comecando em 1, ate que seja menor do 11
#     print(f'Tabuada do {i}')
#     for j in range(1, 11):
#         print(f'{i} x {j} = {i * j}')
#     print('')


numero = 4


# print(str(numero) + "x2 = " + str(numero * 2))
# print(str(numero) + "x3 = " + str(numero * 3))
# print(str(numero) + "x4 = " + str(numero * 4))
# print(str(numero) + "x5 = " + str(numero * 5))
# print(str(numero) + "x6 = " + str(numero * 6))
# print(str(numero) + "x7 = " + str(numero * 7))
# print(str(numero) + "x8 = " + str(numero * 8))
# print(str(numero) + "x9 = " + str(numero * 9))
# print(str(numero) + "x10 = " + str(numero * 10))


for a in range(10): 

    # concatenacao
    print(str(numero) + " x " + str(a+1) +  " = " + str(numero * (a+1)))

    # interpolacao
    print(f'{numero} x {a+1} = {numero * (a+1)}')


 
 