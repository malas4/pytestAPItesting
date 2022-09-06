import requests
import json
from config import BASE_URI


def test_product_data_add_delete():
    URL = f'{BASE_URI}/products'
    file = open(r'C:\Users\Nihaan\PycharmProjects\rest\product_payload.json', "r")
    request_body = json.load(file)
    response = requests.post(URL, json=request_body)
    assert response.status_code == 201

    # validating the response
    response_python_object = json.loads(response.text)
    assert response_python_object['name'] == request_body['name']
    id = response_python_object['id']

    # deleting the product
    response = requests.delete(f'{BASE_URI}/products/{id}')
    assert response.status_code == 200
    response = requests.get(f'{BASE_URI}/{id}')
    assert response.status_code == 404
