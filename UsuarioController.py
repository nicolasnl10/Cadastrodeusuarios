from UsuarioModel import Usuario
def cadastrarUsuario(nome, cpf, email):
    if len(cpf)!=11 or "@" not in email:
        return False
    else:
        usuario = Usuario(nome, cpf, email)
        usuario.save()
        return True
