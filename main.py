# View - o que vai para usuario 
def view ():
    usuario_digitado = input("infrome o seu usuario: ")
    senha_digitado = input("informe sua senha: ")
    controller(usuario_digitado, senha_digitado)

# Model - o que vem do banco de dados (BD)
def model_usuario():
        usuario_BD = "joao"
        return usuario_BD

def model_senha():
    senha_BD = '123'
    return senha_BD

# Controller - a validaçao
def controller(usuario_digitado, senha_digitado):
    usuario_BD = model_usuario()
    senha_BD = model_senha()
    if usuario_digitado == usuario_BD and senha_digitado == senha_BD:
        print("pode entrar")
    else:
        print("usuario ou senha invalido")






view()