# Script para fazer o download de faturas com o API da ENGIE.
Versão: 0.1.0

## Requisitos
Python 3.13 ou superior

Gerenciador de pacotes uv - [link](https://docs.astral.sh/uv/getting-started/installation/)

Dependências listadas no arquivo pyproject.toml

## Guia de Utilização do Script

Execute o script no terminal com o comando:
```
uv run main.py YYYY-AA <num_faturas> <num_skip>
```

* `num_faturas` é um valor entre 1 a 100 e representa o número de faturas que serão baixadas.
* `num_skip` é um valor entre 0 a 100 e representa o número de faturas que são puladas na etapa de download. Necessário para baixar todas as faturas de um determinado mês com mais de 100 faturas no sistemas.