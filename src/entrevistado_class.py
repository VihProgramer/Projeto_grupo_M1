from datetime import datetime

class Entrevistado:
    def __init__(self, idade, genero, resposta_1, resposta_2, resposta_3, resposta_4):
        self.idade = idade
        self.genero = genero
        self.resposta_1 = resposta_1
        self.resposta_2 = resposta_2
        self.resposta_3 = resposta_3
        self.resposta_4 = resposta_4
        self.data_hora = datetime.now()
    
    def __repr__(self):
        data_hora_formatada = self.data_hora.strftime("%d/%m/%Y, %H:%M:%S")
        return f"{self.idade},{self.genero},{self.resposta_1},{self.resposta_2},{self.resposta_3},{self.resposta_4},{data_hora_formatada}"