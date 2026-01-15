import os
from datetime import datetime
from dotenv import load_dotenv
from api_helper import authenticate_user, get_faturas, download_file

def main():
    load_dotenv()
    USERNAME =  os.getenv("API_USERNAME")
    PASSWORD =  os.getenv("API_PASSWORD")
    resp = authenticate_user(USERNAME, PASSWORD)
    reference_month = datetime(2025,12,1)
    faturas = get_faturas(resp, reference_month)
    for item in faturas:
        url = item ["urlFatura"]
        file_name = f"faturas/2025-12_{item['unidade']}_{item['distribuidor']}.pdf"
        download_file(url, file_name)

if __name__ == "__main__":
    main()