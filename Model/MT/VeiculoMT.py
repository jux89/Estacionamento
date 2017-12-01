from Model.AT.VeiculoAT import VeiculoAT

numVeiculos = ()

Veiculos = ({'Cod': [], 'Marca':[],'Modelo':[],'AnoFabricacao':[], 'AnoModelo':[], 'Chassi':[], 'Placa':[]})

def cadastrarVeiculo():

    print("\nVAMOS CADASTRAR O VEICULO?!")
    VeiculoAT.Cod = input("Código: ")
    Veiculos['Cod'].append(VeiculoAT.Cod)
    VeiculoAT.Marca = input("Marca: ")
    Veiculos['Marca'].append(VeiculoAT.Marca)
    VeiculoAT.Modelo = input("Modelo: ")
    Veiculos['Modelo'].append(VeiculoAT.Modelo)
    VeiculoAT.AnoFabricacao = input("AnoFabricacão: ")
    Veiculos['AnoFabricacao'].append(VeiculoAT.AnoFabricacao)
    VeiculoAT.AnoModelo = input("AnoModelo: ")
    Veiculos['AnoModelo'].append(VeiculoAT.AnoModelo)
    VeiculoAT.Chassi = input("Chassi")
    Veiculos['Chassi'].append(VeiculoAT.Chassi)
    VeiculoAT.Placa = input("Placa")
    Veiculos['Placa'].append(VeiculoAT.Placa)
    print("\nVeículo cadastrado com sucesso!\n")

def excluirVeiculo():
    consultar = input("\nInforme o código do veiculo: ")
    consultarVei = consultar in Veiculos['Cod']

    if consultarVei == True:

        pos = Veiculos['Placa'].index(consultar)
        Veiculos['Cod'].pop(pos)
        Veiculos['Marca'].pop(pos)
        Veiculos['Modelo'].pop(pos)
        Veiculos['AnoFabricacao'].pop(pos)
        Veiculos['AnoModelo'].pop(pos)
        Veiculos['Chassi'].pop(pos)
        Veiculos['Placa'].pop(pos)

        print("Veiculo removido com sucesso!!")

    else:
        print("Código invalido!!!")

def consultarVeiculo():
    consultar = input("\nInforme o código do veiculo: ")
    consultarVei = consultar in Veiculos['Cod']

    if consultarVei == True:

        pos = Veiculos['Cod'].index(consultar)
        print("Cod|Marca|Modelo|AnoFabricacão|AnoModelo|Chassi|Placa")

        print("{0} \t {1} \t {2} \t {3} \t {4} \t {5} \t {6}".format(Veiculos['Cod'][pos],Veiculos['Marca'][pos], Veiculos['Modelo'][pos], Veiculos['AnoFabricacao'][pos], Veiculos['AnoModelo'][pos], Veiculos['Chassi'][pos], Veiculos['Placa'][pos]))

    else:
        print("Código invalido, veiculo não cadastrado!")

def atualizarVeiculo():
    print("ALTERAÇÃO DE DADOS DO VEICULO:")
    consultar = input("\nInforme o código do veículo: ")
    consultarV = consultar in Veiculos['Código']

    if consultarV == True:

        newMarca = input("Informe a marca do veículo: ")
        pos = Veiculos['Marca'].index(consultar)
        Veiculos['Marca'][pos] = newMarca

        newModelo = input("Informe o novo modelo do veículo: ")
        pos = Veiculos['Modelo'].index(consultar)
        Veiculos['Modelo'][pos] = newModelo

        newFabricacao = input("Ano de Fabricação: ")
        pos = Veiculos['AnoFabricacao'].index(consultar)
        Veiculos['AnoFabricacao'][pos] = newFabricacao

        newAnoModelo = input("Informe o novo ano modelo do veículo: ")
        pos = Veiculos['AnoModelo'].index(consultar)
        Veiculos['AnoModelo'][pos] = newAnoModelo

        newChassi = input("Informe o chassi: ")
        pos = Veiculos['Chassi'].index(consultar)
        Veiculos['Chassi'][pos] = newChassi

        newPlaca = input("Informe a placa do veículo: ")
        pos = Veiculos['Placa'].index(consultar)
        Veiculos['Placa'][pos] = newPlaca

        print("Dados alterados com sucesso!!")

    else:
        print("Código invalido!!!")


def relatorioVeiculo():
    print()
    for i in range(numVeiculos):
        print((Veiculos['Cod'][i], Veiculos['Marca'][i], Veiculos['Modelo'][i], Veiculos['AnoFabricacao'][i], Veiculos['AnoModelo'][i], Veiculos['Chassi'][i], Veiculos['Placa'][i]))






