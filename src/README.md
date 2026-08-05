# Código da Aplicação

Esta pasta contém o código do **Sentinel AI**, o protótipo funcional do agente de apoio à triagem de fraudes bancárias — executado com um **modelo local via Ollama** (sem depender de API externa).

## Estrutura

```
src/
├── app.py              # Interface de chat em Streamlit
├── agente.py           # Carregamento da base de conhecimento e chamada ao Ollama
├── config.py           # Configurações (host do Ollama, seleção de modelo, timeouts)
└── requirements.txt    # Dependências
```

O agente lê a base de conhecimento diretamente da pasta [`data/`](../data/) na raiz do repositório (`sinais_atencao.json`, `procedimentos.csv`, `glossario.md`) e a formata automaticamente dentro do system prompt a cada inicialização.

## Pré-requisitos

1. **Instalar o Ollama:** [ollama.com/download](https://ollama.com/download)
2. **Iniciar o serviço:**
   ```bash
   ollama serve
   ```
3. **Baixar ao menos um modelo:**
   ```bash
   ollama pull llama3.2:3b
   ```

## Como Rodar

```bash
# 1. Entrar na pasta src
cd src

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Rodar a aplicação
streamlit run app.py
```

A aplicação abre em `http://localhost:8501`. Na barra lateral é possível ver qual modelo está em uso e carregar diretamente um dos casos fictícios de `data/exemplos_casos.json` (`CT001`–`CT006`) para testar rapidamente o comportamento do agente.

## Como Funciona

1. `config.py` decide qual modelo Ollama usar — nesta ordem: variável de ambiente `SENTINEL_MODEL` (se definida), depois o primeiro modelo já instalado dentre `llama3.2:3b`, `gpt-oss` ou `deepseek-r1:8b`, e por fim o fallback `llama3.2:3b`. Também ajusta o timeout automaticamente para modelos de raciocínio mais lentos (ex.: `deepseek-r1`).
2. `agente.py` lê `sinais_atencao.json`, `procedimentos.csv` e `glossario.md`, monta o system prompt completo do Sentinel (regras de segurança + base de conhecimento formatada) e expõe a classe `SentinelAgent`, que envia o histórico da conversa para `POST /api/chat` do Ollama.
3. `app.py` é a interface em Streamlit: mantém o histórico da conversa na sessão, exibe o chat, mostra o modelo em uso na barra lateral e permite carregar casos de teste prontos.

Se o Ollama não estiver rodando, travar ou o modelo não estiver instalado, o agente devolve uma mensagem de erro clara na própria conversa (timeout, erro HTTP ou falha de conexão) em vez de quebrar a aplicação.

> [!IMPORTANT]
> Nunca use dados reais de clientes, contas ou transações neste protótipo — apenas os dados fictícios já disponíveis em `data/exemplos_casos.json` ou variações fictícias criadas por você.

## Personalizando

- Para forçar um modelo específico, exporte a variável de ambiente `SENTINEL_MODEL` antes de rodar (ex.: `export SENTINEL_MODEL=gpt-oss`).
- Para apontar para um Ollama remoto, exporte `OLLAMA_HOST` (ex.: `export OLLAMA_HOST=http://192.168.0.10:11434`).
- Para ajustar o tempo limite de resposta, exporte `OLLAMA_TIMEOUT_S` (padrão: `120`; modelos `deepseek-r1` usam no mínimo `240` automaticamente).
- Para usar outro provedor de LLM (ex.: API da Anthropic ou OpenAI), adapte o método `analisar()` em `agente.py` — a montagem do system prompt (`montar_system_prompt()`) não precisa mudar.
