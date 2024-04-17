import csv
from src.models.entrevistado_class import *

def input_de_dados(genero, idade, resposta_1, resposta_2, resposta_3, resposta_4):
    data = []
    try:
        if not all([genero, idade, resposta_1, resposta_2, resposta_3, resposta_4]):            
            return False
        entrevistado = Entrevistado(genero, idade, resposta_1, resposta_2, resposta_3, resposta_4)
        return entrevistado
    except:
        print("Erro ao adicionar dados:")
        return False

def escrever_csv(data):
    nome_arquivo = 'resultado.csv'
    try:
        with open(nome_arquivo, mode='w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Genero', 'Idade', 'Resposta 1', 'Resposta 2', 'Resposta 3', 'Resposta 4', 'Data'])
            for entrevistado in data:
                writer.writerow(entrevistado)
        print(f'Dados foram escritos com sucesso no arquivo {nome_arquivo}.')
    except Exception as e:
        print(f"Erro ao escrever dados no arquivo CSV: {e}")

