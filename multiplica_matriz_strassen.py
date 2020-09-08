import numpy as np 
import sys
sys.setrecursionlimit(90000000)

matrix_size = 8
valor_maximo = 6

matriz1_strassen = np.random.randint(0,valor_maximo, size=(matrix_size,matrix_size), dtype=np.longlong) # Gera matriz1 com numeros aleatorios de 0 a 10001
matriz2_strassen = np.random.randint(0,valor_maximo, size=(matrix_size,matrix_size), dtype=np.longlong) # Gera matriz2 com numeros aleatorios de 0 a 10001
resultado_strassen = np.random.randint(0,1, size=(matrix_size,matrix_size), dtype=np.longlong) #Gera matriz resultado inicialmente com valores 0

  
def soma_matriz(matriz1,matriz2):
    print(matriz1)
    print("\n")
    print(matriz2)
    print("\n")
    return matriz1 + matriz2

def subtrai_matriz(matriz1,matriz2):
    print(matriz1)
    print("\n")
    print(matriz2)
    print("\n")
    return matriz1 - matriz2

def divide_matriz(matriz,matrix_size):
    if len(matriz) % 2 != 0 or len(matriz[0]) % 2 != 0:
        raise Exception("Somente matrizes pares")

    tamanho = len(matriz)
    meio = tamanho//2  
    topo_esquerdo = [matriz[linha][coluna] for linha in range(meio) for coluna in range(meio)] 
    base_esquerdo = [matriz[linha][coluna] for linha in range(meio) for coluna in range(meio, tamanho)] 
    topo_direito  = [matriz[linha][coluna] for linha in range(meio,tamanho) for coluna in range(meio)]  
    base_direito  = [matriz[linha][coluna] for linha in range(meio,tamanho) for coluna in range(meio,tamanho)]

    te = np.reshape(topo_esquerdo,(-1,matrix_size//2))
    be = np.reshape(base_esquerdo,(-1,matrix_size//2))
    td = np.reshape(topo_direito,(-1,matrix_size//2))
    bd = np.reshape(base_direito,(-1,matrix_size//2))

    return te,be,td,bd

# print(soma_matriz(matriz1_strassen,matriz2_strassen))   
# print(subtrai_matriz(matriz1_strassen,matriz2_strassen))

print(matriz1_strassen)
print("\n")
a,b,c,d = divide_matriz(matriz1_strassen,matrix_size)

print(a)
print("\n")
print(b)
print("\n")
print(c)
print("\n")
print(d)

