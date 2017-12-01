from Model.AT.ContaAT import ContaAT
from Model.MT.VeiculoMT import *
from Model.MT.ClienteMT import *
from Model.AT.PátioAT import *

Contas = ({'Cliente': [], 'Veiculo': [], 'Patio': [], 'Ano': [], 'Mes': [], 'Diarias': [], 'Paga': []})

def inclusaoDiaria():

        Contas['Cliente'] = input("Digite o código do cliente: ")
        consultarC = Contas['Cliente'] in Clientes['Cod']
        if consultarC == True:
            Contas['Cliente'].append(ContaAT.Cliente)

        else:
            print("Cliente inexistente!")

        patio = input("Digite o Pátio: ")
        consultarP = patio in PatioAT['Nome']
        if consultarP == True:
            Contas['Patio'].append(ContaAT.Patio)
        else:
            print("Este pátio não está cadastrado!")

        veiculo = input("Digite a placa do veículo: ")
        consultarV = veiculo in Veiculos['Placa']
        if consultarV == True:
            Contas['Veiculo'].append(ContaAT.Veiculo)
        else:
            print("Veículo não cadastrado!")

        def periodo():
            Ano = input("Ano: ")
            Contas['Ano'] = Ano

            Mes = input("Mes")
            Contas['Mes'] = Mes

        def diarias():
            NumDiarias = input("Digite o número de diárias desejadas: ")
            Contas['Diaria'] = NumDiarias
