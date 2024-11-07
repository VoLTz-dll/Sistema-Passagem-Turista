# database.py

import json
import os

USUARIOS_DB = os.path.join("data", "usuarios.json")

def carregar_usuarios():
    if os.path.exists(USUARIOS_DB):
        with open(USUARIOS_DB, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}
    return {}

def salvar_usuarios(usuarios):
    os.makedirs(os.path.dirname(USUARIOS_DB), exist_ok=True)
    with open(USUARIOS_DB, "w") as file:
        json.dump(usuarios, file, indent=4)
