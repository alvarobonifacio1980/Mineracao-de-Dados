from pathlib import Path
from urllib.request import urlretrieve

# Snapshot público do Inside Airbnb usado como referência para a Nova Zelândia.
URL = "https://data.insideairbnb.com/new-zealand/2025-01-05/visualisations/listings.csv"
DESTINO = Path(__file__).resolve().parent / "4_New-Zealand.csv"

print(f"Baixando: {URL}")
urlretrieve(URL, DESTINO)
print(f"Arquivo salvo em: {DESTINO}")
print("Observação: snapshots podem diferir do arquivo acadêmico original.")
