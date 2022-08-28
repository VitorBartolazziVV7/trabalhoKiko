import os
import random
import sys

os.system('clear')


TAMANHO_MEDICAO = int(sys.argv[1])

combinacoes = []
tam_medicoes = TAMANHO_MEDICAO 
print('\nCombinações: ')
for i in range(0, 2**tam_medicoes):
  x = bin(i)
  combinacoes.append(x.split('b')[1].zfill(tam_medicoes))

soma_usuario = 10
medicao = random.sample(range(1, TAMANHO_MEDICAO+1), TAMANHO_MEDICAO)

total = 0
for l in combinacoes:
  soma = 0
  fatores = list(l)
  for pos in range(0, len(l)):
    soma += int(fatores[pos]) * int(medicao[pos])
  if soma == soma_usuario:
    total += 1
 