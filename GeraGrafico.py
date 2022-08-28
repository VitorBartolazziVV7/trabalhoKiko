from cProfile import label
from xml.dom.minidom import TypeInfo
import matplotlib.pyplot as plt
import pandas as pd

dadosSCore = pd.read_csv('SigleCore.dat', sep=';', header=None)

dadosMultiCore = pd.read_csv('Paralelo.dat', sep=';', header=None)

listaDadosSCore = dadosSCore.values.tolist()
listadadosMultiCore = dadosMultiCore.values.tolist()

dados = []

for i in range(0, len(listaDadosSCore)):
    comp_temp = []
    comp = listaDadosSCore[i][1] / listadadosMultiCore[i][1]

    comp_temp.append(listaDadosSCore[i][0])
    comp_temp.append(round(comp, 2))
    dados.append(comp_temp)

compDataFrame = pd.DataFrame(dados, columns=[0, 1])

plt.subplot(1, 2, 1)
plt.plot(dadosSCore[0], dadosSCore[1], ls='-', lw='1', marker='o', label='SingleCore')
plt.plot(dadosMultiCore[0], dadosMultiCore[1], ls='-', lw='1', marker='o', label='MultiCore')
plt.title('Comparação de tempo SingleCore |----| MultiCore')
plt.grid()
plt.legend(loc="upper left")

plt.subplot(1, 2, 2)
plt.plot(compDataFrame[0], compDataFrame[1], ls='-', lw='1', marker='o', label='Relação das medidas')
plt.title('Diferença de Tempo')
plt.grid()
plt.legend(loc="upper left")
plt.show()