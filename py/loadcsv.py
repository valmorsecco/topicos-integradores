import sys
import pandas as pd
import numpy as np
from numpy import linalg as LA

#Número de termos
numterm = int(sys.argv[1])
numtermld = 0

#Matriz original .csv
df = pd.read_csv(sys.argv[2])

#Matriz de correlação
cor = df.corr()

#Autovalores e Autovetores
autval, autvet = LA.eig(cor)
autvet = np.transpose(autvet)
autvalsort = np.sort(autval)[::-1]
autovalsortr = np.zeros((numterm, numterm))
autvetsort = []
autvalsize = autval.size

#Variância explicada
varexp = 0
while numtermld < numterm:
    varexp = varexp + autvalsort[numtermld]
    autvetsort.append(autvet[np.where(autval == autvalsort[numtermld])[0][0]])
    autovalsortr[numtermld][numtermld] = autvalsort[numtermld] ** (1/2)
    numtermld = numtermld + 1

varexp = varexp / autvalsize
autvetsort = np.array(autvetsort)

#Matriz de carregamentos (pesos)
matcar = np.matmul(autovalsortr, autvetsort)

#Comunalidades e variâncias
i = 0
while i < len(matcar):
    j = 0
    while j < len(matcar[i]):        
        print(matcar[i][j])
        j = j + 1
    i = i + 1

exit(0)

#Iniciando console
print('\n')
print('Algoritmo para ajuste de matrizes iniciado:')
print('Tecnologias: API NodeJS & Python.')
print('Disciplina: Tópicos integradores.')
print('Acadêmicos: Diago Piccoli - Valmor Secco')
print('Número de termos: ' + str(numterm))
print('\n')

#1: Matriz original
print('1: Matriz original')
print(df)
print('\n')

#2: Matriz correlação
print('2: Matriz correlação')
print(cor)
print('\n')

#3: Autovalores
print('3: Autovalores')
print(autval)
print('\n')

#4: Autovetores
print('4: Autovetores')
print(autvet)
print('\n')

#5: Variância explicada
print('5: Variância explicada')
print(varexp)
print('\n')

#6: Matriz de carregamentos (pesos)
print('6: Matriz de carregamentos (pesos)')
print('Matriz estimada de autovetores')
print(autvetsort)
print('\n')
print('Matriz diagonal da raiz')
print(autovalsortr)
print('\n')
print('Matriz estimada de carregamentos')
print(matcar)
print('\n')
