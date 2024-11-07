# Sistema de Passagens de Trem Turístico

## Sumário

- [Introdução](#introdução)
- [Objetivos do Projeto](#objetivos-do-projeto)
- [Funcionalidades](#funcionalidades)
- [Requisitos do Sistema](#requisitos-do-sistema)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Instalação e Configuração](#instalação-e-configuração)
- [Como Executar o Programa](#como-executar-o-programa)
- [Detalhamento dos Módulos](#detalhamento-dos-módulos)
  - [1. `main.py`](#1-mainpy)
  - [2. `utils.py`](#2-utilspy)
  - [3. `database.py`](#3-databasepy)
  - [4. `auth.py`](#4-authpy)
  - [5. `booking.py`](#5-bookingpy)
  - [6. `trens.py`](#6-trenspy)
- [Fluxo de Execução do Programa](#fluxo-de-execução-do-programa)
- [Como Utilizar o Sistema](#como-utilizar-o-sistema)
- [Melhorias Futuras](#melhorias-futuras)
- [Contribuições](#contribuições)
- [Licença](#licença)

---

## Introdução

Este projeto é um **Sistema de Passagens de Trem Turístico** desenvolvido pela turma de **Desenvolvimento de Sistemas 2B**. O sistema permite que os usuários interajam através de uma interface de linha de comando para realizar operações relacionadas à compra de passagens de trem turístico.

## Objetivos do Projeto

- Proporcionar uma experiência interativa para usuários que desejam reservar passagens de trem.
- Implementar conceitos de programação modular para melhorar a organização e manutenção do código.
- Praticar o uso de bibliotecas externas como `colorama` e `inquirer` para melhorar a interface de usuário.

## Funcionalidades

- **Registro de Usuário**: Permite que novos usuários se cadastrem no sistema.
- **Login**: Usuários registrados podem fazer login para acessar funcionalidades adicionais.
- **Recuperação de Senha**: Usuários podem recuperar suas senhas através de uma pergunta de segurança.
- **Listagem de Trens Disponíveis**: Exibe uma lista de trens turísticos disponíveis para reserva.
- **Reserva de Passagens**: Usuários logados podem reservar passagens para os trens disponíveis.
- **Listagem de Reservas**: Usuários podem visualizar suas reservas atuais.
- **Cancelamento de Reservas**: Permite que usuários cancelem reservas existentes.
- **Logout**: Usuários podem sair de suas contas.
- **Interface Limpa**: O sistema limpa o terminal em momentos apropriados para manter a interface organizada.

## Requisitos do Sistema

- **Python 3.6 ou superior**
- **Bibliotecas Python**:
  - `colorama`
  - `inquirer`
- **Sistema Operacional**: Compatível com Windows, macOS e Linux.

## Estrutura do Projeto

```
SistemaPassagensTrem/
│
├── main.py
├── database.py
├── utils.py
├── auth.py
├── booking.py
├── trens.py
└── data/
    └── usuarios.json
```

- **`main.py`**: Script principal que inicializa o programa e apresenta o menu principal.
- **`database.py`**: Gerencia o carregamento e salvamento dos dados dos usuários.
- **`utils.py`**: Contém funções utilitárias, como limpeza de tela e animações.
- **`auth.py`**: Gerencia o registro, login e recuperação de senha dos usuários.
- **`booking.py`**: Gerencia a reserva, listagem e cancelamento de passagens.
- **`trens.py`**: Armazena os dados dos trens disponíveis.
- **`data/usuarios.json`**: Arquivo JSON que armazena os dados dos usuários registrados.

## Instalação e Configuração

### 1. Clone o Repositório

```bash
git clone https://github.com/seu_usuario/SistemaPassagensTrem.git
cd SistemaPassagensTrem
```

### 2. Crie um Ambiente Virtual (Opcional, mas Recomendado)

```bash
python -m venv venv
```

Ative o ambiente virtual:

- **Windows**:

  ```bash
  venv\Scripts\activate
  ```

- **macOS/Linux**:

  ```bash
  source venv/bin/activate
  ```

### 3. Instale as Dependências

```bash
pip install -r requirements.txt
```

**Conteúdo do arquivo `requirements.txt`**:

```
colorama
inquirer
```

## Como Executar o Programa

Após instalar as dependências, execute o programa principal:

```bash
python main.py
```

## Detalhamento dos Módulos

### 1. `main.py`

Responsável por inicializar o sistema e controlar o fluxo do menu principal. Utiliza as funções definidas nos outros módulos para executar as ações selecionadas pelo usuário.

Principais funções:

- `menu()`: Controla o menu principal e a navegação entre as opções.
- Chama `exibir_boas_vindas()` para mostrar a mensagem inicial.

### 2. `utils.py`

Contém funções auxiliares para melhorar a experiência do usuário.

Principais funções:

- `limpar_tela()`: Limpa o terminal de forma portátil entre diferentes sistemas operacionais.
- `exibir_boas_vindas()`: Exibe uma mensagem de boas-vindas centralizada na tela com animação.
- `animacao_carregamento()`, `animacao_sucesso()`, `animacao_cancelamento()`: Funções para exibir animações de carregamento, sucesso e erro.
- `validar_entrada_numerica()`: Valida a entrada numérica do usuário.

### 3. `database.py`

Gerencia o carregamento e salvamento dos dados dos usuários.

Principais funções:

- `carregar_usuarios()`: Carrega os dados dos usuários a partir do arquivo JSON.
- `salvar_usuarios()`: Salva os dados dos usuários no arquivo JSON.

### 4. `auth.py`

Gerencia o registro, login e recuperação de senha dos usuários.

Principais funções:

- `registrar_usuario()`: Permite que novos usuários se registrem no sistema.
- `login()`: Permite que usuários existentes façam login.
- `recuperar_senha()`: Permite que usuários recuperem suas senhas através de uma pergunta de segurança.

### 5. `booking.py`

Gerencia as reservas de passagens.

Principais funções:

- `listar_trens()`: Exibe a lista de trens disponíveis para reserva.
- `reservar_passagem(usuario)`: Permite que um usuário logado reserve passagens.
- `listar_reservas(usuario)`: Lista as reservas feitas pelo usuário.
- `cancelar_reserva(usuario)`: Permite que o usuário cancele uma reserva existente.

### 6. `trens.py`

Armazena os dados dos trens disponíveis para reserva.

Estrutura:

```python
trens_disponiveis = {
    1: {"destino": "Campos do Jordão", "preco": 150.0},
    2: {"destino": "Santos", "preco": 120.0},
    # ... outros trens
}
```

## Fluxo de Execução do Programa

1. **Mensagem de Boas-vindas**: Ao iniciar, o programa exibe uma mensagem de boas-vindas com animação.

2. **Menu Principal**: O usuário é apresentado ao menu principal com as opções disponíveis.

3. **Interação do Usuário**: O usuário pode navegar pelas opções do menu para realizar ações como registrar-se, fazer login, listar trens, reservar passagens, etc.

4. **Manutenção do Estado do Usuário**: O sistema mantém o estado de login do usuário, permitindo acesso a funcionalidades restritas.

5. **Encerramento**: Ao selecionar a opção "Sair", o programa exibe uma mensagem de despedida e encerra.

## Como Utilizar o Sistema

1. **Registrar Usuário**: Se você é um novo usuário, escolha a opção "Registrar Usuário" no menu principal e siga as instruções para criar uma conta.

2. **Login**: Faça login com seu nome de usuário e senha para acessar funcionalidades adicionais.

3. **Listar Trens**: Consulte os trens disponíveis para reserva, visualizando destinos e preços.

4. **Reservar Passagem**: Após fazer login, escolha a opção "Reservar Passagem" para reservar passagens nos trens disponíveis.

5. **Listar Reservas**: Visualize suas reservas atuais.

6. **Cancelar Reserva**: Se necessário, cancele uma reserva existente.

7. **Logout**: Faça logout da sua conta para encerrar a sessão.

## Melhorias Futuras

- **Segurança das Senhas**: Implementar hashing de senhas para melhorar a segurança.
- **Validação de Dados**: Melhorar a validação das entradas do usuário.
- **Interface Gráfica**: Desenvolver uma interface gráfica para melhorar a experiência do usuário.
- **Banco de Dados**: Migrar de um arquivo JSON para um banco de dados relacional ou não relacional.
- **Notificações**: Implementar notificações via e-mail ou SMS para confirmações de reserva.
- **Testes Automatizados**: Adicionar testes unitários para garantir a qualidade do código.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests no repositório do projeto.

---

**Nota**: Este documento visa fornecer uma visão geral completa do projeto, facilitando a compreensão e o uso do sistema por novos desenvolvedores e usuários. Para dúvidas ou sugestões, entre em contato com os mantenedores do projeto.
