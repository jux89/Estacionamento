class PessoaAT(object):

    def __init__(self):
        self.Nome = []
        self.Sobrenome = []
        self.Tel = []
        self.Idade = []
        self.Email = []

    @property
    def Nome(self):
        return self.__Nome

    @Nome.setter
    def Nome(self):
        self.__Nome = self.Nome

    @property
    def Sobrenome(self):
        return self.__Sobrenome

    @Sobrenome.setter
    def Sobrenomo(self):
        self.__Sobrenome = self.Sobrenome

    @property
    def Tel(self):
        return self.__Tel

    @Tel.setter
    def Tel(self):
        self.__Tel = self.Tel

    @property
    def Idade(self):
        return self.__Idade

    @Idade.setter
    def Idade(self):
        self.__idade = self.Idade

    @property
    def Email(self):
        return self.__Email

    @Email.setter
    def Email(self):
        self.__Email = self.Email