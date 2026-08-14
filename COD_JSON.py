from pathlib import Path
import requests
import pandas as pd

URL = "https://olinda.bcb.gov.br/olinda/servico/Pix_DadosAbertos/versao/v1/odata/TransacoesPixPorMunicipio(DataBase='202501')"

params = {
    "$format": "json",
    "$top": 1000,
    "@DataBase": "202501"
}

req = requests.get(URL, params=params, timeout=30)

print("Status:", req.status_code)

if req.status_code != 200:
    print(req.text)
    exit()

dados = req.json()

print(dados.keys())

df = pd.json_normalize(dados["value"])

outdir = Path(r"C:\Users\Usuario\PycharmProjects\PythonProject\data\raw")
outdir.mkdir(parents=True, exist_ok=True)

outfile = outdir / "pix.csv.py"

df.to_csv(outfile, index=False, encoding="utf-8-sig")

print("Arquivo CSV salvo em:", outfile)
