# 🛡️ Sentinel AI — Agente de Apoio à Triagem de Fraudes Bancárias

## Contexto

Equipes de prevenção a fraudes em instituições financeiras precisam avaliar grandes volumes de transações — Pix, transferências, pagamentos e outras movimentações — para identificar comportamentos fora do padrão. Esse processo costuma ser manual, demorado e sujeito à variação de experiência entre analistas.

O **Sentinel AI** é um agente construído com IA Generativa para apoiar essa triagem: ele analisa os dados de uma transação, identifica sinais de atenção com base em uma base de conhecimento estruturada, classifica a prioridade do caso e recomenda próximos passos de verificação — sem nunca confirmar fraude, acusar clientes ou tomar decisões automáticas. A decisão final permanece sempre sob responsabilidade humana.

Este projeto nasceu como adaptação do desafio ["Agente Financeiro Inteligente com IA Generativa"](https://github.com/digitalinnovationone), da DIO, redirecionado especificamente para o caso de uso de **prevenção a fraudes bancárias**.

> [!IMPORTANT]
> Todos os dados utilizados neste projeto (`data/`) são fictícios e foram criados exclusivamente para fins acadêmicos. Nenhuma informação pessoal real, credencial bancária ou regra interna de instituição financeira foi utilizada.

---

## O Que Este Projeto Entrega

### 1. Documentação do Agente

Define o caso de uso, a persona ("Sentinel AI"), a arquitetura (fluxo de dados, integração com a base de conhecimento) e as estratégias de segurança e anti-alucinação.

📄 [`docs/01-documentacao-agente.md`](./docs/01-documentacao-agente.md)

---

### 2. Base de Conhecimento

A base de conhecimento fictícia usada pelo Sentinel para triagem de sinais de atenção em transações bancárias:

| Arquivo | Formato | Descrição |
|---------|---------|-----------|
| `sinais_atencao.json` | JSON | Catálogo de sinais de atenção (`SA001`–`SA010`) e campos relevantes para cada um |
| `procedimentos.csv` | CSV | Ações e verificações recomendadas para cada sinal |
| `exemplos_casos.json` | JSON | Casos fictícios (`CT001`–`CT006`) usados em testes funcionais e de segurança |
| `glossario.md` | Markdown | Padronização de termos e linguagem não acusatória do agente |

📄 [`docs/02-base-conhecimento.md`](./docs/02-base-conhecimento.md)

---

### 3. Prompts do Agente

System prompt completo do Sentinel AI, exemplos de interação baseados nos casos de teste reais e tratamento de edge cases (perguntas fora do escopo, tentativas de obter dados sensíveis, tentativas de indução a acusação e dados insuficientes).

📄 [`docs/03-prompts.md`](./docs/03-prompts.md)

---

### 4. Aplicação Funcional

Protótipo do chatbot de triagem, com integração a um LLM e conexão com a base de conhecimento.

📁 [`src/`](./src/)

---

### 5. Avaliação e Métricas

Metodologia de avaliação, cenários de teste (baseados em `exemplos_casos.json`) e registro de resultados reais dos testes executados, incluindo taxa de alucinação, resistência a manipulação e fidelidade à base de conhecimento.

📄 [`docs/04-metricas.md`](./docs/04-metricas.md)

---

### 6. Pitch

Roteiro de pitch de 3 minutos apresentando o problema, a solução, a demonstração e o diferencial do Sentinel AI.

📄 [`docs/05-pitch.md`](./docs/05-pitch.md)

---

## Ferramentas Sugeridas

| Categoria | Ferramentas |
|-----------|-------------|
| **LLMs** | [Claude](https://claude.ai/), [ChatGPT](https://chat.openai.com/), [Gemini](https://gemini.google.com/), [Copilot](https://copilot.microsoft.com/), [Ollama](https://ollama.ai/) |
| **Desenvolvimento** | [Streamlit](https://streamlit.io/), [Gradio](https://www.gradio.app/), [Google Colab](https://colab.research.google.com/) |
| **Orquestração** | [LangChain](https://www.langchain.com/), [LangFlow](https://www.langflow.org/), [CrewAI](https://www.crewai.com/) |
| **Diagramas** | [Mermaid](https://mermaid.js.org/), [Draw.io](https://app.diagrams.net/), [Excalidraw](https://excalidraw.com/) |
| **Observabilidade** | [LangWatch](https://langwatch.ai/), [Langfuse](https://langfuse.com/) |

---

## Estrutura do Repositório

```
📁 ai-anti-fraud-analyst/
│
├── 📄 README.md
│
├── 📁 data/                          # Base de conhecimento fictícia do Sentinel
│   ├── sinais_atencao.json           # Catálogo de sinais de atenção (SA001-SA010)
│   ├── procedimentos.csv             # Ações recomendadas por sinal
│   ├── exemplos_casos.json           # Casos fictícios de teste (CT001-CT006)
│   ├── glossario.md                  # Linguagem padronizada e não acusatória
│   └── README.md
│
├── 📁 docs/                          # Documentação do projeto
│   ├── 01-documentacao-agente.md     # Caso de uso, persona e arquitetura do Sentinel
│   ├── 02-base-conhecimento.md       # Estratégia de dados e integração
│   ├── 03-prompts.md                 # System prompt, cenários e edge cases
│   ├── 04-metricas.md                # Testes, resultados e métricas de avaliação
│   └── 05-pitch.md                   # Roteiro do pitch
│
├── 📁 src/                           # Código da aplicação
│   └── README.md                     # (estrutura sugerida da aplicação)
│
├── 📁 assets/                        # Imagens, diagramas e roteiro de referência
│   └── RoteiroLab.md
│
└── 📁 examples/                      # Referências e exemplos
    └── README.md
```

---

## Limitações e Avisos

O Sentinel AI é uma ferramenta de **apoio à triagem**, não um sistema de decisão autônoma:

- não confirma que uma pessoa ou empresa cometeu fraude;
- não bloqueia, aprova, recusa ou cancela transações;
- não substitui o trabalho de investigadores, analistas ou áreas de segurança;
- não solicita nem processa senhas, tokens ou dados completos de cartão/conta;
- não utiliza atributos sensíveis (raça, religião, gênero, orientação sexual, etc.) na análise;
- toda conclusão deve passar por avaliação humana.

Detalhes completos das limitações declaradas estão em [`docs/01-documentacao-agente.md`](./docs/01-documentacao-agente.md).

---

## Dicas Finais

1. **Comece pelo prompt:** o system prompt em `docs/03-prompts.md` é a base do comportamento do Sentinel.
2. **Use os dados mockados:** `sinais_atencao.json`, `procedimentos.csv` e `exemplos_casos.json` já garantem consistência e evitam problemas com dados sensíveis.
3. **Foque na segurança:** em prevenção a fraudes, alucinação e acusação indevida são inaceitáveis.
4. **Teste cenários reais:** use os casos `CT001`–`CT006` e crie variações para validar o agente antes de qualquer demonstração.
5. **Seja direto no pitch:** 3 minutos passam rápido, vá ao ponto.
