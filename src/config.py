"""
Configurações do Sentinel AI (execução via Ollama local).

Centraliza a conexão com o servidor Ollama, a escolha automática de
modelo e os caminhos para a base de conhecimento (pasta `data/`).
"""

import os
from pathlib import Path

import requests

# --- Ollama ---
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
OLLAMA_CHAT_URL = f"{OLLAMA_HOST}/api/chat"
OLLAMA_TAGS_URL = f"{OLLAMA_HOST}/api/tags"
REQUEST_TIMEOUT_S = int(os.getenv("OLLAMA_TIMEOUT_S", "120"))

# Ordem de preferência quando SENTINEL_MODEL não é definido explicitamente.
MODELOS_PREFERIDOS = ["llama3.2:3b", "gpt-oss", "deepseek-r1:8b"]


def escolher_modelo_ollama() -> str:
    """
    Decide qual modelo Ollama usar, nesta ordem:
    1) variável de ambiente SENTINEL_MODEL, se definida;
    2) primeiro modelo da lista de preferidos que já estiver instalado
       localmente (consultando `GET /api/tags`);
    3) fallback para "llama3.2:3b".
    """
    modelo_env = os.getenv("SENTINEL_MODEL")
    if modelo_env:
        return modelo_env

    try:
        resposta = requests.get(OLLAMA_TAGS_URL, timeout=5)
        resposta.raise_for_status()
        modelos_instalados = resposta.json().get("models", [])
        disponiveis = {m.get("name", "").split(":")[0] for m in modelos_instalados}
        for nome in MODELOS_PREFERIDOS:
            if nome.split(":")[0] in disponiveis:
                return nome
    except requests.RequestException:
        pass

    return "llama3.2:3b"


MODEL_NAME = escolher_modelo_ollama()


def timeout_para_modelo(modelo: str) -> int:
    """Modelos de raciocínio (ex.: deepseek-r1) costumam demorar mais no primeiro token."""
    if "deepseek-r1" in modelo.lower():
        return max(REQUEST_TIMEOUT_S, 240)
    return REQUEST_TIMEOUT_S


# --- Caminhos da base de conhecimento (pasta `data/` na raiz do repo) ---
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

SINAIS_ATENCAO_PATH = DATA_DIR / "sinais_atencao.json"
PROCEDIMENTOS_PATH = DATA_DIR / "procedimentos.csv"
EXEMPLOS_CASOS_PATH = DATA_DIR / "exemplos_casos.json"
GLOSSARIO_PATH = DATA_DIR / "glossario.md"

# --- Identidade do agente ---
NOME_AGENTE = "Sentinel AI"
