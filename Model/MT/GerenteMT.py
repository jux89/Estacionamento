from Model.AT.GerenteAT import GerenteAT

Gerentes = ({'Cod': [], 'Nome': [], 'Sobrenome': [], 'Telefone': [], 'Idade': [], 'Email': [], 'Salario': [], 'Endereco':[], 'Municipio': [], 'UF': []})

numGerentes = 0

def cadastrarGerente():

    print("\nCADASTRO GERENTE:\n")
    GerenteAT.Cod = input("Cod: ")
    Gerentes['Cod'].append(GerenteAT.Cod)
    GerenteAT.Nome = input("Nome: ")
    Gerentes['Nome'].append(GerenteAT.Nome)
    GerenteAT.Sobrenome = input("Sobrenome: ")
    Gerentes['Sobrenome'].append(GerenteAT.Sobrenome)
    GerenteAT.Tel = input("Telefone: ")
    Gerentes['Telefone'].append(GerenteAT.Tel)
    GerenteAT.Idade = input("Idade: ")
    Gerentes['Idade'].append(GerenteAT.Idade)
    GerenteAT.Email = input("E-mail: ")
    Gerentes['Email'].append(GerenteAT.Email)
    GerenteAT.Salario = input("Salario: ")
    Gerentes['Salario'].append(GerenteAT.Salario)
    GerenteAT.Endereco = input("Endereco (Preencha os campos Logradouro, número, complemento, bairro, CEP): ")
    Gerentes['Endereco'].append(GerenteAT.Endereco)
    GerenteAT.Municipio = input("Municipio: ")
    Gerentes['Municipio'].append(GerenteAT.Municipio)
    GerenteAT.UF = input("UF: ")
    Gerentes['UF'].append(GerenteAT.UF)

def excluirGerente():
    consultar = input("\nInforme o código do gerente: ")
    consultarV = consultar in Gerentes['Cod']

    if consultarV == True:

        pos = Gerentes['Cod'].index(consultar)
        Gerentes['Cod'].pop(pos)
        Gerentes['Nome'].pop(pos)
        Gerentes['Sobrenome'].pop(pos)
        Gerentes['Endereco'].pop(pos)
        Gerentes['Telefone'].pop(pos)
        Gerentes['Idade'].pop(pos)
        Gerentes['Salario'].pop(pos)
        Gerentes['Email'].pop(pos)
        Gerentes['Municipio'].pop(pos)
        Gerentes['UF'].pop(pos)

        print("Gerente removido com sucesso!!")

    else:
        print("Código invalido!!!")

def consultarGerente():
    consultar = input('\nInforme o código do gerente: ')
    consultarV = consultar in Gerentes['Cod']

    if consultarV == True:

        pos = Gerentes['Cod'].index(consultar)
        print("Cod|Nome|Sobrenome|Telefone|Idade|Email|Salario|Endereco|Municipio|UF")

        print("{0} \t {1} \t {2} \t {3} \t {4} \t {5} \t {6} \t {7} \t {8} \t {9}".format(Gerentes['Cod'][pos], Gerentes['Nome'][pos], Gerentes['Sobrenome'][pos], Gerentes['Telefone'][pos], Gerentes['Idade'][pos], Gerentes['Email'][pos], Gerentes['Salario'][pos], Gerentes['Endereco'][pos], Gerentes['Municipio'][pos],Gerentes['UF'][pos]))

    else:
        print("Código invalido, gerente não cadastrado!")

def atualizarGerente():
    print("\nALTERAÇÃO DE DADOS DO GERENTE:")
    consultar = input("\nInforme o código do cliente: ")
    consultarV = consultar in Gerentes['Cod']

    if consultarV == True:

        newName = input("Informe o novo nome do gerente: ")
        pos = Gerentes['Cod'].index(consultar)
        Gerentes['Nome'][pos] = newName

        newSobrenome = input("Informe o novo sobrenome do gerente: ")
        pos = Gerentes['Cod'].index(consultar)
        Gerentes['Sobrenome'][pos] = newSobrenome

        newEndereco = input("Informe o novo endereço do gerente: ")
        pos = Gerentes['Cod'].index(consultar)
        Gerentes['Endereco'][pos] = newEndereco

        newTelefone = input("Atualização de telefone: ")
        pos = Gerentes['Cod'].index(consultar)
        Gerentes['Telefone'][pos] = newTelefone

        newIdade = input("Informe a idade do gerente: ")
        pos = Gerentes['Cod'].index(consultar)
        Gerentes['Idade'][pos] = newIdade

        newEmail = input("Informe o novo endereço de e-mail do gerente: ")
        pos = Gerentes['Cod'].index(consultar)
        Gerentes['Email'][pos] = newEmail

        newMunicipio = input("Informe o município: ")
        pos = Gerentes['Cod'].index(consultar)
        Gerentes['Municipio'][pos] = newMunicipio

        newUF = input("UF: ")
        pos = Gerentes['Cod'].index(consultar)
        Gerentes['UF'][pos] = newUF

        print("Dados alterados com sucesso!!")

    else:
        print("Código invalido!!!")

def relatorioGerente():
    print()
    for i in range(numGerentes):
        print((Gerentes['Cod'][i],Gerentes['Nome'][i], Gerentes['Sobrenome'][i],Gerentes['Telefone'][i], Gerentes['Idade'][i],Gerentes['Email'][i],Gerentes['Endereco'][i],Gerentes['Municipio'][i], Gerentes['UF'][i]))



