import requests
import json

def post_url():
    dfrimput_pet = {
                      "id": 0,
                      "category": {
                        "id": 0,
                        "name": "string"
                      },
                      "name": "doggie",
                      "photoUrls": [
                        "string"
                      ],
                      "tags": [
                        {
                          "id": 0,
                          "name": "string"
                        }
                      ],
                      "status": "available"
                    }
    header={'accept': 'application/json', 'Content-Type': 'application/json'}
    res = requests.post(url='https://petstore.swagger.io/v2/pet', data=json.dumps(dfrimput_pet), headers=header)

    print(res.status_code)
    print(res.json())

def get_url():

    header = {'accept': 'application/json'}
    res = requests.get(f'https://petstore.swagger.io/v2/pet/9223372036854647596', headers=header)

    print(res.status_code)
    print(res.json())

def put_url():
    dfrimput_pet = {
                        "id": 9223372036854647596,
            "category": {
                "id": 0,
                "name": "gusi"
            },
            "name": "doggie",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 0,
                    "name": "string"
                }
            ],
            "status": "sold"
            }
    header={'accept': 'application/json', 'Content-Type': 'application/json'}
    res = requests.put(url='https://petstore.swagger.io/v2/pet', data=json.dumps(dfrimput_pet), headers=header)

    print(res.status_code)
    print(res.json())

def delete_url():

    header = {'accept': 'application/json'}
    res = requests.delete(f'https://petstore.swagger.io/v2/pet/9223372036854647596', headers=header)

    print(res.status_code)
    print(res.json())

