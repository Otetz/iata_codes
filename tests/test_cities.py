import json
import os

import requests_mock
import pytest

from iata_codes import IATACodesClient


@pytest.fixture
def client():
    return IATACodesClient(os.environ['IATA_CODES_API_KEY'])


def json_from_file(filename):
    with open('tests/data/' + filename) as json_file:
        return json.load(json_file)


# noinspection PyShadowingNames
def test_city_code(client):
    city_code = 'MOW'
    with requests_mock.Mocker() as m:
        m.get("https://iatacodes.org/api/v6/cities?api_key={api_key}&code={city_code}".format(
            api_key=os.environ['IATA_CODES_API_KEY'], city_code=city_code),
            json=json_from_file('mow.json'),
            headers={'Content-Type': 'application/json; charset=utf-8'}, )
        res = client.get(code=city_code)
    assert res
    assert len(res) == 1
    assert res[0]['code'] == city_code
    assert res[0]['country_code'] == 'RU'
    assert res[0]['name'] == 'Moscow'


# noinspection PyShadowingNames
def test_city_name(client):
    city_code = 'MOW'
    city_name = 'Moscow'
    with requests_mock.Mocker() as m:
        m.register_uri('GET',
                       "https://iatacodes.org/api/v6/cities?api_key={api_key}&code={city_code}".format(
                           api_key=os.environ['IATA_CODES_API_KEY'], city_code=city_code),
                       json=json_from_file('mow.json'),
                       headers={'Content-Type': 'application/json; charset=utf-8'}, )
        m.register_uri('GET',
                       "https://iatacodes.org/api/v6/autocomplete?api_key={api_key}&query={city_name}".format(
                           api_key=os.environ['IATA_CODES_API_KEY'], city_name=city_name),
                       json=json_from_file('moscow.json'),
                       headers={'Content-Type': 'application/json; charset=utf-8'}, )
        res = client.get(name=city_name)
    assert res
    assert len(res) == 1
    assert res[0]['code'] == city_code
    assert res[0]['country_code'] == 'RU'
    assert res[0]['name'] == city_name


# noinspection PyShadowingNames
def test_one(client):
    city_code = 'MOW'
    with requests_mock.Mocker() as m:
        m.get("https://iatacodes.org/api/v6/cities?api_key={api_key}&code={city_code}".format(
            api_key=os.environ['IATA_CODES_API_KEY'], city_code=city_code),
            json=json_from_file('mow.json'),
            headers={'Content-Type': 'application/json; charset=utf-8'}, )
        res = client.get_one(code=city_code)
    assert res
    assert len(res) >= 3
    assert res['code'] == city_code
    assert res['country_code'] == 'RU'
    assert res['name'] == 'Moscow'


# noinspection PyShadowingNames
def test_country_code(client):
    country_code = 'RU'
    with requests_mock.Mocker() as m:
        m.get("https://iatacodes.org/api/v6/cities?api_key={api_key}&country_code={country_code}".format(
            api_key=os.environ['IATA_CODES_API_KEY'], country_code=country_code),
            json=json_from_file('ru.json'),
            headers={'Content-Type': 'application/json; charset=utf-8'}, )
        res = client.get(country_code=country_code)
    assert res
    assert len(res) >= 150
    assert res[0]['country_code'] == country_code
    assert res[-1]['country_code'] == country_code


# noinspection PyShadowingNames
def test_all_cities(client):
    with requests_mock.Mocker() as m:
        m.get("https://iatacodes.org/api/v6/cities?api_key={api_key}".format(
            api_key=os.environ['IATA_CODES_API_KEY']),
            json=json_from_file('all.json'),
            headers={'Content-Type': 'application/json; charset=utf-8'}, )
        res = client.get()
    assert res
    assert len(res) >= 9000
    assert 'code' in res[0]
    assert 'name' in res[0]
    assert 'country_code' in res[0]


# noinspection PyShadowingNames
def test_wrong_city_code(client):
    city_code = 'MOK'
    with requests_mock.Mocker() as m:
        m.get("https://iatacodes.org/api/v6/cities?api_key={api_key}&code={city_code}".format(
            api_key=os.environ['IATA_CODES_API_KEY'], city_code=city_code),
            json=json_from_file('mok.json'),
            headers={'Content-Type': 'application/json; charset=utf-8'}, )
        res = client.get_one(code=city_code)
    assert res is None
