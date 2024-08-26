import requests
import http.client
import json

def send_bip_whatsapp(phone_number):
    api_key = "9e5735f4bdf8290e3d9db104c33586ba-cc880383-748e-4350-b6bc-80c5e4eeb89c"
    api_url = "https://5v28vz.api.infobip.com"

    payload = json.dumps({
        "messages":[
            {
                "from": "254795570197",
                "to": phone_number,
                "messageId":"",
                "content": {
                    "templateName": "new_conversation_starter", ## replace this with the name of the template
                    "templateData":{
                        "body":{
                            "placeholders":[
                                
                            ]
                        }
                    },
                    "language" : "en_GB"
                },
                "callbackData" : "callback data",
                "notifyUrl": "",
                "urlOptions": {
                    "shortenUrl": False,
                    "trackClicks": False,
                    "trackingUrl": "",
                    "removeProtocol" : False,
                    "customDomain": ""
                }
            },
        ]
    })

    headers = {
        "Authorization": api_key,
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    results = requests.post(url = api_url,headers=headers, json = payload)
    res = results.json()
    return res
    
if __name__ == "__main__":
    result = send_bip_whatsapp("254702568824")
    print("\n ----- Results from whatsapp send messages -----\n")
    print(result)



