# booking.py

import inquirer
from colorama import Fore, Back
from datetime import datetime
from database import carregar_usuarios, salvar_usuarios
from utils import animacao_carregamento, animacao_sucesso, animacao_cancelamento, validar_entrada_numerica
from trens import trens_disponiveis

def listar_trens():
    print(Back.BLUE + Fore.WHITE + "\n=== Listar Trens ===")
    for trem_id, trem in trens_disponiveis.items():
        print(Fore.YELLOW + f"ID: {trem_id} - Destino: {trem['destino']} - Preço: R${trem['preco']:.2f}")
    print(Back.BLUE + Fore.WHITE + "===========================\n")

def selecionar_forma_pagamento():
    formas_pagamento = ["Dinheiro", "Débito", "Crédito", "Voltar"]
    perguntas = [
        inquirer.List('pagamento', message="Selecione a forma de pagamento:", choices=formas_pagamento)
    ]
    resposta = inquirer.prompt(perguntas)
    return resposta['pagamento']

def reservar_passagem(usuario):
    usuarios = carregar_usuarios()
    listar_trens()
    try:
        trem_choices = [
            f"ID: {trem_id} - Destino: {trens_disponiveis[trem_id]['destino']} - Preço: R${trens_disponiveis[trem_id]['preco']:.2f}"
            for trem_id in trens_disponiveis
        ]
        perguntas = [
            inquirer.List('trem', message="Escolha o trem desejado", choices=trem_choices + ["Voltar"])
        ]
        resposta = inquirer.prompt(perguntas)
        if resposta['trem'] == "Voltar":
            return
        trem_index = trem_choices.index(resposta['trem'])
        trem_id = list(trens_disponiveis.keys())[trem_index]
        trem_selecionado = trens_disponiveis.get(trem_id)

        if trem_selecionado:
            numero_passagens = validar_entrada_numerica("Digite o número de passagens (ou 'Voltar' para retornar): ")
            if numero_passagens == 'Voltar':
                return
            data_reserva = input(Fore.GREEN + "Digite a data da viagem (dd/mm/aaaa) (ou 'Voltar' para retornar): ")
            if data_reserva.lower() == 'voltar':
                return
            try:
                datetime.strptime(data_reserva, "%d/%m/%Y")
            except ValueError:
                print(Fore.RED + "\nData inválida. A reserva não foi concluída.\n")
                return

            total = trem_selecionado['preco'] * numero_passagens
            forma_pagamento = selecionar_forma_pagamento()
            if forma_pagamento == "Voltar":
                return

            animacao_carregamento("Processando reserva", duracao=4, simbolo="⏳")
            usuarios[usuario]["reservas"].append({
                "trem": trem_selecionado,
                "quantidade": numero_passagens,
                "total": total,
                "data": data_reserva,
                "pagamento": forma_pagamento
            })
            salvar_usuarios(usuarios)
            animacao_sucesso(
                f"Reserva concluída com sucesso! Total a pagar: R${total:.2f} via {forma_pagamento}. ",
                duracao=4
            )
        else:
            animacao_cancelamento("ID do trem inválido. Tente novamente. ", duracao=4)
    except ValueError as e:
        animacao_cancelamento(f"Entrada inválida: {e}. Por favor, tente novamente. ", duracao=4)

def listar_reservas(usuario):
    usuarios = carregar_usuarios()
    reservas = usuarios[usuario]["reservas"]
    if not reservas:
        animacao_cancelamento("Nenhuma reserva encontrada. ", duracao=4)
    else:
        print(Back.BLUE + Fore.WHITE + "\n=== Listar Reservas ===")
        for i, reserva in enumerate(reservas, start=1):
            print(Fore.YELLOW + f"Reserva {i}: Destino: {reserva['trem']['destino']}, Quantidade: {reserva['quantidade']}, Data: {reserva['data']}, Total: R${reserva['total']:.2f}, Pagamento: {reserva['pagamento']}")
        print(Back.BLUE + Fore.WHITE + "================\n")

def cancelar_reserva(usuario):
    usuarios = carregar_usuarios()
    reservas = usuarios[usuario]["reservas"]
    if not reservas:
        animacao_cancelamento("Nenhuma reserva encontrada. ", duracao=4)
        return
    try:
        reserva_choices = [
            f"Reserva {i + 1}: Destino: {reserva['trem']['destino']}, Quantidade: {reserva['quantidade']}, Data: {reserva['data']}, Total: R${reserva['total']:.2f}"
            for i, reserva in enumerate(reservas)
        ]
        perguntas = [
            inquirer.List('reserva', message="Escolha a reserva que deseja cancelar", choices=reserva_choices + ["Voltar"])
        ]
        resposta = inquirer.prompt(perguntas)
        if resposta['reserva'] == "Voltar":
            return
        reserva_index = reserva_choices.index(resposta['reserva'])
        reservas.pop(reserva_index)
        usuarios[usuario]["reservas"] = reservas
        salvar_usuarios(usuarios)
        animacao_sucesso("Reserva cancelada com sucesso! ", duracao=3)
    except ValueError:
        animacao_cancelamento("Entrada inválida. Por favor, tente novamente. ", duracao=4)
