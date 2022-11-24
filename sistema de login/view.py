from controller import cadastar, logar, listar

print('Olá seja bem vindo')

while True:
    opecao = int(input('Digite 1 par cadastrar, 2 para logar, 3 para sair: '))

    if opecao == 1:
        nome = input('Digite seu nome: ')
        user = input('Digite um usuario: ')
        senha = input('Digite uma senha: ')
        x = cadastar(nome, user, senha)
        if x == 1:
            print('usuario cadastrado com sucesso')
        elif x == 2:
            print('Usuario ja cadastrado, tente novamente')
        else:
            break

    elif opecao == 2:
        user = input('Digite seu usuario: ')
        senha = input('Digite sua senha: ')
        x = logar(user, senha)
        if x == 3:
            print(f'Bem vindo {user}')
            opecao = int(input('Digite 1 para listar usuários cadastrados, ou 2 para sair: '))
            if opecao == 1:
                x = listar()
            else: 
                break
        elif x == 4:
            print('Usuario ou senha incorretos')

    else:
        break