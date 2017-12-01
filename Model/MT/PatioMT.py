from Model.AT.PátioAT import PatioAT

numPatios = 0

Patios = ({'Cod':[],'Nome': [],'Telefone': [], 'CapacidadeV':[], 'ValorDiaria': [], 'Gerente':[],'Cep':[], 'Endereco':[],'Municipio': [], 'UF': []})

def cadastrarPatio():

    print('\nCADASTRO DE PÁTIO:\n')
    PatioAT.Cod = input("Código: ")
    Patios['Cod'].append(PatioAT.Cod)
    PatioAT.Nome = input("Nome: ")
    Patios['Nome'].append(PatioAT.Nome)
    PatioAT.Telefone = input("Telefone: ")
    Patios['Telefone'].append(PatioAT.Telefone)
    PatioAT.CapacidadeV = input("CapacdadeV: ")
    Patios['CapacidadeV'].append(PatioAT.CapacidadeV)
    PatioAT.ValorDiaria = input("ValorDiaria: ")
    Patios['ValorDiaria'].append(PatioAT.ValorDiaria)
    PatioAT.Gerente = input("Gerente: ")
    Patios['Gerente'].append(PatioAT.Gerente)
    PatioAT.Cep = input("Cep")
    Patios['Cep'].append(PatioAT.Cep)
    PatioAT.Endereco = input("Endereco (Preencha os campos Logradouro, número, complemento, bairro, CEP): ")
    Patios['Endereco'].append(PatioAT.Endereco)
    PatioAT.Municipio = input("Municipio: ")
    Patios['Municipio'].append(PatioAT.Municipio)
    PatioAT.UF = input("UF: ")
    Patios['UF'].append(PatioAT.UF)
    print("Pátio cadastrado com sucesso!")

def excluirPatio():
    consultar = input("\nInforme o código do Patio: ")
    consultarP = consultar in Patios['Cod']

    if consultarP == True:

        pos = Patios['Cod'].index(consultar)
        Patios['Cod'].pop(pos)
        Patios['Nome'].pop(pos)
        Patios['Telefone'].pop(pos)
        Patios['CapacidadeV'].pop(pos)
        Patios['ValorDiaria'].pop(pos)
        Patios['Gerente'].pop(pos)
        Patios['Endereço'].pop(pos)
        Patios['Cidade'].pop(pos)
        Patios['UF'].pop(pos)

        print("Patio removido com sucesso!!")

    else:
        print("Código invalido!!!")


def consultarPatio():
    consultar = input("\nInforme o código do Patio: ")
    consultarP = consultar in Patios['Cod']

    if consultarP == True:

        pos = Patios['Cod'].index(consultar)
        print("Cod|Nome|Telefone|CapacidadeV|ValorDiaria|Gerente|Endereço|Cidade|UF")

        print("{0} \t {1} \t {2} \t {3} \t {4} \t {5} \t {6} \t {7} \t {8}".format(Patios['Cod'][pos], Patios['Nome'][pos],Patios['Telefone'][pos], Patios['CapacidadeV'][pos],Patios['ValorDiaria'][pos],Patios['Gerente'][pos],Patios['Endereço'][pos], Patios['Cidade'][pos], Patios['UF'][pos]))

    else:
        print("Código invalido, patio não cadastrado!")


def atualizarPatio():
    print("ALTERAÇÃO DE DADOS DO PÁTIO:")
    consultar = input("\nInforme o código do patio: ")
    consultarV = consultar in Patios['Cod']

    if consultarV == True:

        newName = input("Informe o novo nome do patio: ")
        pos = Patios['Nome'].index(consultar)
        Patios['Nome'][pos] = newName

        newTelefone = input("Informe o novo número de telefone do pátio: ")
        pos = Patios['Telefone'].index(consultar)
        Patios['Telefone'][pos] = newTelefone

        newEndereco = input("Informe o novo endereço do pátio: ")
        pos = Patios['Endereco'].index(consultar)
        Patios['Endereco'][pos] = newEndereco

        newCep = input("Atualização de CEP: ")
        pos = Patios['Cep'].index(consultar)
        Patios['Cep'][pos] = newCep

        newValorDiaria = input("Informe o novo valor da diária: ")
        pos = Patios['ValorDiaria'].index(consultar)
        Patios['ValorDiaria'][pos] = newValorDiaria

        newMunicipio = input("Informe o municipio do pátio: ")
        pos = Patios['Municipio'].index(consultar)
        Patios['Municipio'][pos] = newMunicipio

        newCapacidadeV = input("Informe a nova capacidade de veículos do pátio: ")
        pos = Patios['CapacidadeV'].index(consultar)
        Patios['CapacidadeV'][pos] = newCapacidadeV

        newUF = input("UF do pátio: ")
        pos = Patios['UF'].index(consultar)
        Patios['UF'][pos] = newUF

        newGerente = input("Novo Gerente: ")
        pos = Patios['Gerente'].index(consultar)
        Patios['Gerente'][pos] = newGerente

        print("Dados alterados com sucesso!!")

    else:
        print("Código invalido!!!")

def relatorioPatio():
    print()
    for i in range(numPatios):
        print((Patios['Cod'][i], Patios['Nome'][i],Patios['Telefone'][i], Patios['CapacidadeV'][i],Patios['ValorDiaria'][i],Patios['Gerente'][i],Patios['Endereço'][i], Patios['Cidade'][i], Patios['UF'][i]))