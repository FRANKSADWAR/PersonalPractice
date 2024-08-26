import requests
import http.client
import json

def send_bip_whatsapp(phone_number):
    api_key = "9e5735f4bdf8290e3d9db104c33586ba-cc880383-748e-4350-b6bc-80c5e4eeb89c"

    api_url = "https://5v28vz.api.infobip.com/whatsapp/1/message/template"

    payload = json.dumps({
        "messages":[
            {
                "from": "254795570197",
                "to": phone_number,
                "messageId":"test-message-001",
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
    
def test_send_template(phone):
    import http.client
    import json
    authorization = "9e5735f4bdf8290e3d9db104c33586ba-cc880383-748e-4350-b6bc-80c5e4eeb89c"

    conn = http.client.HTTPSConnection("5v28vz.api.infobip.com")
    payload = json.dumps({
        "messages": [
            {
                "from": "254795570197",
                "to": phone,
                "messageId": "a28dd97c-1ffb-4fcf-99f1-0b557ed381da",
                "content": {
                    "templateName": "new_conversation_starter",
                    "templateData": {
                        "body": {
                            "placeholders": [
                               
                            ]
                        }
                    },
                    "language": "en_GB"
                },
                "callbackData": "Callback data",
            }
        ]
    })
    headers = {
        'Authorization': f'{authorization}',
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    conn.request("POST", "/whatsapp/1/message/template", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))




def test_sdk():
    from infobip_channels.whatsapp.channel import WhatsAppChannel
    c = WhatsAppChannel.from_auth_params({
        "base_url": "https://5v28vz.api.infobip.com",
        "api_key": "9e5735f4bdf8290e3d9db104c33586ba-cc880383-748e-4350-b6bc-80c5e4eeb89c"})

    response = c.send_template_message({
    "messages": [
        {
        "from": "254795570197",
        "to": "254702568824",
        "messageId": "a28dd97c-1ffb-4fcf-99f1-0b557ed381da",
        "content": {
            "templateName": "rice_advisories_1_site_selection_en",
            "templateData": {
            "body": {
                        "placeholders": []
                    }
                    
            },
            "language": "en"
        }
        }
    ]
    })

if __name__ == "__main__":
    result = test_sdk()
    print("\n---- Results -------\n")
    print(result)



