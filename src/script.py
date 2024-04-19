import csv
from src.models.entrevistado_class import *

def input_de_dados(genero, idade, resposta_1, resposta_2, resposta_3, resposta_4, resposta_extra_1,resposta_extra_2):
    data = []
    try:
        if not all([genero, idade, resposta_1, resposta_2, resposta_3, resposta_4, resposta_extra_1,resposta_extra_2]):            
            return False
        entrevistado = Entrevistado(genero, idade, resposta_1, resposta_2, resposta_3, resposta_4,resposta_extra_1, resposta_extra_2)
        return entrevistado
    except Exception as e:
        print(f"Erro ao escrever dados: {e}")
        return False

def escrever_csv(data):
    nome_arquivo = 'resultado.csv'
    try:
        with open(nome_arquivo, mode='w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Genero', 'Idade', 'Resposta 1', 'Resposta 2', 'Resposta 3', 'Resposta 4', 'Resposta Extra1', 'Resposta Extra2', 'Data'])
            for entrevistado in data:
                writer.writerow(entrevistado)
        print(f'Dados foram escritos com sucesso no arquivo {nome_arquivo}.')
    except Exception as e:
        print(f"Erro ao escrever dados no arquivo CSV: {e}")

total_masculino = 0
total_feminino = 0
respostas = {
    'Resposta 1': {'SIM': 0, 'NÃO': 0, 'NÃO SEI': 0},
    'Resposta 2': {'SIM': 0, 'NÃO': 0, 'NÃO SEI': 0},
    'Resposta 3': {'SIM': 0, 'NÃO': 0, 'NÃO SEI': 0},
    'Resposta 4': {'SIM': 0, 'NÃO': 0, 'NÃO SEI': 0},
    'Resposta 5': {'SIM': 0, 'NÃO': 0, 'NÃO SEI': 0},
    'Resposta 6': {'SIM': 0, 'NÃO': 0, 'NÃO SEI': 0}
}


def contar_respostas(data):
    global total_masculino, total_feminino, respostas

    for resposta in data:
        genero = resposta[0]
        if genero == 'MASCULINO':
            total_masculino += 1
        elif genero == 'FEMININO':
            total_feminino += 1

        for i in range(2, len(resposta) - 1):
            if i > 7:
                continue
            resposta_pergunta = resposta[i]
            if resposta_pergunta in respostas[f'Resposta {i-1}']:
                respostas[f'Resposta {i-1}'][resposta_pergunta] += 1




