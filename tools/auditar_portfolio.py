"""Auditoria estática e reproduzível dos notebooks e CSV locais.
Execute da raiz: python tools/auditar_portfolio.py
Não executa modelos nem realiza downloads.
"""
from pathlib import Path
import ast
import csv
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
PROJECTS = [
    ("01_pre_processamento_eda", "trabalho_02_nova_zelandia.ipynb", "4_New-Zealand.csv"),
    ("02_agrupamento", "trabalho_03_agrupamento.ipynb", "trabalho3_dados_4.csv"),
    ("03_regras_associacao", "trabalho_04_regras_associacao.ipynb", "trabalho4_dados_4.csv"),
    ("04_classificacao", "trabalho_05_classificacao.ipynb", "maternal_health_risk_subbase_4.csv"),
    ("05_regressao", "trabalho_07_petr4_brent.ipynb", None),
]
errors = 0
for folder, notebook, csv_name in PROJECTS:
    path = ROOT / folder / notebook
    try:
        doc = json.loads(path.read_text(encoding="utf-8"))
        assert doc.get("nbformat") == 4
        cells = doc["cells"]
        assert cells and all(c.get("cell_type") in ("markdown", "code", "raw") for c in cells)
        code = [c for c in cells if c["cell_type"] == "code"]
        assert code
        # Detecta sintaxe inválida em células Python; ignora magias Jupyter.
        invalid = []
        for i, cell in enumerate(cells, 1):
            if cell["cell_type"] != "code":
                continue
            source = "".join(cell.get("source", []))
            if any(line.lstrip().startswith(("%", "!")) for line in source.splitlines()):
                continue
            try:
                ast.parse(source)
            except SyntaxError as exc:
                invalid.append(f"célula {i}: {exc.msg}")
        if invalid:
            raise ValueError("; ".join(invalid[:5]))
        print(f"OK notebook: {folder} ({len(cells)} células, {len(code)} de código)")
    except (OSError, ValueError, KeyError, AssertionError) as exc:
        errors += 1
        print(f"ERRO notebook: {folder}: {exc}")
    if csv_name is not None:
        data_path = ROOT / folder / "data" / csv_name
        if not data_path.is_file():
            label = "ERRO"
            if label == "ERRO":
                errors += 1
            print(f"{label} dados: {data_path.relative_to(ROOT)} ausente")
        else:
            try:
                with data_path.open(encoding="utf-8-sig", newline="") as f:
                    reader = csv.reader(f)
                    header = next(reader)
                    assert header and len(header) > 1
                    count = sum(1 for _ in reader)
                if folder == "01_pre_processamento_eda":
                    sha_esperado = "2284f8d6c9a45069fecee324c158eda49f6cf02791496ecdded101d35b174c20"
                    sha_obtido = hashlib.sha256(data_path.read_bytes()).hexdigest()
                    if sha_obtido != sha_esperado or count != 25006 or len(header) != 16:
                        errors += 1
                        print(f"ERRO base original: hash={sha_obtido}, linhas={count}, colunas={len(header)}")
                    else:
                        print("OK base original: SHA-256, 25.006 linhas, 16 colunas")
                print(f"OK dados: {csv_name} ({count} linhas de dados)")
            except (OSError, UnicodeError, StopIteration, AssertionError) as exc:
                errors += 1
                print(f"ERRO dados: {csv_name}: {exc}")
print(f"\nAuditoria concluída: {errors} erro(s).")
sys.exit(1 if errors else 0)
