import pytest
from src.generator import gerar_senha


def test_tamanho_senha():
    senha = gerar_senha(["Números", "Simbolos"], 16)

    assert len(senha) == 16

def test_numeros():
    senha = gerar_senha(["Números"], 20)

    assert senha.isdigit()

def test_letras_minusculas():
    senha = gerar_senha(["Letras minúsculas"], 20)

    assert senha.islower()
    assert senha.isalpha()

def test_letra_maiusculas():
    senha = gerar_senha(["Letras maiúsculas"], 20)

    assert senha.isupper()
    assert senha.isalpha()

def test_todas_categorias():
    senha = gerar_senha(["Números", "Simbolos", "Letras minúsculas", "Letras maiúsculas"], 16)
    assert len(senha) == 16
    assert any(c.isdigit() for c in senha)
    assert any(c.islower() for c in senha)
    assert any(c.isupper() for c in senha)
    assert any(not c.isalnum() for c in senha)

def test_sem_categoria():
    with pytest.raises(ValueError):
        gerar_senha([], 16)

def test_tamanho_insuficiente():
    with pytest.raises(ValueError):
        gerar_senha(["Números", "Simbolos", "Letras minúsculas", "Letras maiúsculas"], 3)