import numpy as np 
import sys
from time import sleep, time
sys.setrecursionlimit(90000000)

  
def soma_matriz(matriz1,matriz2):
    return matriz1 + matriz2

def subtrai_matriz(matriz1,matriz2):
    return matriz1 - matriz2

def divide_matriz(matriz):
    if len(matriz) % 2 != 0 or len(matriz[0]) % 2 != 0:
        raise Exception("Somente matrizes pares")

    tamanho = len(matriz)
    meio = tamanho//2  
    topo_esquerdo = [matriz[linha][coluna] for linha in range(meio) for coluna in range(meio)] 
    base_esquerdo = [matriz[linha][coluna] for linha in range(meio) for coluna in range(meio, tamanho)] 
    topo_direito  = [matriz[linha][coluna] for linha in range(meio,tamanho) for coluna in range(meio)]  
    base_direito  = [matriz[linha][coluna] for linha in range(meio,tamanho) for coluna in range(meio,tamanho)]

    te = np.reshape(topo_esquerdo,(-1,tamanho//2))
    be = np.reshape(base_esquerdo,(-1,tamanho//2))
    td = np.reshape(topo_direito,(-1,tamanho//2))
    bd = np.reshape(base_direito,(-1,tamanho//2))

    return te,be,td,bd

def tamanho_matriz(matriz):
    return len(matriz),len(matriz[0])

def multiplica_strassen(matriz1,matriz2):
    
    #caso base matriz 2x2 
    if tamanho_matriz(matriz1) == (2,2):
        return np.matmul(matriz1,matriz2)

    #divide as matrizes em submatrizes de tamanho = matriz_tamanho//2
    A, B, C, D = divide_matriz(matriz1)
    E, F, G, H = divide_matriz(matriz2)

    #recurisavemente calcula os 7 passos do algoritimo de strassen
    p1 = multiplica_strassen(A, subtrai_matriz(F, H))
    p2 = multiplica_strassen(soma_matriz(A, B), H)
    p3 = multiplica_strassen(soma_matriz(C, D), E)
    p4 = multiplica_strassen(D, subtrai_matriz(G, E))
    p5 = multiplica_strassen(soma_matriz(A, D), soma_matriz(E, H))
    p6 = multiplica_strassen(subtrai_matriz(B, D), soma_matriz(G, H))
    p7 = multiplica_strassen(subtrai_matriz(A, C), soma_matriz(E, F))

    #resultado das 4 submatrizes finais
    topo_esquerdo = soma_matriz(subtrai_matriz(soma_matriz(p5, p4), p2), p6)
    topo_direito = soma_matriz(p1, p2)
    base_esquerda = soma_matriz(p3, p4)
    base_direita = subtrai_matriz(subtrai_matriz(soma_matriz(p1, p5), p3), p7)

    #junta as 4 submatrizes numa matriz final
    matriz_final = np.vstack((np.hstack((topo_esquerdo, topo_direito)), np.hstack((base_esquerda, base_direita)))) 
    return matriz_final

def rodar():
    print("Entre com o numero de testes: ")
    numero_testes = int(input())
    print("Entre com o tamanho da matriz(N x N): ")
    tamanho_matriz_input = int(input())
    contador = 1

    start = time()
    while contador <= numero_testes:
        start_parcial = time()
        matriz_tamanho = tamanho_matriz_input
        valor_maximo = 10001
        matriz1_strassen = np.random.randint(0,valor_maximo, size=(matriz_tamanho,matriz_tamanho), dtype=np.longlong) # Gera matriz1 com numeros aleatorios de 0 a 10001
        matriz2_strassen = np.random.randint(0,valor_maximo, size=(matriz_tamanho,matriz_tamanho), dtype=np.longlong) # Gera matriz2 com numeros aleatorios de 0 a 10001
        print("matriz=\n", matriz1_strassen) 
        print("\n")
        print("matriz2=\n", matriz2_strassen) 
        print("\n")
        multiplica = multiplica_strassen(matriz1_strassen,matriz2_strassen)
        print(multiplica)
        end_parcial = time()
        tempo_parcial = end_parcial - start_parcial
        contador+=1
        print('tempo parcial em segundos:', tempo_parcial)
        
    end = time()
    tempo = end - start
    print('tempo total de execução em segundos:',tempo)
    print('tempo medio de execução em segundos:', tempo/numero_testes)

def main():
    rodar()


if __name__ == "__main__":
    main()



