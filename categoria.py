class Categoria:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    def getInformacoes(self):
        return f'ID: {self.id}, Nome: {self.nome}'
