import requests
import json
import os
from dotenv import load_dotenv


load_dotenv('.envs')
api_key = os.getenv('api_key_dcode')

SERVER = "https://decodehash.com"
DECODEHASH_END_POINT = "/app/api/v1/decode-hash/freemium/"
hash_str = "92918dd737cc3f312026d3be8957287591b501996ab231e1fec0cb92bffe187c"

url = f"{SERVER}{DECODEHASH_END_POINT}{hash_str}"

headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {api_key}",
    }
#URL_ENDPOINT = "https://api.hashback.co.ke/decode"
#payload = {
#       "hash":"92918dd737cc3f312026d3be8957287591b501996ab231e1fec0cb92bffe187c"
#}

try:
    response = requests.get(url, headers = headers)
    data = response.json()
    print(data)
except Exception as e:
    print("Error occured", str(e))

#api_key_dcode = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJmcmFua2xpbmt6YmVuejk1QGdtYWlsLmNvbSIsImV4cCI6MTc3ODMxNDQ2MywibmJmIjoxNzUyMzk0NDYzfQ.fwVkwFkw8t3W0jIEQb8V-sXUjfu-JWLAQXV1NO36-04"