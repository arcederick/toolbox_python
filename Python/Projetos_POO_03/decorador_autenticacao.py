# Decorador de Autenticação
def autenticacao_requerida(funcao):
    def wrapper(usuario, *args, **kwargs):
        if usuario["autenticado"]:
            return funcao(usuario, *args, **kwargs)
        else:
            return "Acesso não autorizado. Faça login primeiro."
    return wrapper

# Função de Login Simples
def fazer_login(usuario, senha):
    if senha == "senha_segura":
        usuario["autenticado"] = True
        return "Login bem-sucedido."
    else:
        usuario["autenticado"] = False
        return "Senha incorreta."

# Função para Visualizar Notas (requer autenticação)
@autenticacao_requerida
def visualizar_notas(usuario):
    return f"Suas notas: Matemática: 90, História: 85, Ciências: 88"

# Função para Sair
def fazer_logout(usuario):
    usuario["autenticado"] = False
    return "Logout bem-sucedido."

if __name__ == "__main__":
    usuario = {"autenticado": False}

    print(fazer_login(usuario, "senha_errada"))
    print(fazer_login(usuario, "senha_segura"))

    print(visualizar_notas(usuario))  # Esta função requer autenticação
    print(fazer_logout(usuario))

    print(visualizar_notas(usuario))  # Tentando acessar após o logout