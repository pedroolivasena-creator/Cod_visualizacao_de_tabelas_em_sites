# Cod_visualizacao_em_JSON
Documentação do código
1. Importação das bibliotecas
from pathlib import Path
import requests
import pandas as pd

São utilizadas três bibliotecas:

Path (pathlib): permite trabalhar com caminhos de arquivos e pastas de forma mais segura e organizada.
requests: realiza requisições HTTP para acessar a API do Banco Central.
pandas: organiza os dados recebidos em um DataFrame e permite exportá-los para CSV.
2. Definição da URL da API
URL = "https://olinda.bcb.gov.br/olinda/servico/Pix_DadosAbertos/versao/v1/odata/TransacoesPixPorMunicipio(DataBase='202501')"

A variável URL armazena o endereço da API do Banco Central.

O trecho:

DataBase='202501'

indica a base de dados referente a janeiro de 2025.

A API utiliza o padrão OData, que permite consultar conjuntos de dados por meio de requisições HTTP.

3. Definição dos parâmetros
params = {
    "$format": "json",
    "$top": 1000,
    "@DataBase": "202501"
}

Esses parâmetros configuram como a API deve retornar os dados:

$format: "json" → solicita que os dados sejam retornados no formato JSON.
$top: 1000 → solicita no máximo 1.000 registros.
@DataBase: "202501" → informa o período da base de dados consultada.

Observação: como o período também está definido diretamente na URL, o @DataBase pode ser redundante dependendo de como o endpoint interpreta os parâmetros.

4. Requisição à API
req = requests.get(URL, params=params, timeout=30)

O método requests.get() realiza uma requisição GET para a API.

O parâmetro:

timeout=30

determina que a requisição poderá esperar até 30 segundos antes de ser interrompida.

A resposta da API fica armazenada na variável req.

5. Verificação do status da requisição
print("Status:", req.status_code)


if req.status_code != 200:
    print(req.text)
    exit()

O código verifica o status HTTP retornado pela API.

O código:

200

significa que a requisição foi realizada com sucesso.

Caso o status seja diferente de 200, o programa:

Mostra o conteúdo da resposta utilizando req.text;
Encerra a execução com exit().

Isso evita que o programa tente processar uma resposta que pode conter uma mensagem de erro em vez dos dados esperados.

6. Conversão da resposta para JSON
dados = req.json()

A resposta recebida da API é convertida de JSON para uma estrutura de dados do Python.

Normalmente, a API retorna uma estrutura semelhante a:

{
    "value": [
        {...},
        {...},
        {...}
    ]
}

O campo value contém os registros obtidos.

7. Verificação das chaves
print(dados.keys())

Esse comando mostra as chaves existentes no objeto JSON.

Por exemplo:

dict_keys(['@odata.context', 'value'])

Isso é útil para verificar a estrutura retornada pela API antes de acessar os dados.

8. Conversão dos dados para DataFrame
df = pd.json_normalize(dados["value"])

Aqui os registros armazenados em:

dados["value"]

são convertidos para um DataFrame do Pandas.

O json_normalize() é especialmente útil quando os dados JSON possuem estruturas aninhadas, pois consegue transformar essas estruturas em colunas.

O resultado é armazenado na variável:

df
9. Definição do diretório de saída
outdir = Path(r"C:\Users\Usuario\PycharmProjects\PythonProject\data\raw")

Define a pasta onde o arquivo será armazenado.

O r antes da string:

r"C:\Users\..."

faz com que as barras invertidas \ sejam interpretadas corretamente no caminho do Windows.

10. Criação da pasta
outdir.mkdir(parents=True, exist_ok=True)

Esse comando garante que a pasta de destino exista.

parents=True → permite criar também pastas intermediárias que ainda não existam.
exist_ok=True → evita gerar erro caso a pasta já exista.
11. Definição do arquivo de saída
outfile = outdir / "pix.csv.py"

Aqui é definido o nome do arquivo que será criado.

Existe um detalhe importante: o nome está como:

pix.csv.py

Se a intenção é criar um arquivo CSV, o ideal é utilizar:

outfile = outdir / "pix.csv"

Assim, a extensão será corretamente .csv.

12. Exportação para CSV
df.to_csv(outfile, index=False, encoding="utf-8-sig")

O DataFrame é convertido em um arquivo CSV.

outfile → indica onde o arquivo será salvo.
index=False → impede que o índice do DataFrame seja salvo como uma coluna adicional.
encoding="utf-8-sig" → utiliza uma codificação que facilita a abertura do CSV no Excel, especialmente quando existem caracteres como ã, ç e é.
13. Mensagem final
print("Arquivo CSV salvo em:", outfile)

Exibe no console o caminho onde o arquivo foi salvo.

Por exemplo:

Arquivo CSV salvo em: C:\Users\Usuario\PycharmProjects\PythonProject\data\raw\pix.csv
Fluxo geral do programa

O funcionamento pode ser resumido assim:

API do Banco Central
↓
Requisição HTTP com requests
↓
Recebimento dos dados em JSON
↓
Extração de dados["value"]
↓
Conversão para DataFrame com Pandas
↓
Criação da pasta raw
↓
Exportação para CSV
↓
Arquivo pix.csv

Objetivo do código

O objetivo principal é coletar automaticamente dados públicos de transações Pix por município disponibilizados pelo Banco Central, transformá-los em uma estrutura tabular utilizando Pandas e armazená-los em formato CSV para posterior análise ou processamento em um projeto de dados.

Versão corrigida do trecho do nome do arquivo

Recomendo alterar:

outfile = outdir / "pix.csv.py"

para:

outfile = outdir / "pix.csv"

porque pix.csv.py possui extensão de arquivo Python (.py) e não representa corretamente um arquivo CSV.
