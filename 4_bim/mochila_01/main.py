# coding=utf-8

import csv
import time
from datetime import timedelta
from utils import funcao_objetivo,start
import random

def gerar_solucao_inicial(tamanho_da_solucao, tamanho_da_populacao, populacao):
	for i in range(tamanho_da_populacao):
		for j in range(tamanho_da_solucao):
			populacao[i][j] = random.randint(0, 1)


def avaliar_solucao(lucro_dos_objetos, peso_dos_objetos, tamanho_da_mochila, penalidade, fitness, populacao, indice):
	fitness[indice] = funcao_objetivo(lucro_dos_objetos, peso_dos_objetos, tamanho_da_mochila, penalidade, populacao[indice])


def avaliar_populacao(lucro_dos_objetos, peso_dos_objetos, tamanho_da_mochila, penalidade, fitness, populacao, tamanho_da_populacao):
	for i in range(tamanho_da_populacao):
		avaliar_solucao(lucro_dos_objetos, peso_dos_objetos, tamanho_da_mochila, penalidade, fitness, populacao, i)


def identificar_melhor_solucao(fitness, tamanho_da_populacao):
	tamanho_do_torneio = 3

	indice_melhor_solucao = random.randint(0, tamanho_da_populacao - 1)

	for i in range(tamanho_do_torneio - 1):
		indice_da_solucao_candidata = indice_melhor_solucao
		
		while ( indice_da_solucao_candidata == indice_melhor_solucao ):
			indice_da_solucao_candidata = random.randint(0, tamanho_da_populacao - 1)

		if fitness[indice_da_solucao_candidata] > fitness[indice_melhor_solucao]:
			indice_melhor_solucao = indice_da_solucao_candidata

	print("Solucao que venceu o torneio indice ", indice_melhor_solucao, "com o fitness ", fitness[indice_melhor_solucao])

	return indice_melhor_solucao

def elitismo(tamanho_da_populacao, populacao, fitness, fitness_proxima_populacao, proxima_populacao):
	indice_da_melhor_solucao = identificar_melhor_solucao(fitness, tamanho_da_populacao)
	proxima_populacao[tamanho_da_populacao] = populacao[indice_da_melhor_solucao]
	fitness_proxima_populacao[tamanho_da_populacao] = fitness[indice_da_melhor_solucao]

	return indice_da_melhor_solucao

def cruzamento(tamanho_da_solucao, populacao, fitness, proxima_populacao, tamanho_da_populacao):
	# pegar da população inicial 2 individuos com maior fitness
	# cruzar esses individuos
	# colocar a proxima população os dois novos individuos gerados
	fitness_populacao = fitness.copy()
	indice_solucao_a = identificar_melhor_solucao(fitness_populacao, tamanho_da_populacao)

	fitness_populacao[indice_solucao_a] = 0
	indice_solucao_b = identificar_melhor_solucao(fitness_populacao, tamanho_da_populacao)

	solucao_a = populacao[indice_solucao_a]
	solucao_b = populacao[indice_solucao_b]
		
	ponto_de_corte = random.randint(0, tamanho_da_solucao - 1)
	print('Ponto de Corte:', ponto_de_corte)

	nova_solucao_a = []
	nova_solucao_b = []

	for i in range(tamanho_da_solucao):
		if i <= ponto_de_corte:
			nova_solucao_a.append(solucao_a[i])
			nova_solucao_b.append(solucao_b[i])
		else:
			nova_solucao_b.append(solucao_a[i])
			nova_solucao_a.append(solucao_b[i])

	proxima_populacao = populacao.copy()
	proxima_populacao[indice_solucao_a] = nova_solucao_a
	proxima_populacao[indice_solucao_b] = nova_solucao_b

def identificar_pior_solucao_da_proxima_populacao(tamanho_da_populacao, fitness_proxima_populacao):
	indice_da_pior_solucao = 0
	for i in range(tamanho_da_populacao+1):
		if fitness_proxima_populacao[indice_da_pior_solucao] > fitness_proxima_populacao[i]:
			indice_da_pior_solucao = i
	return indice_da_pior_solucao


def identificar_pior_solucao_da_populacao_atual(tamanho_da_populacao, fitness):
	indice_da_pior_solucao = 0
	for i in range(tamanho_da_populacao):
		if fitness[indice_da_pior_solucao] > fitness[i]:
			indice_da_pior_solucao = i
	return indice_da_pior_solucao


def gerar_proxima_populacao(proxima_populacao, fitness_proxima_populacao, tamanho_da_populacao):
	pior = identificar_pior_solucao_da_proxima_populacao(tamanho_da_populacao, fitness_proxima_populacao)
	del proxima_populacao[pior]
	del fitness_proxima_populacao[pior]

	populacao = proxima_populacao
	fitness = fitness_proxima_populacao

	proxima_populacao.append(proxima_populacao[0])
	fitness_proxima_populacao.append(fitness_proxima_populacao[0])

	return populacao, fitness


def criterio_de_parada_atingido(quantidade_atual_de_avaliacoes, quantidade_total_de_avaliacoes):
	return quantidade_atual_de_avaliacoes >= quantidade_total_de_avaliacoes


def relatorio_de_convergencia_da_geracao(fitness, melhor_fitness_da_geracao, media_fitness_da_geracao, pior_fitness_da_geracao, tamanho_da_populacao):
	melhor_fitness_da_geracao.append(fitness[identificar_melhor_solucao(fitness, tamanho_da_populacao)])
	pior_fitness_da_geracao.append(fitness[identificar_pior_solucao_da_populacao_atual(tamanho_da_populacao, fitness)])
	media = 0

	for i in fitness:
		media = media+i

	media_fitness_da_geracao.append(media/len(fitness))


def algoritmoPopulacional(lucro_dos_objetos, peso_dos_objetos, tamanho_da_mochila, penalidade):
	tamanho_da_solucao = len(lucro_dos_objetos)
	tamanho_da_populacao = 4
	quantidade_total_de_avaliacoes = 20
	quantidade_atual_de_avaliacoes = 0
	populacao = []
	proxima_populacao = []
	fitness = [0] * tamanho_da_populacao
	fitness_proxima_populacao = [0] * (tamanho_da_populacao + 1)
	indice_da_melhor_solucao = 0
	indice_da_pior_solucao = 0

	for i in range(tamanho_da_populacao):
		populacao.append([0] * tamanho_da_solucao)
		proxima_populacao.append([0] * tamanho_da_solucao)
	proxima_populacao.append([0] * tamanho_da_solucao)

	melhor_fitness_da_geracao = []
	media_fitness_da_geracao = []
	pior_fitness_da_geracao = []

	gerar_solucao_inicial(tamanho_da_solucao, tamanho_da_populacao, populacao)
	avaliar_populacao(lucro_dos_objetos, peso_dos_objetos, tamanho_da_mochila, penalidade, fitness, populacao, tamanho_da_populacao)
	quantidade_atual_de_avaliacoes = tamanho_da_populacao
	relatorio_de_convergencia_da_geracao(fitness, melhor_fitness_da_geracao, media_fitness_da_geracao, pior_fitness_da_geracao, tamanho_da_populacao)

	contador = 0
	while not criterio_de_parada_atingido(quantidade_atual_de_avaliacoes, quantidade_total_de_avaliacoes):
		indice_da_melhor_solucao = elitismo(tamanho_da_populacao, populacao, fitness, fitness_proxima_populacao, proxima_populacao)

		for i in range(tamanho_da_populacao):
			cruzamento(tamanho_da_solucao, populacao, fitness, proxima_populacao, tamanho_da_populacao)
			fitness_proxima_populacao[i] = funcao_objetivo(lucro_dos_objetos, peso_dos_objetos, tamanho_da_mochila, penalidade, proxima_populacao[i])

			quantidade_atual_de_avaliacoes = quantidade_atual_de_avaliacoes + 1

		populacao, fitness = gerar_proxima_populacao(proxima_populacao, fitness_proxima_populacao, tamanho_da_populacao)
		relatorio_de_convergencia_da_geracao(fitness, melhor_fitness_da_geracao, media_fitness_da_geracao, pior_fitness_da_geracao, tamanho_da_populacao)

		contador = contador + 1
	
	print("Melhor individuo")
	melhor_final = identificar_melhor_solucao(fitness, tamanho_da_populacao)
	print(populacao[melhor_final])
	print("Fitness =", fitness[melhor_final])

	# O valor de fitness ou aptidão define o qual bem a solução resolve o problema. 
	return fitness[melhor_final], melhor_fitness_da_geracao, media_fitness_da_geracao, pior_fitness_da_geracao

def gerarRelatorioFinal(outputs):
	filepath = 'results/final.csv'
	print('writing - ', filepath)
	rows = [["entrada", "execucao", "solucao"]]

	with open(filepath, 'w', newline='', encoding='utf-8') as f:
		for i in range(len(outputs)):
			resultados = outputs[i]

			for j in range(len(resultados)):
				result = resultados[j]
				solucao, melhor_fitness_da_geracao, media_fitness_da_geracao, pior_fitness_da_geracao = result
				
				rows.append((i+1, j+1, solucao))

		writer = csv.writer(f)
		writer.writerows(rows)

	print("result", resultados)

def main():
	# Test cases (comentar para utilizar os inputs)
	# execucoes = 1
	# lucro_dos_objetos = [5, 3, 2, 1, 4, 6, 3, 5, 1, 1, 2, 3, 5, 6, 8]
	# peso_dos_objetos = [6, 3, 5, 1, 1, 2, 3, 5, 6, 8, 4, 3, 3, 2, 1]
	# tamanho_da_mochila = 7
	
	# Constantes
	penalidade = 25
	execucoes = 30

	# Variaveis
	resultados_1 = []
	resultados_2 = []

	for execucao in range(execucoes):
		# PRIMEIRO INPUT
		lucro_dos_objetos, peso_dos_objetos, tamanho_da_mochila = start(1)
		print(lucro_dos_objetos, peso_dos_objetos, tamanho_da_mochila)
		res = algoritmoPopulacional(lucro_dos_objetos, peso_dos_objetos, tamanho_da_mochila, penalidade)
		resultados_1.append(res)

	gerarRelatorioFinal([resultados_1, resultados_2])

if __name__ == "__main__":
	print('starting')
	program_start_time = time.time()
	main()
	print("--- %s seconds ---" % (time.time() - program_start_time))
