import csv 
from ast import literal_eval as make_tuple

algos = ['aleatorio', 'hibrido', 'guloso']
execucoes = 30

def getResults():
    data = [None] * len(algos)

    for i in range(execucoes):
        for algoIndex in range(len(algos)):
            algo = algos[algoIndex]
            
            if not data[algoIndex]:
                data[algoIndex] = []

            filepath ='results/{0}-result-{1}.txt'.format(i, algo)
            print('filepath', filepath)

            with open(filepath, newline='', encoding='utf-8') as resFile:
                for row in resFile:
                    if row:
                        data[algoIndex].append(make_tuple(row))

    return data

        
def write(filename, rows):
    filepath = 'results/{0}.csv'.format(filename)
    print('writing - ', filepath)

    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

def obter_resultados():
    data = getResults()

    rows = [algos]
    for i in range(execucoes):
        rows.append([None] * len(algos))

    for algoIndex in range(len(algos)):
        for resultIndex in range(len(data[algoIndex])):
            
            solucao, distancia = data[algoIndex][resultIndex]

            rows[resultIndex + 1][algoIndex] = distancia

    write('final-result', rows)
    print(rows)


if __name__ == "__main__":
    print('starting')
    obter_resultados()
