import csv
import time
from datetime import timedelta
from aleatorio import aleatorio
from hibrido import hibrido
from guloso import guloso

def writeResult(cidades, execucao, filename, resultRow):
    filepath = 'results/{0}-{1}.txt'.format(execucao, filename)
    print('writing - ', filepath)

    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        results = []
        for i in resultRow[0]: 
            results.append(cidades[i])

        row = (results, resultRow[1])
        f.write(str(row))

def writeTimeResult(execucao, filename, data):
    filepath = 'results/{0}-{1}.txt'.format(execucao, filename)
    print('writing - ', filepath)

    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        f.write(str(data))

def getData(rows):
    header = rows[0]
    cidades = []
    matriz_distancias = []

    for i in range(1, len(rows)):
        row = rows[i]

        cidade = row[0]
        cidades.append(cidade)

        distancias = row.copy()
        distancias.pop(0)
        for j in range(len(distancias)):
            distancias[j] = int(distancias[j] if distancias[j] else 0)

        matriz_distancias.append(distancias)
    
    return cidades, matriz_distancias

def start():
    with open('input.csv', newline='', encoding='utf-8') as inputFile:
        reader = csv.reader(inputFile)
        rows = []
        for row in reader:
            rows.append(row)

        return getData(rows)

def main():
    # Test cases
    # matriz_distancias = [[0,1,3,2],[1,0,4,3],[3,4,0,2],[2,3,1,0]]
    # cidadesindex = [0,1,2,3]
    # execucoes = 1

    execucoes = 30
    cidades, matriz_distancias = start()
    cidadesindex = []
    for i in range(len(cidades)):
        cidadesindex.append(i)

    for execucao in range(execucoes):
        aleatorio_start_time = time.time()
        res = aleatorio(matriz_distancias, cidadesindex)
        print("aleatorio - res:", res)
        writeResult(cidades, execucao, 'result-aleatorio', res)
        writeTimeResult(execucao, 'result-aleatorio-time', time.time() - aleatorio_start_time)

        guloso_start_time = time.time()
        res = guloso(matriz_distancias, cidadesindex)
        print("guloso - res:", res)
        writeResult(cidades, execucao, 'result-guloso', res)
        writeTimeResult(execucao, 'result-guloso-time', time.time() - guloso_start_time)

        hibrido_start_time = time.time()
        res = hibrido(matriz_distancias, cidadesindex)
        print("hibrido - res:", res)
        writeResult(cidades, execucao, 'result-hibrido', res)
        writeTimeResult(execucao, 'result-hibrido-time', time.time() - hibrido_start_time)


if __name__ == "__main__":
    print('starting')
    program_start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - program_start_time))
