
import secrets
import string


def gerar_senha(selecionados, tamanho):
    caracteres = ""
    categorias = []

    if "Números" in selecionados:
        caracteres += string.digits
        categorias.append(string.digits)

    if "Simbolos" in selecionados:
        caracteres += string.punctuation
        categorias.append(string.punctuation)

    if "Letras minúsculas" in selecionados:
        caracteres += string.ascii_lowercase
        categorias.append(string.ascii_lowercase)

    if "Letras maiúsculas" in selecionados:
        caracteres += string.ascii_uppercase
        categorias.append(string.ascii_uppercase)

    if not caracteres:
        raise ValueError("Selecione pelo menos uma categoria!")

    if tamanho < len(categorias):
        raise ValueError("Tamanho insuficiente!")

    senha = []

    # Garante um caractere de cada categoria
    for categoria in categorias:
        senha.append(secrets.choice(categoria))

    # Completa o tamanho da senha
    while len(senha) < tamanho:
        senha.append(secrets.choice(caracteres))

    # Embaralha os caracteres
    for j in range(len(senha) - 1, 0, -1):
        k = secrets.randbelow(j + 1)
        senha[j], senha[k] = senha[k], senha[j]

    # Retorna a senha pronta
    return "".join(senha)
