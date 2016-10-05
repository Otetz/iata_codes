import os

import pytest

from iata_codes.cities import IATACodesClient


@pytest.fixture
def client():
    return IATACodesClient(os.environ['IATA_CODES_API_KEY'])


def test_city_code(client):
    city_code = 'MOW'
    res = client.get(code=city_code)
    assert res
    assert len(res) == 1
    assert res[0]['code'] == city_code
    assert res[0]['country_code'] == 'RU'
    assert res[0]['name'] == 'Moscow'


def test_city_name(client):
    city_name = 'Moscow'
    res = client.get(name=city_name)
    assert res
    assert len(res) == 1
    assert res[0]['code'] == 'MOW'
    assert res[0]['country_code'] == 'RU'
    assert res[0]['name'] == city_name


def test_one(client):
    city_code = 'MOW'
    res = client.get_one(code=city_code)
    assert res
    assert len(res) >= 3
    assert res['code'] == city_code
    assert res['country_code'] == 'RU'
    assert res['name'] == 'Moscow'


def test_country_code(client):
    country_code = 'RU'
    res = client.get(country_code=country_code)
    assert res
    assert len(res) >= 150
    assert res[0]['country_code'] == country_code
    assert res[-1]['country_code'] == country_code


def test_all_cities(client):
    res = client.get()
    assert res
    assert len(res) >= 9000
    assert 'code' in res[0]
    assert 'name' in res[0]
    assert 'country_code' in res[0]
