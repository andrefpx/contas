class Conta():
    def __init__ (self,nome,valor):
        self.__nome = nome
        self.__valor = valor

    @property # get
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,nome):
        self.__nome = nome


    @property  # get
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

