import sys
import pandas as pd
import numpy as np
from numpy import linalg as LA
import statistics

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
autvalsize = len(autval)

#Variância explicada
varexp = 0
while numtermld < numterm:
    varexp = varexp + autvalsort[numtermld]
    autvetsort.append(autvet[np.where(autval == autvalsort[numtermld])[0][0]])
    autovalsortr[numtermld][numtermld] = autvalsort[numtermld] ** (1/2)
    numtermld = numtermld + 1

varexp = varexp / autvalsize
autvetsort = np.transpose(np.array(autvetsort))

#Matriz de carregamentos (pesos)
matcar = np.matmul(autvetsort, autovalsortr)

#Comunalidades e variâncias
arrcmaux = []
i = 0
while i < len(matcar):
    j = 0
    vl = 0
    while j < len(matcar[i]):
        vl = vl + matcar[i][j] ** 2
        j = j +1
        if(j == len(matcar[i])):
            arrcmaux.append(vl)
    i = i + 1

#Variância expecífica
arrcmauxexp = []
for item in arrcmaux:
    arrcmauxexp.append(1 - item)

#Coeficiente dos escores fatoriais
matcart = np.transpose(matcar)
matcartne = LA.inv(np.matmul(matcart, matcar))
coefef = np.matmul(matcartne, matcart)

#Escores fatoriais
z = np.array(df)
medias = []
dp = []
idx = 0
while idx < len(np.array(df)[0]):
    medias.append(0)
    dp.append([])
    idxy = 0
    for item in np.array(df):
        medias[idx] = medias[idx] + item[idx]
        dp[idx].append(item[idx])
        idxy = idxy + 1
    medias[idx] = medias[idx] / idxy
    idx = idx + 1

idxdp = 0
for item in dp:
    dp[idxdp] = statistics.stdev(item)
    idxdp = idxdp + 1

idx2 = 0
zaux = np.array(z, dtype=np.float64)
while idx2 < len(z[0]):
    idx3 = 0
    for item in z:
        auxz = z[idx3][idx2]
        auxm = medias[idx2]
        auxd = dp[idx2]
        zaux[idx3][idx2] = ((auxz - auxm) / auxd)
        idx3 = idx3 + 1
    idx2 = idx2 + 1

z = zaux
zt = np.transpose(z)
czt = np.transpose(np.matmul(coefef, zt))

somaAux = []
somaAuxMostra = []

idxf = 0
for item in czt:
    idxi = 0
    idxij = 0
    somaAux.append(0)
    while idxi < len(item):
        idxij = idxij + autval[idxi]
        somaAux[idxf] = somaAux[idxf] + (item[idxi] * autval[idxi])
        idxi = idxi + 1
    somaAux[idxf] = somaAux[idxf] / autval.sum()
    somaAuxMostra.append([(idxf + 1), somaAux[idxf]])
    idxf = idxf + 1

somaAux = np.array(somaAux)
somaAuxMostra = np.array(somaAuxMostra)
somaAuxMostra = somaAuxMostra[somaAuxMostra[:,1].argsort(kind='mergesort')]

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

#7: Comunalidades e variâncias
print('7: Comunalidades e variâncias')
i7 = 0
for item in arrcmaux:
    i7 = i7 + 1
    print('h' + str(i7) + ' ' + str(item))
print('\n')

#8: Variância expecífica
print('8: Variância expecífica')
for item in arrcmauxexp:
    print(item)
print('\n')

#9: Coeficiente dos escores fatoriais
print('9: Coeficiente dos escores fatoriais')
print(coefef)
print('\n')

#10: Escores fatoriais
print('10: Escores fatoriais')
print('Médias')
print(medias)
print('\n')
print('Desvio padrão')
print(dp)
print('\n')
print('Z')
print(z)
print('\n')
print('Z Transposto')
print(zt)
print('\n')
print('(Z Transposto * coefef) transposto')
print(czt)
print('\n')
print('Escore final ponderado')
print(somaAuxMostra)
print('Escore final ordenado')
for item in reversed(somaAuxMostra):
    print(item)
print('\n')
