"""
Sentinel AI — protótipo funcional em Streamlit (execução via Ollama local).

Interface de chat para apoio à triagem de possíveis sinais de fraude em
transações bancárias.
"""

import streamlit as st

import config
from agente import SentinelAgent, carregar_exemplos_casos

st.set_page_config(
    page_title=config.NOME_AGENTE,
    page_icon="🛡️",
    layout="centered",
)

st.title(f"🛡️ {config.NOME_AGENTE}")
st.caption(
    "Apoio à triagem de possíveis sinais de fraude em transações bancárias. "
    "As respostas não confirmam fraude e não substituem a decisão humana."
)

# --- Inicialização do agente (uma vez por sessão) ---
if "agente" not in st.session_state:
    st.session_state.agente = SentinelAgent()

if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

# --- Barra lateral: casos de teste prontos e status do modelo ---
with st.sidebar:
    st.header("Casos de teste")
    st.caption(
        "Carregue um caso fictício de `data/exemplos_casos.json` para "
        "testar rapidamente o agente."
    )

    casos = carregar_exemplos_casos()
    opcoes = {f"{caso['id_caso']} — {caso['titulo']}": caso for caso in casos}
    escolha = st.selectbox("Selecione um caso:", ["—"] + list(opcoes.keys()))

    if escolha != "—" and st.button("Carregar caso selecionado"):
        caso = opcoes[escolha]
        descricao = "\n".join(
            f"{chave}: {valor}" for chave, valor in caso["entrada"].items()
        )
        st.session_state.mensagens.append({"role": "user", "content": descricao})
        st.rerun()

    st.divider()
    if st.button("Limpar conversa"):
        st.session_state.mensagens = []
        st.rerun()

    st.divider()
    st.caption(f"🧠 Modelo local (Ollama): `{st.session_state.agente.modelo}`")
    st.caption(f"🔌 Servidor: `{config.OLLAMA_HOST}`")
    st.caption(
        "⚠️ Todos os dados usados neste protótipo são fictícios e "
        "destinados exclusivamente a fins acadêmicos."
    )

# --- Histórico da conversa ---
for mensagem in st.session_state.mensagens:
    with st.chat_message(mensagem["role"]):
        st.markdown(mensagem["content"])

# --- Entrada do usuário ---
entrada = st.chat_input(
    "Descreva a transação (valor, horário, dispositivo, favorecido, histórico...)"
)

if entrada:
    st.session_state.mensagens.append({"role": "user", "content": entrada})
    with st.chat_message("user"):
        st.markdown(entrada)

    with st.chat_message("assistant"):
        with st.spinner(f"Analisando sinais de atenção com {st.session_state.agente.modelo}..."):
            resposta = st.session_state.agente.analisar(st.session_state.mensagens)
            st.markdown(resposta)

    st.session_state.mensagens.append({"role": "assistant", "content": resposta})
