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

