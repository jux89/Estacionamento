from Model.AT.PátioAT import *
from Model.AT.VeiculoAT import *
from Model.AT.ClienteAT import *


class ContaAT(object):

    def __init__(self):
        self.Cliente = []
        self.Veiculo = []
        self.Patio = []
        self.Ano = []
        self.Mes = []
        self.Diaria = []
        self.Paga = []

    @property
    def Cliente(self):
        return self.__Cliente

    @Cliente.setter
    def Cliente(self):
        self.__Cliente = self.__Cliente

    @property
    def Ano(self):
        return self.__Ano

    @Ano.setter
    def Ano(self):
        self.__Ano = self.__Ano

    @property
    def Mes(self):
        return self.__Mes

    @Mes.setter
    def Mes(self):
        self.__Mes = self.__Mes

    @property
    def Diaria(self):
        return self.__Diaria

    @Diaria.setter
    def Diaria(self):
        self.__Diaria = self.__Diaria

    @property
    def Paga(self):
        return self.__Paga

    @Paga.setter
    def Paga(self):
        self.__Paga = self.__Paga

    @property
    def Cliente(self):
        return self.___Cliente

    @Cliente.setter
    def Cliente(self):
        if isinstance(self.__Cliente, ClienteAT):
            self.__Cliente = self.Cliente
        else:
            raise Exception("Cliente inválido!")

    @property
    def Veiculo(self):
        return self.__Veiculo

    @Veiculo.setter
    def Veiculo(self):
        if isinstance(self.__Veiculo, VeiculoAT):
            self.__Veiculo = self.Veiculo
        else:
            raise Exception("Veiculo inválido!")

    @property
    def Patio(self):
        return self.__Patio

    @Patio.setter
    def Patio(self):
        if isinstance(self.Patio, PatioAT):
            self.__Patio = self.Patio
        else:
            raise Exception("Patio inválido!")
