"""
Configurações do Sentinel AI.

Carrega variáveis de ambiente e centraliza os caminhos para a base de
conhecimento (pasta `data/`) utilizada pelo agente.
"""

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# --- Anthropic API ---
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
MODEL_NAME = os.getenv("SENTINEL_MODEL", "claude-sonnet-4-6")
MAX_TOKENS = int(os.getenv("SENTINEL_MAX_TOKENS", "1500"))

# --- Caminhos da base de conhecimento (pasta `data/` na raiz do repo) ---
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

SINAIS_ATENCAO_PATH = DATA_DIR / "sinais_atencao.json"
PROCEDIMENTOS_PATH = DATA_DIR / "procedimentos.csv"
EXEMPLOS_CASOS_PATH = DATA_DIR / "exemplos_casos.json"
GLOSSARIO_PATH = DATA_DIR / "glossario.md"

# --- Identidade do agente ---
NOME_AGENTE = "Sentinel AI"
