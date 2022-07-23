import validacao

# View - o que vai para usuario 
def formulario_login():
    usuario_digitado = input("infrome o seu usuario: ")
    senha_digitado = input("informe sua senha: ")
    validacao.validar_login(usuario_digitado, senha_digitado)

