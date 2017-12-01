from Model.AT.ClienteAT import ClienteAT

numClientes = 0

Clientes = ({'Cod': [], 'Nome': [], 'Sobrenome': [], 'Telefone': [], 'Idade': [], 'Email': [], 'Endereco':[], 'Municipio': [], 'UF': []})

def cadastroCliente():

        print("\nCADASTRO CLIENTE:\n")
        ClienteAT.Cod = input("Cod: ")
        Clientes['Cod'].append(ClienteAT.Cod)
        ClienteAT.Nome = input("Nome: ")
        Clientes['Nome'].append(ClienteAT.Nome)
        ClienteAT.Sobrenome = input("Sobrenome: ")
        Clientes['Sobrenome'].append(ClienteAT.Sobrenome)
        ClienteAT.Tel = input("Telefone: ")
        Clientes['Telefone'].append(ClienteAT.Tel)
        ClienteAT.Idade = input("Idade: ")
        Clientes['Idade'].append(ClienteAT.Idade)
        ClienteAT.Email = input("Email: ")
        Clientes['Email'].append(ClienteAT.Email)
        ClienteAT.Endereco = input("Endereco (Preencha os campos Logradouro, número, complemento, bairro, CEP): ")
        Clientes['Endereco'].append(ClienteAT.Endereco)
        ClienteAT.Municipio = input("Municipio: ")
        Clientes['Municipio'].append(ClienteAT.Municipio)
        ClienteAT.UF = input("UF: ")
        Clientes['UF'].append(ClienteAT.UF)
        print("Cliente registrado com sucesso!")

def consultarCliente():
    consultar = input('\nInforme o código do cliente: ')
    consultarV = consultar in Clientes['Cod']

    if consultarV == True:

        pos = Clientes['Cod'].index(consultar)
        print("Cod|Nome|Sobrenome|Telefone|Idade|Email|Endereco|Municipio|UF")

        print("{0} \t {1} \t {2} \t {3} \t {4} \t {5} \t {6} \t {7} \t {8}".format(Clientes['Cod'][pos], Clientes['Nome'][pos], Clientes['Sobrenome'][pos], Clientes['Telefone'][pos], Clientes['Idade'][pos], Clientes['Email'][pos], Clientes['Endereco'][pos], Clientes['Municipio'][pos],Clientes['UF'][pos]))

    else:
        print("Código invalido, cliente não existe!")

def relatorioCliente():
    print()
    for i in range(numClientes):
        print((Clientes['Cod'][i],Clientes['Nome'][i], Clientes['Sobrenome'][i],Clientes['Telefone'][i], Clientes['Idade'][i],Clientes['Email'][i],Clientes['Endereco'][i],Clientes['Municipio'][i], Clientes['UF'][i]))

def excluirCliente():
    consultar = input("\nInforme o código do cliente: ")
    consultarV = consultar in Clientes['Cod']

    if consultarV == True:

        pos = Clientes['Cod'].index(consultar)
        Clientes['Cod'].pop(pos)
        Clientes['Nome'].pop(pos)
        Clientes['Sobrenome'].pop(pos)
        Clientes['Endereco'].pop(pos)
        Clientes['Telefone'].pop(pos)
        Clientes['Idade'].pop(pos)
        Clientes['Email'].pop(pos)
        Clientes['Municipio'].pop(pos)
        Clientes['UF'].pop(pos)

        print("Cliente removido com sucesso!!")

    else:
        print("Código invalido!!!")

def atualizarCliente():
        print("ALTERAÇÃO DE DADOS DO CLIENTE:")
        consultar = input("\nInforme o código do cliente: ")
        consultarV = consultar in Clientes['Cod']

        if consultarV == True:

            newName = input("Informe o novo nome do cliente: ")
            pos = Clientes['Cod'].index(consultar)
            Clientes['Nome'][pos] = newName

            newSobrenome = input("Informe o novo sobrenome do cliente: ")
            pos = Clientes['Cod'].index(consultar)
            Clientes['Sobrenome'][pos] = newSobrenome

            newEndereco = input("Informe o novo endereço do cliente: ")
            pos = Clientes['Cod'].index(consultar)
            Clientes['Endereco'][pos] = newEndereco

            newTelefone = input("Atualização de telefone: ")
            pos = Clientes['Cod'].index(consultar)
            Clientes['Telefone'][pos] = newTelefone

            newIdade = input("Informe a idade do cliente: ")
            pos = Clientes['Cod'].index(consultar)
            Clientes['Idade'][pos] = newIdade

            newEmail = input("Informe o novo endereço de e-mail do cliente: ")
            pos = Clientes['Cod'].index(consultar)
            Clientes['Email'][pos] = newEmail

            newMunicipio = input("Informe o município: ")
            pos = Clientes['Cod'].index(consultar)
            Clientes['Municipio'][pos] = newMunicipio

            newUF = input("UF: ")
            pos = Clientes['Cod'].index(consultar)
            Clientes['UF'][pos] = newUF

            print("Dados alterados com sucesso!!")

        else:
            print("Código invalido!!!")
