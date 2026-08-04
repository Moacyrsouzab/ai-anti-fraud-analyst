# Base de Conhecimento

## Dados Utilizados

O Sentinel utiliza os arquivos da pasta `data` como base de conhecimento para apoiar a triagem inicial de possíveis sinais de atenção em transações bancárias.

Todos os dados utilizados neste projeto são fictícios e foram criados exclusivamente para fins acadêmicos. Nenhuma informação pessoal real, dado de cliente, credencial bancária ou regra interna de instituição financeira foi utilizada.

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `sinais_atencao.json` | JSON | Armazenar os sinais de atenção que podem ser identificados durante a análise de uma transação bancária |
| `procedimentos.csv` | CSV | Relacionar cada sinal de atenção às verificações e aos próximos passos sugeridos |
| `exemplos_casos.json` | JSON | Disponibilizar casos fictícios para testar e avaliar o comportamento do agente |
| `glossario.md` | Markdown | Padronizar os principais termos utilizados pelo Sentinel |
| `README.md` | Markdown | Documentar a finalidade, a estrutura e as limitações da pasta `data` |

> [!IMPORTANT]
> Os sinais presentes na base não representam confirmação de fraude. Eles apenas indicam situações que podem justificar uma análise complementar pelo profissional responsável.

---

## Adaptações nos Dados

Os dados do projeto de referência estavam relacionados a um assistente financeiro. Para o desenvolvimento do Sentinel, os arquivos foram modificados e expandidos para representar situações relacionadas à prevenção a fraudes em transações bancárias.

As principais adaptações realizadas foram:

- Inclusão de informações relacionadas a Pix, transferências, pagamentos, contas, favorecidos, dispositivos, localização, horários e histórico transacional;
- Criação de sinais de atenção específicos para valores fora do padrão, movimentações em horários incomuns, uso de novo dispositivo, localização divergente, favorecido recém-cadastrado, tentativas consecutivas e aumento repentino da frequência de transações;
- Inclusão de orientações de análise e próximos passos para cada sinal cadastrado;
- Criação de casos fictícios para testar respostas corretas, ausência de informações e tentativas de induzir o agente a realizar acusações ou bloqueios automáticos;
- Inclusão de observações de cautela para evitar que um sinal seja tratado como prova de fraude;
- Criação de um glossário para manter a linguagem do agente padronizada, explicável e não acusatória.

A base foi construída manualmente e possui finalidade demonstrativa. Ela não representa todas as regras, procedimentos ou situações possíveis em uma operação bancária real.

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
3. Descrição da transação informada pelo usuário.

As instruções fixas orientam o agente a:

- Não confirmar fraudes;
- Não acusar pessoas;
- Não inventar informações;
- Utilizar somente os critérios disponíveis na base;
- Informar quando os dados forem insuficientes;
- Explicar os sinais identificados;
- Sugerir próximos passos;
- Não bloquear, cancelar ou aprovar transações automaticamente;
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
possíveis sinais de fraude em transações bancárias.

Utilize somente a base de conhecimento apresentada.
Não confirme fraudes, não bloqueie transações e não invente informações.

Base de conhecimento:

{base_formatada}

Caso informado pelo usuário:

{descricao_caso}

Apresente:
1. Resumo do caso;
2. Nível de atenção;
3. Sinais de atenção;
4. Informações ausentes ou contraditórias;
5. Próximos passos;
6. Limitações da análise.
'''
```

Nesta primeira versão, toda a base é incluída no contexto porque possui poucos registros.

Em uma evolução futura, o Sentinel poderá utilizar uma estratégia de RAG para consultar dinamicamente apenas os sinais e procedimentos mais relacionados à transação analisada.

---

## Exemplo de Contexto Montado

O exemplo abaixo mostra como os dados podem ser formatados antes de serem enviados ao agente.

```text
Identidade do Agente:
- Nome: Sentinel
- Função: Apoiar a triagem inicial de possíveis sinais de fraude
- Escopo: Transações bancárias
- Limitação: Não confirmar fraude, não bloquear transações e não substituir a decisão humana

Sinais de Atenção Disponíveis:

Sinal SA001:
- Categoria: Comportamento transacional
- Nome: Valor acima do padrão do cliente
- Descrição: O valor da transação é significativamente superior aos valores normalmente movimentados pela conta.
- Nível de atenção: Médio
- Orientações:
  - Comparar o valor com o histórico recente do cliente;
  - Verificar se existem transações semelhantes anteriores;
  - Confirmar se houve alteração recente no perfil de movimentação.
- Observação: Uma transação de valor elevado pode ser legítima e deve ser contextualizada.

Sinal SA002:
- Categoria: Dispositivo e acesso
- Nome: Transação realizada em novo dispositivo
- Descrição: A operação foi iniciada em um dispositivo ainda não reconhecido no histórico da conta.
- Nível de atenção: Médio
- Orientações:
  - Verificar a data do primeiro acesso do dispositivo;
  - Consultar alterações cadastrais ou de senha recentes;
  - Confirmar se houve autenticação adicional.
- Observação: A troca de aparelho pode ser legítima e não representa fraude isoladamente.

Sinal SA003:
- Categoria: Favorecido
- Nome: Favorecido recém-cadastrado
- Descrição: A transferência foi destinada a um favorecido adicionado pouco antes da operação.
- Nível de atenção: Médio
- Orientações:
  - Verificar o intervalo entre o cadastro do favorecido e a transação;
  - Comparar com o histórico de destinatários da conta;
  - Confirmar se ocorreram outras transações para o mesmo favorecido.
- Observação: Um novo favorecido pode representar uma operação legítima.

Sinal SA004:
- Categoria: Horário e frequência
- Nome: Sequência de transações em horário incomum
- Descrição: Foram realizadas várias transações em curto intervalo e fora do horário habitual do cliente.
- Nível de atenção: Alto
- Orientações:
  - Verificar a quantidade e o intervalo entre as operações;
  - Comparar o horário com o comportamento histórico da conta;
  - Consultar tentativas recusadas ou falhas de autenticação anteriores.
- Observação: O conjunto de sinais aumenta a necessidade de validação, mas não confirma fraude.

Caso Informado:
- Foi realizado um Pix de R$ 8.500,00 às 02h18;
- O valor médio das transações do cliente é de aproximadamente R$ 450,00;
- A operação foi feita em um novo dispositivo;
- O favorecido foi cadastrado dez minutos antes da transferência;
- Houve outras duas tentativas de Pix no mesmo período.

Resposta Esperada:
- Resumir as informações fornecidas;
- Classificar o nível de atenção com base na combinação dos sinais;
- Identificar os sinais SA001, SA002, SA003 e SA004;
- Explicar por que cada sinal merece verificação;
- Informar os dados que ainda precisam ser consultados;
- Sugerir próximos passos de validação;
- Reforçar que a análise não representa confirmação de fraude e não autoriza bloqueio automático.
```
