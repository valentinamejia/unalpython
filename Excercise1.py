'''
solicitar dos listas por teclado, la primera M y la segunda N (las listas almacenan
números y strings).Posteriormente, solicite un entero L, que corresponderá a un indice para
ambas listas. el programa debe imprimir la suma (si ambos son númericos) o concatenar (si son
strings) de los elementos de M + N (en ese orden)
Si se produce un error al sumar elementos de diferente tipo imprimir "No se pueden operar"
si es un error en el indice "Indice no valido"
[3,4,5,6,'Hola','chao']
'''

M = input('Ingrese una lista: \n')
N = input('Ingrese una lista: \n')
L = int(input('Ingrese un índice: \n'))
M = M.split(',')
N = N.split(',')

lenght = len(M)
lenght2 = len(N)

for i in range(lenght):
    if M[i].isnumeric():
        M[i] = int(M[i])
    else:
        M[i] = M[i]

for i in range(lenght2):
    if N[i].isnumeric():
        N[i] = int(N[i])
    else:
        N[i] = N[i]

try:
    if type(M[L]) == type(N[L]):
        print(M[L]+N[L])
    else:
        print('No se pueden operar')

except IndexError:
    print('Indice no válido')
    quit()



'''


'''
