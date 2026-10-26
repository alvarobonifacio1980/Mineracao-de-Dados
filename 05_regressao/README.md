# Trabalho 07 — Regressão e Séries Temporais

## Problema

Prever a volatilidade futura de cinco pregões da PETR4 e avaliar se informações externas relacionadas ao petróleo acrescentam capacidade preditiva.

## Dados

Este notebook é o mais reprodutível da coleção em termos de aquisição: os dados são obtidos por código a partir de fontes públicas.

Principais fontes:

- PETR4: API brapi;
- Brent: FRED;
- OVX: FRED.

Não é necessário incluir um CSV bruto neste repositório para a execução original, desde que as APIs/fontes estejam disponíveis.

## Metodologia

- retornos logarítmicos;
- volatilidade histórica;
- alvo futuro de cinco pregões;
- baseline HV30;
- regressão com atributos PETR4;
- PETR4 + Brent;
- PETR4 + OVX;
- validação walk-forward;
- controle explícito de disponibilidade temporal das variáveis;
- MAE, RMSE, R² e viés.

## Observação

Resultados podem variar ligeiramente caso os provedores revisem séries históricas ou calendários. O notebook documenta a data da reprodução e as limitações encontradas.
