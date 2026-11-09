
import string


def avaliar_senha(senha):
    pontos = 0

    # Avalia o comprimento da senha
    if len(senha) <= 10:
        pontos += 5
    else:
        pontos += 20

    # Verifica se possui números
    if any(c.isdigit() for c in senha):
        pontos += 20

    # Verifica se possui letras minúsculas
    if any(c.islower() for c in senha):
        pontos += 20

    # Verifica se possui letras maiúsculas
    if any(c.isupper() for c in senha):
        pontos += 20

    # Verifica se possui símbolos
    if any(c in string.punctuation for c in senha):
        pontos += 20

    return pontos
