import requests
import os
from dotenv import load_dotenv


def decode_msisdn(msisdn :str):
    load_dotenv('.envs')
    api_key = os.getenv('api_key_hashback')
    url = os.getenv('hashback_url')

    data = {
        'hash': msisdn,
        'API_KEY': api_key
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    try:
        response = requests.post(url, data=data, headers=headers)
        if response.status_code == 200:
            response_data =  response.json()
            decoded_phone = response_data["MSISDN"]
            return decoded_phone
        else:
            return msisdn
    except Exception as e:
        print("Exception occured while decoding M-PESA hash: ",{e})
        return e

if __name__ =="__main__":
    msisdn = "92918dd737cc3f312026d3be8957287591b501996ab231e1fec0cb92bffe187c"
    decoded_phone = decode_msisdn(msisdn)
    print(decoded_phone)