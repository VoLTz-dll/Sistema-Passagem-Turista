# utils.py
import sys
import time
import shutil
from colorama import Fore, Back, Style, init

# Inicializar o Colorama
init(autoreset=True)

def limpar_tela():
    print('\033[2J\033[H', end='')

def exibir_boas_vindas():
    limpar_tela()
    # Mensagem de boas-vindas
    mensagem = [
        "Olá, seja bem-vindo!",
        "Estamos apresentando o Sistema de Passagens de Trem Turístico",
        "Feito pela turma de Desenvolvimento de Sistema 2B"
    ]

    # Obtém o tamanho do terminal
    columns, rows = shutil.get_terminal_size()
    
    # Calcula a largura e altura da caixa
    largura_caixa = max(len(linha) for linha in mensagem) + 4  # Margem de 4 caracteres
    altura_caixa = len(mensagem) + 2  # Margem de 2 linhas

    # Garantir que a largura da caixa não exceda a largura do terminal
    if largura_caixa > columns:
        largura_caixa = columns - 4  # Deixa uma margem mínima
    if altura_caixa > rows:
        altura_caixa = rows - 4  # Deixa uma margem mínima

    # Calcula a posição inicial para centralizar a caixa
    x_inicio = (columns - largura_caixa) // 2
    y_inicio = (rows - altura_caixa) // 2

    # Desenha a caixa com a mensagem centralizada
    linhas = []

    # Linha superior da caixa
    linhas.append(' ' * x_inicio + '┌' + '─' * (largura_caixa - 2) + '┐')

    # Linhas de conteúdo
    for linha in mensagem:
        linha_truncada = linha[:largura_caixa - 4]  # Trunca a linha se necessário
        espaco_esquerda = (largura_caixa - 2 - len(linha_truncada)) // 2
        espaco_direita = largura_caixa - 2 - len(linha_truncada) - espaco_esquerda
        linhas.append(' ' * x_inicio + '│' + ' ' * espaco_esquerda + linha_truncada + ' ' * espaco_direita + '│')

    # Linha inferior da caixa
    linhas.append(' ' * x_inicio + '└' + '─' * (largura_caixa - 2) + '┘')

    # Animação de aparecimento
    for linha in linhas:
        print(Fore.GREEN + linha)
        time.sleep(0.3)  # Ajuste o tempo conforme desejado

    time.sleep(2)  # Aguarda alguns segundos antes de limpar a tela
    limpar_tela()

def animacao_carregamento(mensagem, duracao=3, simbolo="."):
    sys.stdout.write(Fore.CYAN + mensagem)
    sys.stdout.flush()
    for _ in range(duracao):
        time.sleep(0.5)
        sys.stdout.write(Fore.CYAN + simbolo)
        sys.stdout.flush()
    sys.stdout.write("\n")

def animacao_cancelamento(mensagem, duracao=5):
    sys.stdout.write(Fore.RED + mensagem)
    sys.stdout.flush()
    for _ in range(duracao):
        time.sleep(0.4)
        sys.stdout.write(Fore.RED + "✖")
        sys.stdout.flush()
    sys.stdout.write("\n")

def animacao_sucesso(mensagem, duracao=3):
    sys.stdout.write(Fore.GREEN + mensagem)
    sys.stdout.flush()
    for _ in range(duracao):
        time.sleep(0.5)
        sys.stdout.write(Fore.GREEN + "✔")
        sys.stdout.flush()
    sys.stdout.write("\n")

def validar_entrada_numerica(mensagem, valor_minimo=1):
    while True:
        try:
            valor = input(Fore.GREEN + mensagem)
            if valor.lower() == 'voltar':
                return 'Voltar'
            valor = int(valor)
            if valor >= valor_minimo:
                return valor
            else:
                print(Fore.RED + f"Valor deve ser maior ou igual a {valor_minimo}. Tente novamente.")
        except ValueError:
            print(Fore.RED + "Entrada inválida. Por favor, insira um número.")
