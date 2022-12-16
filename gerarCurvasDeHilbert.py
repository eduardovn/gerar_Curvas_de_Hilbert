from ntpath import join
import numpy as np
from collections import Counter
from itertools import chain
from hilbertcurve.hilbertcurve import HilbertCurve
from matplotlib import pyplot as plt






def removerColchetes(lista):
    novaLista = []
    novaLista = [ele for sublist in lista for ele in sublist]
    return novaLista
   
    
def defineLinhasColunasMatriz(lista):
    listaPosicoesXY = []
    eixoX = [i[0] for i in lista]
    eixoY = [i[1] for i in lista]
    
    listaX = sorted(eixoX, key = lambda x:float(x))
    listaY = sorted(eixoY, key = lambda y:float(y))

    dicionarioX = {}
    dicionarioX = Counter(listaX)
    indiceX = max(dicionarioX.keys(), key=(lambda i: dicionarioX[i]))

    tamanhoColuna = dicionarioX[indiceX]
    listaPosicoesXY.append(tamanhoColuna-1)

    dicionarioY = {}
    dicionarioY = Counter(listaY)
    
    indiceY = max(dicionarioY.keys(), key=(lambda j: dicionarioY[j]))
    
    tamanhoLinha = dicionarioY[indiceY]
    listaPosicoesXY.append(tamanhoLinha)

    return listaPosicoesXY 



def converterListaParaDicionario(lista):
    dicionario = {lista[i]: lista[i + 1] for i in range(0, len(lista), 2)}
    return dicionario


def organizarListaEmCurvasDeHilbert(listaOrdenada, listaOrgCurvaHilbert):
    novaLista = []

    dicionario = dict(zip(listaOrgCurvaHilbert, listaOrdenada))
    #print("dicionario : ",dicionario)
    #print("dicionario key",dicionario.keys())
    #print("dicionario values",dicionario.values())
    novaLista = list(dicionario.values())
    #print("novaLista: ",novaLista)

    return novaLista
    

def gerarCurvaHilbert(linha, coluna, matriz):
    matriz = np.array(matriz)
    p = 4
    N = 2
   
    hilbert_curve = HilbertCurve(p, N)
    indexes = np.zeros((linha*coluna,N), dtype='int')
  
  
    for i in range(linha*coluna):
        coords = hilbert_curve.point_from_distance(i)
        indexes[i,:] = coords

 
    lista = [matriz[x,y] for x,y in indexes]

    return lista


def gerarMatriz(linhas, colunas):
    matriz = []
    
    contador = 0
    for i in range(linhas):
        row = []
        for j in range(colunas):
             
            row.append(contador)
            contador = contador + 1
        matriz.append(row)

    return matriz


if __name__=="__main__":
    ##############################################################
    lista =  [(24.0, 30.0), (53.0, 5.0), (35.6, 30.0), (29.8, 25.0), (47.2, 0.0), 
                (53.0, 20.0), (29.8, 40.0), (47.2, 15.0), (58.0, 10.0), (24.0, 15.0),
                (53.0, 35.0), (58.0, 25.0), (41.4, 10.0), (29.8, 0.0), (24.0, 5.0), 
                (47.2, 30.0), (19.0, 15.0), (41.4, 25.0), (35.6, 5.0), (19.0, 30.0), 
                (35.6, 20.0), (24.0, 20.0), (29.8, 15.0), (41.4, 40.0), (24.0, 35.0), 
                (53.0, 10.0), (35.6, 35.0), (29.8, 30.0), (47.2, 5.0), (53.0, 25.0), 
                (41.4, 0.0), (47.2, 20.0), (58.0, 15.0), (53.0, 40.0), (58.0, 30.0), 
                (47.2, 40.0), (41.4, 15.0), (24.0, 10.0), (29.8, 5.0), (47.2, 35.0), 
                (19.0, 20.0), (41.4, 30.0), (24.0, 25.0), (35.6, 10.0), (53.0, 0.0), 
                (35.6, 25.0), (29.8, 20.0), (63.0, 20.0), (29.8, 35.0), (24.0, 40.0), 
                (53.0, 15.0), (35.6, 40.0), (53.0, 30.0), (47.2, 10.0), (58.0, 20.0), 
                (14.0, 20.0), (41.4, 5.0), (24.0, 0.0), (47.2, 25.0), (19.0, 10.0), 
                (41.4, 20.0), (35.6, 0.0), (19.0, 25.0), (35.6, 15.0), (29.8, 10.0), 
                (41.4, 35.0)]
    ##############################################################
    listaOrdenada = []
    listaOrdenada = sorted(lista,key=lambda l:(l[0],l[1]))
    #print("listaOrdenada 1: ",listaOrdenada)
    #print("===============================")
    primeiroElemento = listaOrdenada[0]
    ultimoElemento = listaOrdenada[-1]
    listaOrdenada.pop(0)
    listaOrdenada.pop()

    #print("listaOrdenada 2: ",listaOrdenada) 
    #print("tam: ",len(listaOrdenada))
    
    listaPosicoesXY = defineLinhasColunasMatriz(listaOrdenada)

    colunas = listaPosicoesXY[0]
    linhas = listaPosicoesXY[1]
    intervalo = 5

    
    listaOrgCurvaHilbert = []
    listaDePontosHexagono = []
    
    matrizBase = gerarMatriz(linhas, colunas)   
    listaOrgCurvaHilbert = gerarCurvaHilbert( linhas, colunas, matrizBase)    
    #print("listaOrdenada tam: ",len(listaOrgCurvaHilbert))
    #print("listaOrdenada: ",listaOrgCurvaHilbert)
    
    listaDePontosHexagono = organizarListaEmCurvasDeHilbert(listaOrdenada, listaOrgCurvaHilbert)
    #print("listaDePontosHexagono tam: ",len(listaDePontosHexagono))
    print("listaDePontosHexagono: ",listaDePontosHexagono)
    
   