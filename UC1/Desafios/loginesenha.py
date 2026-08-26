# definindo as variáveis de login
usuario = "admin"
senha = 123456

# definindo variáveis de controle de tentativas
tentativas = 0
limite = 3

# loop de login
while True:
    usuario1 = input("Digite o usuário: ")
    senha1 = int(input("Digite a senha: "))

    # login caso usuário e senha estejam corretos
    if usuario1 == usuario and senha1 == senha:
        print("Login efetuado com sucesso!")
        break

    # diminuindo tentativas caso usuário ou senha estejam incorretos
    elif usuario1 != usuario or senha1 != senha:
        tentativas = tentativas + 1

        # verificando tentativas
        if tentativas < limite:
            print(f"Usuário ou senha incorretos.\nVocê tem mais {limite - tentativas} tentativas!")

        # encerrando caso exceda o número de tentativas
        else:
            print("Número de tentativas excedido.\nAcesso bloqueado!")
            break