# main.py

from colorama import Fore, Back
import inquirer
from utils import limpar_tela, animacao_sucesso, exibir_boas_vindas
from auth import registrar_usuario, recuperar_senha, login
from booking import listar_trens, reservar_passagem, listar_reservas, cancelar_reserva

def menu():
    usuario_atual = None
    while True:
        limpar_tela()  # Limpa a tela no início de cada iteração do menu
        menu_options = [
            "Registrar Usuário",
            "Login",
            "Recuperar Senha",
            "Listar Trens",
            "Reservar Passagem",
            "Listar Reservas",
            "Cancelar Reserva",
            "Logout",
            "Sair"
        ]
        perguntas = [
            inquirer.List('opcao', message=Back.BLUE + Fore.WHITE + "Sistema de Passagens de Trem Turístico", choices=menu_options)
        ]
        resposta = inquirer.prompt(perguntas)
        opcao = resposta['opcao']

        # Limpar a tela antes de executar a opção selecionada
        limpar_tela()

        if opcao == "Registrar Usuário":
            registrar_usuario()
            input(Fore.GREEN + "\nPressione Enter para voltar ao menu...")
        elif opcao == "Login":
            usuario_atual = login()
            if usuario_atual:
                print(Fore.BLACK + Back.GREEN + f"\nVocê está logado como {usuario_atual}!\n")
            input(Fore.GREEN + "\nPressione Enter para voltar ao menu...")
        elif opcao == "Recuperar Senha":
            recuperar_senha()
            input(Fore.GREEN + "\nPressione Enter para voltar ao menu...")
        elif opcao == "Listar Trens":
            listar_trens()
            input(Fore.GREEN + "\nPressione Enter para voltar ao menu...")
        elif opcao == "Reservar Passagem":
            if usuario_atual:
                reservar_passagem(usuario_atual)
            else:
                print(Fore.RED + Back.WHITE + "\nVocê precisa estar logado para reservar uma passagem.\n")
            input(Fore.GREEN + "\nPressione Enter para voltar ao menu...")
        elif opcao == "Listar Reservas":
            if usuario_atual:
                listar_reservas(usuario_atual)
            else:
                print(Fore.RED + Back.WHITE + "\nVocê precisa estar logado para listar suas reservas.\n")
            input(Fore.GREEN + "\nPressione Enter para voltar ao menu...")
        elif opcao == "Cancelar Reserva":
            if usuario_atual:
                cancelar_reserva(usuario_atual)
            else:
                print(Fore.RED + Back.WHITE + "\nVocê precisa estar logado para cancelar uma reserva.\n")
            input(Fore.GREEN + "\nPressione Enter para voltar ao menu...")
        elif opcao == "Logout":
            usuario_atual = None
            animacao_sucesso("Logout bem-sucedido. ", duracao=3)
            input(Fore.GREEN + "\nPressione Enter para voltar ao menu...")
        elif opcao == "Sair":
            animacao_sucesso("Obrigado por usar o sistema de passagens de trem turístico. Até logo! ", duracao=4)
            break

    limpar_tela()  # Limpa a tela ao sair do programa

if __name__ == "__main__":
    exibir_boas_vindas()
    menu()
