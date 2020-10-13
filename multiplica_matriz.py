import numpy as np
from time import sleep, time




def multiplica_matriz():
    print("Entre com o numero de testes: ")
    numero_testes = int(input())
    print("Entre com o tamanho da matriz(N x N): ")
    tamanho_matriz_input = int(input())
    contador = 1
    start = time()
    while contador <= numero_testes:
        start_parcial = time()
        matriz_tamanho = tamanho_matriz_input
        valor_maximo = 10000

        #GERA MATRIZES ALEATORIAS DE TAMANHO = matriz_size
        matriz1 = np.random.randint(0,valor_maximo, size=(matriz_tamanho,matriz_tamanho), dtype=np.longlong) # Gera matriz1 com numeros aleatorios de 0 a 10001
        matriz2 = np.random.randint(0,valor_maximo, size=(matriz_tamanho,matriz_tamanho), dtype=np.longlong) # Gera matriz2 com numeros aleatorios de 0 a 10001
        resultado = np.random.randint(0,1, size=(matriz_tamanho,matriz_tamanho), dtype=np.longlong) #Gera matriz resultado inicialmente com valores 0 

        print("matriz=\n", matriz1) 
        print("\n")
        print("matriz2=\n", matriz2) 
        print("\n")
        #print("resultado\n", resultado)
        #print("\n")

        #MULTIPLICA AS MATRIZES PELO METODO TRADICIONAL
        for index in range(len(matriz1)): 
            for index2 in range(len(matriz2[0])): 
                for index3 in range(len(matriz2)):
                    resultado[index][index2] += matriz1[index][index3] * matriz2[index3][index2]

        end_parcial = time()
        tempo_parcial = end_parcial - start_parcial
        print('tempo parcial em segundos:', tempo_parcial)
        print("resultado=")
        print(resultado)
        contador += 1
    end = time()
    tempo = end - start
    print('tempo total de execução em segundos:',tempo)
    print('tempo medio de execução em segundos:', tempo/numero_testes)

    
    

def main():
    multiplica_matriz()


if __name__ == "__main__":
    main()
