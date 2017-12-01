from Model.AT.PessoaAT import PessoaAT

class GerenteAT (PessoaAT):

    def __init__(self):
        self.Cod = []
        self.Salario = []
        self.Endereco = []
        self.Municipio = []
        self.CEP = []

        PessoaAT.__init__()

    @property
    def Cod(self):
        return self.__Cod

    @Cod.setter
    def Cod(self):
        self.__Cod = self.Cod

    @property
    def PessoaAT(self):
        return self.__PessoaAT

    @PessoaAT.setter
    def PessoaAT(self):
        self.__pessoa = self.PessoaAT

    @property
    def Salario(self):
        return self.__Salario

    @Salario.setter
    def Salario(self):
        self.__Salario = self.Salario

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