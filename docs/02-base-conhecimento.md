# Base de Conhecimento

## Dados Utilizados

O Sentinel utiliza os arquivos da pasta `data` como base de conhecimento para apoiar a triagem inicial de possíveis sinais de atenção em sinistros de automóvel.

Todos os dados utilizados neste projeto são fictícios e foram criados exclusivamente para fins acadêmicos. Nenhuma informação pessoal real, dado de cliente ou regra interna de seguradora foi utilizada.

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `sinais_atencao.json` | JSON | Armazenar os sinais de atenção que podem ser identificados durante a análise do sinistro |
| `procedimentos.csv` | CSV | Relacionar cada sinal de atenção às verificações e aos próximos passos sugeridos |
| `exemplos_casos.json` | JSON | Disponibilizar casos fictícios para testar e avaliar o comportamento do agente |
| `glossario.md` | Markdown | Padronizar os principais termos utilizados pelo Sentinel |
| `README.md` | Markdown | Documentar a finalidade, a estrutura e as limitações da pasta `data` |

> [!IMPORTANT]
> Os sinais presentes na base não representam confirmação de fraude. Eles apenas indicam situações que podem justificar uma análise complementar pelo profissional responsável.

---

## Adaptações nos Dados

Os dados do projeto de referência estavam relacionados a um assistente financeiro. Para o desenvolvimento do Sentinel, os arquivos foram modificados e expandidos para representar situações relacionadas à prevenção a fraudes em sinistros de automóvel.

As principais adaptações realizadas foram:

- Substituição de dados financeiros por informações relacionadas a apólices, veículos, condutores, terceiros, documentos e históricos de sinistros;
- Criação de sinais de atenção específicos para contratação recente, divergências cadastrais, documentação pendente, recorrência de sinistros, inconsistências em relatos e incompatibilidade entre dinâmica e danos;
- Inclusão de orientações de análise e próximos passos para cada sinal cadastrado;
- Criação de casos fictícios para testar respostas corretas, ausência de informações e tentativas de induzir o agente a realizar acusações;
- Inclusão de observações de cautela para evitar que um sinal seja tratado como prova de fraude;
- Criação de um glossário para manter a linguagem do agente padronizada, explicável e não acusatória.

A base foi construída manualmente e possui finalidade demonstrativa. Ela não representa todas as regras, procedimentos ou situações possíveis em uma operação real de seguros.

---

## Estratégia de Integração

### Como os dados são carregados?

Os arquivos JSON e CSV são carregados no início da execução da aplicação.

O arquivo `sinais_atencao.json` é lido com a biblioteca `json` do Python, enquanto o arquivo `procedimentos.csv` pode ser carregado com a biblioteca `pandas`.

O arquivo `glossario.md` é lido como texto e pode ser incluído no contexto do agente para orientar a utilização correta dos termos.

Como a base de conhecimento desta primeira versão é pequena, os dados podem ser carregados integralmente no início da sessão.

Exemplo simplificado:

```python
import json
import pandas as pd


with open(
    "data/sinais_atencao.json",
    "r",
    encoding="utf-8"
) as arquivo:
    sinais_atencao = json.load(arquivo)


procedimentos = pd.read_csv(
    "data/procedimentos.csv"
).to_dict(orient="records")
```

Em uma aplicação desenvolvida com Streamlit, o carregamento pode utilizar cache para evitar a leitura dos arquivos a cada nova interação:

```python
import json
import streamlit as st


@st.cache_data
def carregar_base(caminho: str) -> list[dict]:
    with open(caminho, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)
```

### Como os dados são usados no prompt?

Os dados são incluídos dinamicamente no contexto enviado ao modelo.

O prompt utilizado pelo Sentinel é composto por três partes:

1. Instruções fixas que definem o comportamento do agente;
2. Base de conhecimento carregada da pasta `data`;
3. Descrição do sinistro informada pelo usuário.

As instruções fixas orientam o agente a:

- Não confirmar fraudes;
- Não acusar pessoas;
- Não inventar informações;
- Utilizar somente os critérios disponíveis na base;
- Informar quando os dados forem insuficientes;
- Explicar os sinais identificados;
- Sugerir próximos passos;
- Manter a decisão final sob responsabilidade humana.

A base de conhecimento é convertida para texto e adicionada ao prompt antes da descrição do caso.

Exemplo simplificado:

```python
import json


base_formatada = json.dumps(
    sinais_atencao,
    ensure_ascii=False,
    indent=2
)

prompt = f'''
Você é o Sentinel, um assistente de apoio à triagem de
possíveis sinais de fraude em sinistros de automóvel.

Utilize somente a base de conhecimento apresentada.
Não confirme fraudes e não invente informações.

Base de conhecimento:

{base_formatada}

Caso informado pelo usuário:

{descricao_caso}

Apresente:
1. Resumo do caso;
2. Sinais de atenção;
3. Informações ausentes;
4. Próximos passos;
5. Limitações da análise.
'''
```

Nesta primeira versão, toda a base é incluída no contexto porque possui poucos registros.

Em uma evolução futura, o Sentinel poderá utilizar uma estratégia de RAG para consultar dinamicamente apenas os sinais e procedimentos mais relacionados ao caso analisado.

---

## Exemplo de Contexto Montado

O exemplo abaixo mostra como os dados podem ser formatados antes de serem enviados ao agente.

```text
Identidade do Agente:
- Nome: Sentinel
- Função: Apoiar a triagem inicial de possíveis sinais de fraude
- Escopo: Sinistros de automóvel
- Limitação: Não confirmar fraude e não substituir a decisão humana

Sinais de Atenção Disponíveis:

Sinal SA001:
- Categoria: Apólice
- Nome: Sinistro próximo ao início da vigência
- Descrição: O sinistro ocorreu pouco tempo após o início da vigência.
- Nível de atenção: Médio
- Orientações:
  - Validar a data de contratação;
  - Confirmar a data de início da vigência;
  - Verificar alterações ou endossos recentes.
- Observação: Este sinal isoladamente não comprova fraude.

Sinal SA002:
- Categoria: Cadastro
- Nome: Divergência entre segurado, proprietário e condutor
- Descrição: As pessoas relacionadas à apólice, à propriedade do veículo e à condução são diferentes.
- Nível de atenção: Médio
- Orientações:
  - Confirmar a relação entre os envolvidos;
  - Consultar os documentos do veículo;
  - Verificar quem utilizava o veículo habitualmente.
- Observação: A divergência pode ser legítima e deve ser contextualizada.

Sinal SA003:
- Categoria: Documentação
- Nome: Documento relevante pendente
- Descrição: Um documento importante para a análise ainda não foi apresentado.
- Nível de atenção: Médio
- Orientações:
  - Verificar se o documento é obrigatório;
  - Solicitar o documento pendente;
  - Comparar o documento com o relato do sinistro.
- Observação: A ausência temporária de um documento não confirma fraude.

Caso Informado:
- O sinistro ocorreu sete dias após o início da vigência;
- O veículo pertence ao pai do segurado;
- Outra pessoa conduzia o veículo no momento da ocorrência;
- O boletim de ocorrência ainda não foi apresentado.

Resposta Esperada:
- Resumir as informações fornecidas;
- Identificar os sinais SA001, SA002 e SA003;
- Explicar por que cada sinal merece verificação;
- Informar os dados que ainda precisam ser consultados;
- Sugerir próximos passos;
- Reforçar que a análise não representa confirmação de fraude.
```
