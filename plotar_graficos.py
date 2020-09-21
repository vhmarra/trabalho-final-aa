import matplotlib.pyplot as plt

tamanho_matriz = [32,64,128,256,512,1024]

tempo_padrao = [2.1295,8.6097,58.8896,452.0123,3841.1216,30436.9614]
tempo_strassen = [2.1407,8.6264,52.0659,458.141,2491.3155,17481.0806]

padrao = plt.plot(tamanho_matriz,tempo_padrao,label='padrao')
strassen = plt.plot(tamanho_matriz,tempo_strassen,label='strassen')
plt.title('Trabalho Final AA')
plt.ylabel('Tempo em segundos')
plt.xlabel('Tamanho da matriz')
plt.show()