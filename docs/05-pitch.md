# Pitch (3 minutos)

> [!Tip]
> Apresentação completa sobre a solução está disponível na pasta `assets`.

## Roteiro Sugerido

### 1. O Problema (30 seg)
> Qual dor do cliente você resolve?

Equipes de prevenção a fraudes bancárias recebem um volume enorme de alertas de transações — Pix, transferências, pagamentos — e precisam decidir rapidamente quais merecem atenção prioritária. Essa triagem é hoje manual e não padronizada: a qualidade da análise varia conforme a experiência de cada analista, informações relevantes às vezes passam despercebidas, e transações de alto risco podem não ser priorizadas a tempo, enquanto operações de baixo risco consomem tempo desnecessário da equipe.

### 2. A Solução (1 min)
> Como seu agente resolve esse problema?

O **Sentinel AI** é um agente de apoio à triagem de fraudes bancárias. Ele recebe os dados de uma transação (valor, horário, dispositivo, favorecido, histórico do cliente etc.), consulta uma base de conhecimento de sinais de atenção e procedimentos, e devolve uma análise padronizada: resumo do caso, nível de atenção (Baixo, Médio, Alto ou Crítico), sinais identificados com justificativa, informações ausentes ou contraditórias e próximas ações recomendadas.

O Sentinel nunca confirma fraude, nunca acusa o cliente e nunca bloqueia ou aprova transações — ele existe para acelerar e padronizar a triagem, mantendo a decisão final sempre com um profissional humano.

### 3. Demonstração (1 min)
> Mostre o agente funcionando (pode ser gravação de tela)

Gravação de tela mostrando 2-3 casos reais da base de testes (`data/exemplos_casos.json`):
- Um caso de alto risco (Pix de valor muito acima do padrão, dispositivo novo, favorecido recém-cadastrado) — mostrando o agente identificando os sinais e classificando corretamente o nível de atenção;
- Um caso de baixo risco (pagamento dentro do padrão do cliente) — mostrando que o agente não gera alarme falso;
- Uma tentativa de manipulação (pedido para "confirmar a fraude" ou "encerrar a conta") — mostrando o agente recusando e mantendo a decisão sob responsabilidade humana.

### 4. Diferencial e Impacto (30 seg)
> Por que essa solução é inovadora e qual é o impacto dela na sociedade?

Diferente de sistemas de regras fixas, o Sentinel explica o *porquê* de cada sinal em linguagem clara e não acusatória, o que acelera o trabalho do analista sem tirar dele a decisão final. O impacto é duplo: reduz o tempo gasto em triagens de baixo risco, liberando a equipe para casos que realmente importam, e reduz o risco de acusações indevidas contra clientes — já que o agente é construído para nunca tratar um indício isolado como prova de fraude.

---

## Checklist do Pitch

- [ ] Duração máxima de 3 minutos
- [ ] Problema claramente definido
- [ ] Solução demonstrada na prática
- [ ] Diferencial explicado
- [ ] Áudio e vídeo com boa qualidade

---

## Link do Vídeo

> Cole aqui o link do seu pitch (YouTube, Loom, Google Drive, etc.)

[Link do vídeo]
