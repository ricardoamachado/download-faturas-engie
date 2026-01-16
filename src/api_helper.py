import requests
import json
from datetime import datetime


def authenticate_user(username: str, password: str) -> str:
    url = "https://smart-geracaodistribuida-api.engiesolucoes.digital/api/autenticacao/Login"
    data = {
        "email": username,
        "password": password
    }
    headers = {
        "Content-Type": "application/json",
        "accept" : "*/*",
    }

    response = requests.post(url, data=json.dumps(data), headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Erro de autenticação com status code: {response.status_code}: {response.text}")

def get_faturas(token: str, reference_month:datetime, num_faturas: int = 100, num_skip: int = 0) -> dict:
    url = "https://smart-geracaodistribuida-api.engiesolucoes.digital/api/fatura"
    headers = {
        "accept": "text/plain",
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    data = {
        "mesReferencia": reference_month.strftime("%Y-%m-01"),
        "paginacao": {"skip": num_skip, "take": num_faturas}
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Erro ao consultar faturas com status code: {response.status_code}: {response.text}")

def download_file(url:str, local_filename) -> None:
    response = requests.get(url)
    if response.status_code == 200:
        with open(local_filename, 'wb') as file:
            file.write(response.content)
        print(f"Arquivo '{local_filename}' baixado com sucesso!")
    else:
        raise Exception(f"Erro ao baixar o arquivo. Status code: {response.status_code}")
        