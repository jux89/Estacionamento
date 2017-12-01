class PatioAT(object):

    def __init__(self):
        self.Cod = []
        self.Nome = []
        self.Endereco = []
        self.CEP = []
        self.Municipio = []
        self.Telefone = []
        self.CapacidadeV = []
        self.ValorDiaria = []
        self.Gerente = []

    @property
    def Cod(self):
        return self.__Cod

    @Cod.setter
    def Cod(self):
        self.__Cod = self.Cod

    @property
    def Nome(self):
        return self.__Nome

    @Nome.setter
    def Nome(self):
        self.__Nome = self.Nome

    @property
    def Endereco(self):
        return self.__Endereco

    @Endereco.setter
    def Endereco(self, value):
        self.__Endereco = self.Endereco

    @property
    def Municipio(self):
        return self.__Municipio

    @Municipio.setter
    def Municipio(self):
        self.__Municipio = self.Municipio

    @property
    def CEP(self):
        return self.__CEP

    @CEP.setter
    def CEP(self):
        self.__CEP = self.CEP

    @property
    def Telefone(self):
        return self.__Telefone

    @Telefone.setter
    def Telefone(self):
        self.__Telefone = self.Telefone

    @property
    def CapacidadeV(self):
        return self.__CapacidadeV

    @CapacidadeV.setter
    def CapacidadeV(self):
        self.__CapacidadeV = self.CapacidadeV

    @property
    def ValorDiaria(self):
        return self.__ValorDiaria

    @ValorDiaria.setter
    def ValorDiaria(self, value):
        self.__valor_diaria = self.__ValorDiaria

    @property
    def Gerente(self):
        return self.__Gerente

    @Gerente.setter
    def Gerente(self):
        self.__Gerente = self.__Gerente