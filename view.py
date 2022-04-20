from controller import Controller_Cadastro, Controller_Login

while True:
    print('=========== SISTEMA DE LOGIN ===========\n')
    entrada = int(input(
        f'Digite 1 para realizar cadastro\n'
        f'Digite 2 para realizar login\n'
        f'Digite 3 para sair\n'
    ))

    if entrada == 1:
        nome = input('Digite seu nome: ')
        email = input('Digite seu email: ')
        senha = input('Digite sua senha: ')

        resultado = Controller_Cadastro.cadastrarUsuario(nome, email, senha)
        
        if resultado == 1:
            print('Cadastro realizado com sucesso\n')
        elif resultado == 2:
            print('Tamanho do nome digitado inválido')
        elif resultado == 3:
            print('Email maior que 200 caracteres')
        elif resultado == 4:
            print('Tamanho da senha inválido')
    
    elif entrada == 2:
        email = input('Digite seu email: ')
        senha = input('Digite sua senha: ')

        resultado = Controller_Login.login(email, senha)

        if resultado:
            print('Login realizado com sucesso\n')
            print(resultado)
        else:
            print('Email ou senha inválidos')


        
        
        
