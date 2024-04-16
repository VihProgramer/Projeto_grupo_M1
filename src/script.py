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
    


def escrever_csv():
    print('estou no escrever_csv')