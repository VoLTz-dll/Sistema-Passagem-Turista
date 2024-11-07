# auth.py

import getpass
from colorama import Fore, Back
from datetime import datetime
from database import carregar_usuarios, salvar_usuarios
from utils import animacao_carregamento, animacao_sucesso, animacao_cancelamento

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
        senha = getpass.getpass(Fore.GREEN + "Digite uma senha (ou 'Voltar' para retornar): ").strip()
        if senha.lower() == 'voltar':
            return
        if not senha:
            print(Fore.RED + "Senha não pode ser vazia. Tente novamente.")
        else:
            break
    pergunta_recuperacao = input(Fore.GREEN + "Digite uma pergunta de recuperação de senha (ou 'Voltar' para retornar): ").strip()
    if pergunta_recuperacao.lower() == 'voltar':
        return
    while not pergunta_recuperacao:
        print(Fore.RED + "Pergunta de recuperação não pode ser vazia. Tente novamente.")
        pergunta_recuperacao = input(Fore.GREEN + "Digite uma pergunta de recuperação de senha: ").strip()
    resposta_recuperacao = input(Fore.GREEN + "Digite a resposta para a pergunta de recuperação (ou 'Voltar' para retornar): ").strip()
    if resposta_recuperacao.lower() == 'voltar':
        return
    while not resposta_recuperacao:
        print(Fore.RED + "Resposta de recuperação não pode ser vazia. Tente novamente.")
        resposta_recuperacao = input(Fore.GREEN + "Digite a resposta para a pergunta de recuperação: ").strip()
    usuarios[username] = {
        "senha": senha,
        "reservas": [],
        "pergunta_recuperacao": pergunta_recuperacao,
        "resposta_recuperacao": resposta_recuperacao
    }
    salvar_usuarios(usuarios)
    animacao_carregamento("Registrando usuário", duracao=4)
    animacao_sucesso("Usuário registrado com sucesso! ", duracao=3)

def recuperar_senha():
    usuarios = carregar_usuarios()
    print(Back.BLUE + Fore.WHITE + "\n=== Recuperar Senha ===")
    username = input(Fore.GREEN + "Digite seu nome de usuário (ou 'Voltar' para retornar): ")
    if username.lower() == 'voltar':
        return
    if username in usuarios:
        pergunta = usuarios[username]["pergunta_recuperacao"]
        resposta = input(Fore.GREEN + f"{pergunta} (ou 'Voltar' para retornar): ")
        if resposta.lower() == 'voltar':
            return
        if resposta == usuarios[username]["resposta_recuperacao"]:
            nova_senha = getpass.getpass(Fore.GREEN + "Digite a nova senha (ou 'Voltar' para retornar): ")
            if nova_senha.lower() == 'voltar':
                return
            while not nova_senha:
                print(Fore.RED + "Senha não pode ser vazia. Tente novamente.")
                nova_senha = getpass.getpass(Fore.GREEN + "Digite a nova senha: ")
            usuarios[username]["senha"] = nova_senha
            salvar_usuarios(usuarios)
            animacao_sucesso("Senha alterada com sucesso! ", duracao=3)
        else:
            animacao_cancelamento("Resposta incorreta. Não foi possível alterar a senha. ", duracao=4)
    else:
        animacao_cancelamento("Usuário não encontrado. ", duracao=4)

def login():
    usuarios = carregar_usuarios()
    print(Back.BLUE + Fore.WHITE + "\n=== Login ===")
    while True:
        username = input(Fore.GREEN + "Digite seu nome de usuário (ou 'Voltar' para retornar): ")
        if username.lower() == 'voltar':
            return None
        senha = getpass.getpass(Fore.GREEN + "Digite sua senha (ou 'Voltar' para retornar): ")
        if senha.lower() == 'voltar':
            return None
        animacao_carregamento("Validando credenciais", duracao=3, simbolo="⏳")
        if username in usuarios and usuarios[username]["senha"] == senha:
            animacao_sucesso("Login bem-sucedido! ", duracao=3)
            return username
        else:
            animacao_cancelamento("Usuário ou senha incorretos. Tente novamente. ", duracao=4)
