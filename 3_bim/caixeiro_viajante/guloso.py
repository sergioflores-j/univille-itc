from random import randrange
from aleatorio import itemAleatorio
from utils import funcao_objetivo

def itemGuloso(matriz_distancias, cidades, cidades_copia, solucao):
    partida = cidades[solucao[len(solucao)-1]]
    proxima = cidades_copia[0]
    proxima_indice = 0
    menor_distancia = matriz_distancias[partida][proxima]

    i = 0
    for proxima_cidade_candidata in cidades_copia:
        distancia = matriz_distancias[partida][proxima_cidade_candidata]
        if distancia < menor_distancia:
            menor_distancia = distancia
            proxima = proxima_cidade_candidata
            proxima_indice = i
        i = i + 1
    
    solucao.append(cidades_copia[proxima_indice])
    del cidades_copia[proxima_indice]

def guloso(matriz_distancias, cidades):
    solucao = []
    cidades_copia = cidades.copy()

    # Seleciona a cidade de partida
    itemAleatorio(cidades_copia, solucao)

    while len(cidades_copia) > 0:
        itemGuloso(matriz_distancias, cidades, cidades_copia, solucao)

    return solucao, funcao_objetivo(matriz_distancias, solucao)