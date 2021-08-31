def funcao_objetivo(matriz_distancias, solucao):
    distancia = 0
    for i in range(0, len(solucao) - 1):
        distancia = distancia + matriz_distancias[solucao[i]][solucao[i + 1]]

    return distancia + matriz_distancias[solucao[len(solucao)-1]][solucao[0]]
