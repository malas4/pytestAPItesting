import requests
import json
from config import BASE_URI, id


def test_product_data_add_delete():
    URL = f'{BASE_URI}/products'
    file = open(r'C:\Users\Nihaan\PycharmProjects\rest\product_payload.json', "r")
    request_body = json.load(file)
    response = requests.post(URL, json=request_body)
    assert response.status_code == 200

    # validating the response
    response_python_object = json.loads(response.text)
    assert response_python_object['name'] == request_body['name']
    id = response_python_object['id']

    # deleting the product
    response = requests.delete(f'{BASE_URI}/products/{id}')
    assert response.status_code == 200
    response = requests.get(f'{BASE_URI}/{id}')
    assert response.status_code == 404

def test_patch_product_data():
    URL=f'{BASE_URI}/products/{id}'
    data = {
                "name": "Spider man New",
                "type": "figurine",
                "price": 20,
                "shipping": 0,
                "upc": "dfd",
                 "description": "toys for kids",
                "manufacturer": "sam",
                "model": "32323"
            }
    response = requests.patch(URL, data=data)
    response_json = response.json()
    assert response.status_code == 200
    print(response_json['price'])
    assert response_json['price'] == 10
