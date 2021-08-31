import csv
from aleatorio import aleatorio
from hibrido import hibrido
from guloso import guloso

def write(execucao, filename, rows):
    filepath = 'results/{0}-{1}.txt'.format(execucao, filename)
    print('writing - ', filepath)

    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        f.write(str(rows))

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
        res = aleatorio(matriz_distancias, cidadesindex)
        print("aleatorio - res:", res)
        write(execucao, 'result-aleatorio', res)

        res = guloso(matriz_distancias, cidadesindex)
        print("guloso - res:", res)
        write(execucao, 'result-guloso', res)

        res = hibrido(matriz_distancias, cidadesindex)
        print("hibrido - res:", res)
        write(execucao, 'result-hibrido', res)


if __name__ == "__main__":
    print('starting')
    main()
