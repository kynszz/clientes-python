# View - o que vai para usuario 
usuario_digitado = input("infrome o seu usuario: ")
senha_digitado = input("informe sua senha: ")

# Model - o que vem do banco de dados (BD)
usuario_BD = "joao"
senha_BD = "123"

# Controller - a validaçao
if usuario_digitado == "usuario_BD" and senha_digitado == senha_BD:
    print('pode entrar')
else:
    print("usuario ou senha invalido")