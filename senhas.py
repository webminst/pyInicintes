import random
import string

def gerador_senhas(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

tamanho_senha = int(input("Digite o tamanho da senha desejada: "))
senha_gerada = gerador_senhas(tamanho_senha)
print("Senha gerada:", senha_gerada)