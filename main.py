import openai
import secrets
import requests

openai.api_key = secrets.KEYS['secretKey']
SECRET_KEY = secrets.KEYS['secretKey']


class openaiApis:
    baseUrl = 'https://api.openai.com/v1/'

    def imageGenerations(self):
        method = 'POST'
        api = 'images/generations'
        data = {
            "prompt": "A cute baby sea otter",
            "n": 2,
            "size": "1024x1024"
        }

        requests.request(method=method, url=openaiApis.baseUrl + api, data=data)

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=input("Send Message: "),
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )


print(response)