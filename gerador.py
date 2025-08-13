import random
import string

def gerar_senha(tamanho=8, letras=True, numeros=True, simbolos=True):
    if tamanho < 1:
        raise ValueError("Tamanho deve ser maior que zero")

    caracteres = ''
    if letras:
        caracteres += string.ascii_letters
    if numeros:
        caracteres += string.digits
    if simbolos:
        caracteres += string.punctuation

    if not caracteres:
        raise ValueError("Nenhum tipo de caractere selecionado")

printf("teste")