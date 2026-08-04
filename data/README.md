# Pasta `data`

Esta pasta contém a base de conhecimento fictícia utilizada pelo **Sentinel**, agente acadêmico de apoio à triagem de possíveis fraudes em transações bancárias.

## Arquivos

| Arquivo | Finalidade |
|---|---|
| `sinais_atencao.json` | Catálogo de sinais de atenção e campos relevantes |
| `procedimentos.csv` | Ações e verificações sugeridas para cada sinal |
| `exemplos_casos.json` | Casos fictícios para testes funcionais e de segurança |
| `glossario.md` | Padronização de termos e linguagem do agente |
| `README.md` | Documentação desta pasta |

## Como utilizar

1. Carregue `sinais_atencao.json` e `procedimentos.csv` na inicialização da aplicação.
2. Inclua os sinais e procedimentos relevantes no contexto do agente.
3. Use `exemplos_casos.json` para validar as respostas.
4. Utilize `glossario.md` para manter linguagem explicável e não acusatória.

## Estrutura esperada

```text
data/
├── README.md
├── sinais_atencao.json
├── procedimentos.csv
├── exemplos_casos.json
└── glossario.md
```

## Cuidados

- Todos os dados são fictícios e foram criados para fins acadêmicos.
- Nenhum sinal isolado confirma fraude.
- O agente não deve bloquear transações nem acusar clientes.
- Dados pessoais reais não devem ser usados na demonstração.
- A decisão final deve ser realizada por um profissional responsável.
