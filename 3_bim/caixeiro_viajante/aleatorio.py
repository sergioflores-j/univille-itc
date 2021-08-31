from random import randrange
from utils import funcao_objetivo

def itemAleatorio(cidades, solucao): 
    indice = randrange(len(cidades))
    cidade_sorteada = cidades[indice]
    del cidades[indice]
    solucao.append(cidade_sorteada)

def aleatorio(matriz_distancias, cidades): 
    solucao = []
    cidades_copia = cidades.copy()
    
    while len(cidades_copia) > 0:
        itemAleatorio(cidades_copia, solucao)

    return solucao, funcao_objetivo(matriz_distancias, solucao)
