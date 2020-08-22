import numpy as np


def multiplica_matriz():

    matrix_size = 10

    matriz1 = np.random.uniform(0.0,10001.0, size=(matrix_size,matrix_size)) # Gera matriz1
    matriz2 = np.random.uniform(0.0,10001.0, size=(matrix_size,matrix_size)) # Gera matriz2
    resultado = np.random.uniform(0.0,0.0, size=(matrix_size,matrix_size))

    print(matriz1) 
    print("\n")
    print(matriz2) 
    print("\n")
    print(resultado)
    print("\n")

    for index in range(len(matriz1)): #percorre matriz1
        for index2 in range(len(matriz2[0])): #percorre matriz2
            for index3 in range(len(matriz2)):
                resultado[index][index2] += matriz1[index][index3] * matriz2[index3][index2]

    for index_resultado in resultado:
        print(resultado)
    

multiplica_matriz()