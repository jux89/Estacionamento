from Model.MT.ClienteMT import *
from Model.MT.GerenteMT import *
from Model.MT.PatioMT import *
from Model.MT.VeiculoMT import *
from Model.MT.ContaMT import *

def menu():
    opcao = int(input('''
    print ('---------------------------------------------')
    print ('|          CONTROLE DE ESTACIONAMENTO       |')
    print ('|              MENU PRINCIPAL               |')
    print ('---------------------------------------------')

    print('1 - Cliente') 
    print('2 - Gerente')
    print('3 - Veiculo')
    print('4 - Patio')
    print('5 - Conta')
    print('6 - Sair')

    'Seja bem-vindo! Escolha uma das opcoes do Menu acima: '''))
    while opcao != 6:
        if opcao == 1:
            print('\nCADASTRO DE CLIENTES:\n')
            print('1 - Cadastro')
            print('2 - Exclusao')
            print('3 - Consulta')
            print('4 - Relatorio')
            print('5 - Alteração')
            print('6 - Voltar ao Menu Principal')

            menuCliente = int(input("Digite a opção desejada: "))
            if menuCliente == 1:
                cadastroCliente()
            elif menuCliente == 2:
                excluirCliente()
            elif menuCliente == 3:
                consultarCliente ()
            elif menuCliente == 4:
                relatorioCliente()
            elif menuCliente == 5:
                atualizarCliente()
            elif menuCliente== 6:
                menu()
            else:
                print("Comando inválido! Digite uma das opções do Menu.")

        elif opcao == 2:
            print('\nCADASTRO DE GERENTE:\n')
            print('1 - Cadastro')
            print('2 - Exclusao')
            print('3 - Consulta')
            print('4 - Relatorio')
            print('5 - Alteração')
            print('6 - Voltar ao Menu Principal')

            menuGerente = int(input("Digite a opção desejada: "))

            if menuGerente == 1:
                cadastrarGerente()
            elif menuGerente == 2:
                excluirGerente()
            elif menuGerente == 3:
                consultarGerente()
            elif menuGerente == 4:
                relatorioGerente()
            elif menuGerente == 5:
                atualizarGerente()
            elif menuGerente == 6:
                menu()
            else:
                print("Comando inválido! Digite uma das opções do Menu.")

        elif opcao == 3:
            print('\nCADASTRO DE VEÍCULO:\n')
            print('1 - Cadastro')
            print('2 - Exclusao')
            print('3 - Consulta')
            print('4 - Relatorio')
            print('5 - Alteração')
            print('6 - Voltar ao Menu Principal')

            menuVeiculo = int(input("Digite a opção desejada: "))
            if menuVeiculo == 1:
                cadastrarVeiculo()
            elif menuVeiculo == 2:
                excluirVeiculo()
            elif menuVeiculo == 3:
                consultarVeiculo()
            elif menuVeiculo == 4:
                relatorioVeiculo()
            elif menuVeiculo == 5:
                atualizarVeiculo()
            elif menuVeiculo == 6:
                menu()
            else:
                print("Comando inválido! Digite uma das opções do Menu.")

        elif opcao == 4:
            print('\nCADASTRO DE PÁTIO:\n')
            print('1 - Cadastro')
            print('2 - Exclusao')
            print('3 - Consulta')
            print('4 - Relatorio')
            print('5 - Alteração')
            print('6 - Voltar ao Menu Principal')

            menuPatio = int(input("Digite a opção desejada: "))
            if menuPatio == 1:
                cadastrarPatio()
            elif menuPatio == 2:
                excluirPatio()
            elif menuPatio == 3:
                consultarPatio()
            elif menuPatio == 4:
                relatorioPatio()
            elif menuPatio == 5:
                atualizarPatio()
            elif menuPatio == 6:
                menu()
            else:
                print("Comando inválido! Digite uma das opções do Menu.")

        elif opcao == 5:
            print('\nSUB MENU CONTA:\n')
            print ('1 - Inclusao de diaria: ')
            print ('2 - Exclusao de diaria: ')
            print ('3 - Total a Pagar: ')
            print ('4 - Voltar ao Menu Principal: ')

            menuConta = int(input("Digite a opção desejada: "))
            if menuConta == 1:
                inclusaoDiaria()
            elif menuConta == 2:
                exclusaoDiaria()
            elif menuConta == 3:
                totalAPagar()
            elif menuConta == 4:
                menu()

            elif opcao == 6:
                exit()

    else:
            print("Digite uma das opcoes presentes no Menu.")


if __name__ == 'main':
    menu()

menu()