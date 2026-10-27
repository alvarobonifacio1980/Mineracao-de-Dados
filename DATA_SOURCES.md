# Proveniência, acesso e reprodução dos dados

Este repositório combina **arquivos CSV incluídos**, um **snapshot público recuperável** e **séries adquiridas online**. A existência de acesso público não implica, por si só, licença irrestrita de redistribuição: mantenha a atribuição e confira os termos da fonte primária antes de reutilizar os arquivos.

| Trabalho | Base | Situação no GitHub | Nota de reprodução |
|---|---|---|---|
| 01 — EDA | Inside Airbnb, Nova Zelândia | Arquivo acadêmico original incluído; download alternativo opcional | A base acadêmica original de 25.006 linhas está incluída; snapshots externos podem diferir |
| 02 — Agrupamento | Produção agrícola | `02_agrupamento/data/trabalho3_dados_4.csv` | Cópia do experimento incluída; fonte primária/licença ainda precisam ser identificadas |
| 03 — Associação | Cestas de compras | `03_regras_associacao/data/trabalho4_dados_4.csv` | Cópia do experimento incluída; fonte primária/licença ainda precisam ser identificadas |
| 04 — Classificação | Maternal Health Risk (UCI), subbase | `04_classificacao/data/maternal_health_risk_subbase_4.csv` | Subconjunto de 92 registros; ver termos e citação do dataset UCI |
| 05 — Regressão | PETR4, Brent, OVX | Aquisição por API no notebook | Disponibilidade, histórico ajustado e revisões do provedor podem alterar a reprodução |

## Fontes identificadas

- **Inside Airbnb:** https://insideairbnb.com/get-the-data/ — dados e informações de atribuição/licença. O script de aquisição está em `01_pre_processamento_eda/data/download_data.py`.
- **Maternal Health Risk (UCI):** https://archive.ics.uci.edu/dataset/863/maternal+health+risk
- **PETR4:** https://brapi.dev/ — verificar limites e condições de acesso da API.
- **Brent (DCOILBRENTEU):** https://fred.stlouisfed.org/series/DCOILBRENTEU
- **OVX (OVXCLS):** https://fred.stlouisfed.org/series/OVXCLS

## Como executar

1. Instale as dependências: `python -m pip install -r requirements.txt`.
2. Abra o notebook **dentro da pasta do respectivo trabalho**, para que os caminhos `data/...` sejam resolvidos corretamente.
3. Rode `python tools/auditar_portfolio.py` **a partir da raiz** para conferir integridade estática e CSV locais. A auditoria não substitui a execução completa das análises.
4. O trabalho 01 baixa um snapshot alternativo se o CSV original estiver ausente; a saída deve ser tratada como **nova análise**, não como reprodução exata dos resultados acadêmicos.

## Pendência de proveniência

Os nomes dos arquivos de agrupamento e de associação não são suficientes para identificar com segurança o URL original e a licença aplicável. Até a confirmação, preservar o arquivo de origem, os metadados e esta ressalva; **não atribuir licença CC/UCI sem evidência**. O fato de os CSVs já estarem disponíveis neste repositório não elimina a necessidade de conferir os termos de redistribuição.

**Atualização de 27/10/2026:** o autor forneceu `10_New-Zealand.csv` (23.941 linhas), que pode ser utilizado localmente como alternativa em `01_pre_processamento_eda/data/`, sem ser confundido com o original de 25.006 linhas. As três bases CSV já versionadas de agrupamento, associação e classificação foram confrontadas por SHA de blob Git e são exatamente idênticas aos arquivos fornecidos.

**Base original recuperada:** arquivo `4_New-Zealand.csv` (25.006 × 16), identificado por SHA-256 `2284f8d6c9a45069fecee324c158eda49f6cf02791496ecdded101d35b174c20`, verificado em 27/10/2026. **Publicado no GitHub** em `01_pre_processamento_eda/data/4_New-Zealand.csv`. O notebook valida esse hash ao encontrá-lo localmente; o arquivo alternativo não é equivalente.
