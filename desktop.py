from produto import Produto

class Desktop(Produto):
    def __init__(self, modelo, cor, preco, categoria, potenciaDaFonte):
        super().__init__(modelo, cor, preco, categoria)
        self.__potenciaDaFonte = potenciaDaFonte

    def cadastrar(self):
        pass

    def getInformacoes(self):
        return f'{super().getInformacoes()}, Potência da Fonte: {self.__potenciaDaFonte}'
