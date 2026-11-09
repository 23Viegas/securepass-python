import pytest
import string

minusculas = string.ascii_lowercase[:8]
maiusculas = string.ascii_uppercase[:8]
numeros = string.digits[:8]
simbolos = string.punctuation[:8]

from src.security import avaliar_senha
from src.generator import gerar_senha




def test_apenas_numeros():
    senha = numeros[:8]
    pontos = avaliar_senha(senha)
    assert pontos == 25

def test_apenas_minusculas():
    senha = minusculas[:8]
    pontos = avaliar_senha(senha)
    assert pontos == 25

def test_apenas_maiusculas():
    senha = maiusculas[:8]
    pontos = avaliar_senha(senha)
    assert pontos == 25

def test_apenas_simbolos():
    senha = simbolos[:8]
    pontos = avaliar_senha(senha)
    assert pontos == 25

def test_numeros_minusculas():
    senha = numeros[:4] + minusculas[:4]
    pontos = avaliar_senha(senha)
    assert pontos == 45

def test_numeros_maiusculas():
    senha = numeros[:4] + maiusculas[:4]
    pontos = avaliar_senha(senha)
    assert pontos == 45

def test_minusculas_maisuculas():
    senha = minusculas[:4] + maiusculas[:4]
    pontos = avaliar_senha(senha)
    assert pontos == 45

def test_3_categorias():
    senha = numeros[:3] + minusculas[:3] + maiusculas[:3]
    pontos = avaliar_senha(senha)
    assert pontos == 65

def test_todas_categorias():
    senha = numeros[:2] + minusculas[:2] + maiusculas[:2] + simbolos[:2]
    pontos = avaliar_senha(senha)
    assert pontos == 85

def test_todas_categorias_10():
    senha = numeros[:4] + maiusculas[:4] + minusculas[:4] + simbolos[:4]
    assert len(senha) >= 10
    pontos = avaliar_senha(senha)
    assert pontos == 100
    