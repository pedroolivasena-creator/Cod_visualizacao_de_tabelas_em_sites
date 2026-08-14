from pathlib import Path
import requests

XLS_URL = "https://ftp.ibge.gov.br/Estimativas_de_Populacao/Estimativas_2025/POP2025_20260113.xls"

response = requests.get(XLS_URL, stream=True, timeout=5)
response.raise_for_status()

outdir = Path(r"C:\Users\Usuario\PycharmProjects\PythonProject\data\raw")
outdir.mkdir(parents=True, exist_ok=True)
XLS_PATH = outdir / "pop_ibge_2025.XLS"

with open(XLS_PATH, "wb") as f:
    for chunk in response.iter_content(chunk_size=1024):
        if chunk: f.write(chunk)

print("Arquivo CSV salvo em:", XLS_PATH)
