import csv

def funcao_objetivo(lucro_dos_objetos, peso_dos_objetos, tamanho_da_mochila, penalidade, solucao):
  fitness = 0
  peso = 0
  for i in range(len(solucao)):
    fitness = fitness + (solucao[i] * lucro_dos_objetos[i])
    peso = peso + (solucao[i] * peso_dos_objetos[i])
  
  if (peso > tamanho_da_mochila):
    fitness = fitness - penalidade

  return fitness

# TODO
def writeResult(cidades, execucao, filename, resultRow):
  filepath = 'results/{0}-{1}.txt'.format(execucao, filename)
  print('writing - ', filepath)

  with open(filepath, 'w', newline='', encoding='utf-8') as f:
    results = []
    for i in resultRow[0]:
      results.append(cidades[i])

    row = (results, resultRow[1])
    f.write(str(row))

# TODO
def writeTimeResult(execucao, filename, data):
  filepath = 'results/{0}-{1}.txt'.format(execucao, filename)
  print('writing - ', filepath)

  with open(filepath, 'w', newline='', encoding='utf-8') as f:
    f.write(str(data))


def getData(rows):
  lucro_dos_objetos = []
  peso_dos_objetos = []
  tamanho_da_mochila = 0
  
  for i in range(1, len(rows)):
    row = rows[i]

    [c,w,p,s] = row
    tamanho_da_mochila = c

    peso_dos_objetos.append(w)
    lucro_dos_objetos.append(p)

  return lucro_dos_objetos, peso_dos_objetos, tamanho_da_mochila

def start(i):
  filepath = 'input{0}.csv'.format(i)

  with open(filepath, newline='', encoding='utf-8') as inputFile:
    reader = csv.reader(inputFile)
    rows = []
    for row in reader:
      rows.append(row)

    return getData(rows)