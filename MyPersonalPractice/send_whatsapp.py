import requests
import http.client
import json

conn = http.client.HTTPSConnection("5v28vz.api.infobip.com")


payload = json.dumps({
    "messages":[
        {
            "from": "",
            "to": "",
            "messageId":"",
            "content": {
                "templateName": "template_name", ## replace this with the name of the template
                "templateData":{
                    "body":{
                        "placeholders":[
                            "Placeholder Value 1",
                            "Placeholder Value 2"
                        ]
                    }
                },
                "language" : "en_GB"
            },
            "callbackData" : "callback data",
            "notifyUrl": "",
            "urlOptions": {
                "shortenUrl": True,
                "trackClicks": True,
                "trackingUrl": "",
                "removeProtocol" : True,
                "customDomain": ""
            }
        },
    ]
})

headers = {
    "Authorization": "",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

