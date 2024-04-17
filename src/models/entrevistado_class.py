from datetime import datetime

class Entrevistado:
    def __init__(self, genero, idade, resposta_1, resposta_2, resposta_3, resposta_4, resposta_extra_1, resposta_extra_2):
        self.genero = genero
        self.idade = idade
        self.resposta_1 = resposta_1
        self.resposta_2 = resposta_2
        self.resposta_3 = resposta_3
        self.resposta_4 = resposta_4
        self.resposta_extra_1 = resposta_extra_1
        self.resposta_extra_2 = resposta_extra_2

        self.data_hora = datetime.now()