from Model.AT.PessoaAT import PessoaAT

class ClienteAT(PessoaAT):

    def __init__(self):
        self.Cod = []
        self.Endereco = []
        self.Municipio = []
        self.UF = []

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
    def PessoaAT(self, value):
        self.__PessoaAT = self.__PessoaAT

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
    def Municipio(self, value):
        self.__Municipio = self.__Municipio

    @property
    def UF(self):
        return self.__UF

    @UF.setter
    def UF(self, value):
        self.__UF = self.__UF
