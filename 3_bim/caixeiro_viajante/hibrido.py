from random import randrange
from guloso import itemGuloso
from aleatorio import itemAleatorio
from utils import funcao_objetivo

def hibrido(matriz_distancias, cidades):
    solucao = []
    cidades_copia = cidades.copy()
    delta = 70

    # Seleciona a cidade de partida
    itemAleatorio(cidades_copia, solucao)

    while len(cidades_copia) > 0:
        # Sorteia a probabilidade de selecionar o método guloso ou aleatorio.
        valor_aleatorio = randrange(100)

        if delta > valor_aleatorio:
            #-------
            #. Metodo Guloso
            #-------
            itemGuloso(matriz_distancias, cidades, cidades_copia, solucao)
        else:
            #-------
            #. Metodo Aleatório
            #-------
            itemAleatorio(cidades_copia, solucao)

    return solucao, funcao_objetivo(matriz_distancias, solucao)