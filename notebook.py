from produto import Produto

class Notebook(Produto):
    def __init__(self, modelo, cor, preco, categoria, tempoDeBateria):
        super().__init__(modelo, cor, preco, categoria)
        self.__tempoDeBateria = tempoDeBateria

    def cadastrar(self):
        print("Cadastrando notebook...")

    def getInformacoes(self):
        return f'{super().getInformacoes()}, Tempo de Bateria: {self.__tempoDeBateria}'
