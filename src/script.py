import csv
from entrevistado_class import *
data = []

def input_de_dados(genero, idade, resposta_1, resposta_2, resposta_3, resposta_4):
    try:
        if not all([genero, idade, resposta_1, resposta_2, resposta_3, resposta_4]):            
            return False
        entrevistado = Entrevistado(idade, genero, resposta_1, resposta_2, resposta_3, resposta_4)
        print(f'Eu sou o entrevistado: {entrevistado}')
        data_hora_formatada = entrevistado.data_hora.strftime("%d/%m/%Y")
        data.append([entrevistado.genero, entrevistado.idade, entrevistado.resposta_1, entrevistado.resposta_2, entrevistado.resposta_3, entrevistado.resposta_4, data_hora_formatada])
        print(f'Eu sou o data: {data}')
        return True
    except:
        print("Erro ao adicionar dados:")
        return False
    

# Definição da função escrever_csv para escrever os dados no arquivo CSV
def escrever_csv():
    nome_arquivo = 'resultado.csv'  # Nome do arquivo CSV
    try:
        with open(nome_arquivo, mode='w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            # Escreva o cabeçalho do arquivo CSV
            writer.writerow(['Nome', 'Idade', 'Resposta 1', 'Resposta 2', 'Resposta 3', 'Resposta 4', 'Data'])
            # Itere sobre os dados e escreva cada conjunto de respostas no arquivo CSV
            for entrevistado in data:
                writer.writerow(entrevistado)
        print(f'Dados foram escritos com sucesso no arquivo {nome_arquivo}.')
    except Exception as e:
        print(f"Erro ao escrever dados no arquivo CSV: {e}")

# Função para salvar as respostas e chamar escrever_csv() após cada entrevista
def salvar_respostas(e):
    if input_de_dados(nome.value, idade.value, pergunta_1.value, pergunta_2.value, pergunta_3.value, pergunta_4.value):
        nome.value = ''
        idade.value = ''
        pergunta_1.value = ''
        pergunta_2.value = ''
        pergunta_3.value = ''
        pergunta_4.value = ''
        alertar = exibir_alerta("Obrigado!","Suas respostas foram salvas com sucesso!", "")
        page.dialog = alertar
        alertar.open = True
        page.update()
        
        # Adicione as respostas à lista 'data'
        data.append([nome.value, idade.value, pergunta_1.value, pergunta_2.value, pergunta_3.value, pergunta_4.value])
        
        # Após salvar as respostas, escreva os dados no arquivo CSV
        escrever_csv()
    else:
        alertar = exibir_alerta("Atenção!","Preencha todos os campos corretamente!", "")
        page.dialog = alertar
        alertar.open = True
        page.update()

