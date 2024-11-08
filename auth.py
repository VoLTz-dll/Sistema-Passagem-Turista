# auth.py

from colorama import Fore, Back
from database import carregar_usuarios, salvar_usuarios
from utils import animacao_carregamento, animacao_sucesso, animacao_cancelamento, input_senha

def registrar_usuario():
    usuarios = carregar_usuarios()
    print(Back.BLUE + Fore.WHITE + "\n=== Registrar Usuário ===")
    while True:
        username = input(Fore.GREEN + "Digite um nome de usuário (ou 'Voltar' para retornar): ").strip()
        if username.lower() == 'voltar':
            return
        if not username:
            print(Fore.RED + "Nome de usuário não pode ser vazio. Tente novamente.")
        elif username in usuarios:
            print(Fore.RED + Back.WHITE + "\nUsuário já existe. Tente um nome diferente.\n")
        else:
            break
    while True:
        senha = input_senha("Digite uma senha (ou 'Voltar' para retornar): ").strip()
        if senha.lower() == 'voltar':
            return
        if not senha:
            print(Fore.RED + "Senha não pode ser vazia. Tente novamente.")
        else:
            break

    usuarios[username] = {
        "senha": senha,
        "reservas": []

    }
    salvar_usuarios(usuarios)
    animacao_carregamento("Registrando usuário", duracao=4)
    animacao_sucesso("Usuário registrado com sucesso! ", duracao=3)




def login():
    usuarios = carregar_usuarios()
    print(Back.BLUE + Fore.WHITE + "\n=== Login ===")
    while True:
        username = input(Fore.GREEN + "Digite seu nome de usuário (ou 'Voltar' para retornar): ").strip()
        if username.lower() == 'voltar':
            return None
        if not username:
            print(Fore.RED + "Nome de usuário não pode ser vazio. Tente novamente.")
            continue
        senha = input_senha("Digite sua senha (ou 'Voltar' para retornar): ").strip()
        if senha.lower() == 'voltar':
            return None
        if not senha:
            print(Fore.RED + "Senha não pode ser vazia. Tente novamente.")
            continue
        animacao_carregamento("Validando credenciais", duracao=3, simbolo="⏳")
        if username in usuarios and usuarios[username]["senha"] == senha:
            animacao_sucesso("Login bem-sucedido! ", duracao=3)
            return username
        else:
            animacao_cancelamento("Usuário ou senha incorretos. Tente novamente. ", duracao=4)
