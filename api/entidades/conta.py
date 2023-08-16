class Conta():
    def __init__ (self,nome,resumo,valor ):
        self.__nome = nome
        self.__resumo = resumo
        self.__valor = valor
    @property # get
    def nome(self):
        self.__nome

    @nome.setter
    def nome(self,nome):
        self.__nome = nome

    @property  # get
    def resumo(self):
        self.resumo

    @resumo.setter
    def resumo(self, resumo):
        self.resumo = resumo

    @property  # get
    def valor(self):
        self.valor

    @valor.setter
    def valor(self, valor):
        self.valor = valor