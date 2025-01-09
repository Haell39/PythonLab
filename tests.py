import requests
import pandas as pd

# URL da API que retorna uma lista de posts
url = "https://jsonplaceholder.typicode.com/posts"

# Fazendo a requisição GET para a API
response = requests.get(url)

# Verificando se a requisição foi bem-sucedida
if response.status_code == 200:
    # Convertendo a resposta JSON para um dicionário Python
    data = response.json()

    # Criando um DataFrame do pandas a partir dos dados
    df = pd.DataFrame(data)

    # Exibindo os primeiros 5 registros do DataFrame
    display(df.head())
else:
    print(f"Erro na requisição: {response.status_code}")


