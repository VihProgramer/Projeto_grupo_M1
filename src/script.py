from entrevistado_class import *
data = []

def input_de_dados(nome, idade, resposta_1, resposta_2, resposta_3, resposta_4):
    try:
        if not all([nome, idade, resposta_1, resposta_2, resposta_3, resposta_4]):            
            return False
        data.append([nome, idade, resposta_1, resposta_2, resposta_3, resposta_4])
        return True
    except:
        print("Erro ao adicionar dados:")
        return False
    


def escrever_csv():
    print('estou no escrever_csv')

def pesquisa_digital():
    print('estou no pesquisa_digital')