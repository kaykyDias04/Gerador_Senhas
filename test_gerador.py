import pytest
import string
from gerador import gerar_senha


def test_tamanho_senha():
    assert len(gerar_senha(10)) == 10

def test_somente_letras():
    senha = gerar_senha(10, letras=True, numeros=False, simbolos=False)
    assert senha.isalpha()

def test_somente_numeros():
    senha = gerar_senha(5, letras=False, numeros=True, simbolos=False)
    assert senha.isdigit()

def test_com_simbolos():
    senha = gerar_senha(20, letras=False, numeros=False, simbolos=True)
    assert all(c in string.punctuation for c in senha)

def test_tamanho_invalido():
    with pytest.raises(ValueError):
        gerar_senha(0)

def test_nenhum_tipo_caractere():
    with pytest.raises(ValueError):
        gerar_senha(5, letras=False, numeros=False, simbolos=False)