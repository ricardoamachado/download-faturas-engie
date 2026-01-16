import os
from datetime import datetime
from dotenv import load_dotenv
from api_helper import authenticate_user, get_faturas, download_file
from sys import argv

def main():

    if len(argv) > 1:
        reference_month = datetime.strptime(argv[1], "%Y-%m")
    else:
        reference_month = datetime.now()
    if len(argv) > 2:
        num_faturas = int(argv[2])
        if num_faturas <= 0 or num_faturas > 100:
            num_faturas = 100
    else:
        num_faturas = 100
    if len(argv) > 3:
        num_skip = int(argv[3])
        if num_skip < 0 or num_skip > 100:
            num_skip = 0
        else:
            num_skip = 0

    load_dotenv()
    USERNAME =  os.getenv("API_USERNAME")
    PASSWORD =  os.getenv("API_PASSWORD")
    if not USERNAME or not PASSWORD:
        raise ValueError("API_USERNAME e API_PASSWORD não foram definidos nas variáveis de ambiente.")
    resp = authenticate_user(USERNAME, PASSWORD)
    faturas = get_faturas(resp, reference_month, num_faturas=num_faturas, num_skip=num_skip)
    for item in faturas:
        url = item ["urlFatura"]
        file_name = f"faturas/{reference_month.strftime('%Y-%m')}_{item['unidade']}_{item['distribuidor']}.pdf"
        download_file(url, file_name)

if __name__ == "__main__":
    main()