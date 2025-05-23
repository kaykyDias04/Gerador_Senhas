from gerador import gerar_senha

senha = gerar_senha(12, letras=True, numeros=True, simbolos=False)
print(senha)