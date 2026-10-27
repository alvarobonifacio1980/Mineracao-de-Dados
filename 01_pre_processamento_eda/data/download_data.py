from pathlib import Path
import pandas as pd

URL = "https://data.insideairbnb.com/new-zealand/2025-01-05/visualisations/listings.csv"
DESTINO = Path(__file__).with_name("4_New-Zealand.csv")

df = pd.read_csv(URL)
df.to_csv(DESTINO, index=False)
print(f"Arquivo salvo em {DESTINO} com {len(df):,} registros e {df.shape[1]} colunas.")
