import pytest
import requests
from config import BASE_URI
import json



def test_get_products_contains_duracell():
    try:
        response = requests.get(f'{BASE_URI}/products')
        response.raise_for_status()

    except requests.exceptions.HTTPError as e:
        print(e)
    response_json_data = response.json()
    product = response_json_data['data'][0]['name']
    assert product == 'Duracell - AAA Batteries (4-Pack)'


def test_pagination():
    response = requests.get(f'{BASE_URI}/products?$limit=15&$skip=15')
    assert response.status_code == 200
    json_data = json.loads(response.text)
    data_length = len(json_data['data'])
    assert data_length == 15


def test_search_with_bad_productid():
    response = requests.get(f'{BASE_URI}/products/1234')
    assert response.status_code==404

def test_verify_duracell_2ndcategory_housewares():
    try:
        response = requests.get(f'{BASE_URI}/products')
        response.raise_for_status()

    except requests.exceptions.HTTPError as e:
        print(e)
    response_json_data = response.json()
    assert response_json_data['data'][0]['categories'][1]['name']== 'Housewares'

