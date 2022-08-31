import os
import sys
import random
from mpi4py import MPI



os.system('clear')

#conexão com mpi
comm = MPI.COMM_WORLD
# pega nucleo atual
rank = comm.Get_rank()

# pega do for no script de 10 a 22
TAMANHO_MEDICAO = int(sys.argv[1])
# pega quantidade de nucleos setados no script
TAMANHO_CORE = comm.Get_size()

# dentre os valores aleatorios , acha a soma que da 10
soma_usuario = 10 
# gera os valores aleatorios
medicao = []
if rank == 0: # calcula valor da soma e passa para os outros cores
    medicao = random.sample(range(1, TAMANHO_MEDICAO+1), TAMANHO_MEDICAO) 
    for i in range(1, TAMANHO_CORE):
      # comando para envio
        comm.send(medicao, i)
      # em algum momento ele não está no nucleo 0 e recebe a msg, especificar o core 0
else:
    medicao = comm.recv(source=0)

combinacoes0 = []
# formula para pegar o inicio e fim de cada sessão(intervalo do valor), para dividir o numero de combinações entre os cores
for i in range(int(rank*(((2**TAMANHO_MEDICAO)/TAMANHO_CORE)+1)), int((rank+1)*((2**TAMANHO_MEDICAO)/TAMANHO_CORE))):
    # pega o intervalor do valor , converte para binario e adciona a lista e adciona o numero de 0 a esquerda de acordo com o tamanho da medição(ficar no intervalor)
    x = bin(i)  
    combinacoes0.append(x.split('b')[1].zfill(TAMANHO_MEDICAO))


# lista dos resultados
resultato_fatores = []
# for na lista das combinações, para pegar uma posição da lista
for l in combinacoes0:
    soma = 0
    # converte essa posição para uma lista
    fatores = list(l)
    # percorrer a lista que foi convertida 
    for pos in range(0, len(l)):
        # soma pela posição do fator e da medição
        soma += int(fatores[pos]) * int(medicao[pos])
        # se soma for igual a soma usuario, ele adciona essa soma na lista de fatores(meu resultado)
    if soma == soma_usuario:
        resultato_fatores.append(fatores)


if rank != 0:       
   # envia todos resultados para posição 0
    comm.send(resultato_fatores, 0)        
   # se tiver na posição 0, recebe de todos os cores menos ele mesmo
else:
    for i in range(0, TAMANHO_CORE -1):
        resultato_fatores.append(comm.recv())
    
    
