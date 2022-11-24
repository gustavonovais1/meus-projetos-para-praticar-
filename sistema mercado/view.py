from controller import *

print('Olá seja bem vindo(a) de volta!')

while True:

    decisao = int(input('Digite para acessar opçôes: 1 para Clientes, 2 para Funcionarios, 3 para Produtos, 0 para sair: '))

    if decisao == 1:
        decidir = int(input('Digite 1 para cadastrar um cliente, 2 para excluir um cliente, 3 para listar clientes, ou 0 para sair: '))
        if decidir == 1:
            nome = input('Digite o nome do cliente: ')
            telefone = int(input('Digite o telefone: '))
            cpf = int(input('Digite o cpf do cliente: '))
            id_cliente = int(input('Digite um id para o cliente: '))
            x = ControllerCliente.cadastrar_cliente(Cliente(nome, telefone, cpf, id_cliente))
            if x == 7:
                print('CPF já cadastrado, tente novamnete com outro cpf')
            elif x == 8:
                print("Cliente cadastrado com sucesso")
            elif x == 9:
                print('Erro ao cadastrar cliente')

        elif decidir == 2:
            cpf = int(input('Digite o cpf do cliente que deseja excluir: '))
            x = ControllerCliente.excluir_cliente(cpf)
            if x == 10:
                print('Cliente excluido com sucesso!')
            elif x == 11:
                print('Erro ao excluir cliente')
            elif x == 12:
                print('Não existe cliente cadastrado com esse cpf')

        elif decidir == 3:
            ControllerListar.listar_clientes()
        else:
            break

    elif decisao == 2:
        decidir = int(input('Digite 1 para cadastrar um funcionario, 2 para excluir um funcionario, 3 para listar funcionarios ou 0 para sair: '))
        if decidir == 1:
            nome = input("Digite o nome do funcionario: ")
            telefone = int(input('Digite um telefone: '))
            cpf = int(input('Digite o cpf do funcionarioo: '))
            clt = int(input('Digite o numero da clt do funcionario: '))
            x = ControllerFuncionario.cadastrar_funcionario(Funcionario(nome,telefone, cpf, clt))
            if x == 1:
                print('CPF já cadastrado, tente novamnete com outro cpf')
            elif x == 2:
                print('Funcionario cadastrado com sucesso!')
            elif x == 3:
                print('Erro ao cadastrar funcionario')

        elif decidir == 2:
            cpf = int(input('Digite o cpf do funcionario que deseja excluir: '))
            x = ControllerFuncionario.excluir_funcionario(cpf)
            if x == 4:
                print('Funcionario excluido com sucesso!')
            elif x == 5:
                print('Erro ao excluir funcionario')
            elif x == 6:
                print('Não existe funcionario cadastrado com esse cpf')

        elif decidir == 3:
            ControllerListar.listar_funcionarios()
        else:
            break

    elif decisao == 3:
        decidir = int(input('Digite 1 para cadastrar um produto, 2 para excluir um produto, 3 para listar produtos ou 0 para sair: '))
        if decidir == 1:
            nomeProduto = input('Digite o nome do produto: ')
            preco = int(input('Digite o preço do produto: '))
            x = ControllerProduto.cadastrar_produto(Produto(nomeProduto, preco))
            if x == 13:
                print('Produto já cadastrado, tente novamnete com outro nome de produto')
            elif x == 14:
                print("Produto cadastrado com sucesso")
            elif x == 15:
                print('Erro ao cadastrar produto')

        elif decidir == 2:
            nomeProduto = input('Digite o nome do produto: ')
            x = ControllerProduto.excluir_produto(nomeProduto)
            if x == 16:
                print('Produto excluido com sucesso!')
            elif x == 17:
                print('Erro ao excluir produto')
            elif x == 18:
                print('Não existe produto cadastrado com esse nome')

        elif decidir == 3:
            ControllerListar.listar_produtos()
        else:
            break

    else:
        break