import json
import os

import requests_mock
import pytest

from iata_codes.cities import IATACodesClient


@pytest.fixture
def client():
    return IATACodesClient(os.environ['IATA_CODES_API_KEY'])


def json_from_file(filename):
    with open('tests/data/' + filename) as json_file:
        return json.load(json_file)


def test_city_code(client):
    city_code = 'MOW'
    with requests_mock.Mocker() as m:
        m.get("https://iatacodes.org/api/v6/cities?api_key={api_key}&code=MOW".format(
            api_key=os.environ['IATA_CODES_API_KEY']),
            json=json_from_file('mow.json'),
            headers={'Content-Type': 'application/json; charset=utf-8'}, )
        res = client.get(code=city_code)
    assert res
    assert len(res) == 1
    assert res[0]['code'] == city_code
    assert res[0]['country_code'] == 'RU'
    assert res[0]['name'] == 'Moscow'


def test_city_name(client):
    city_name = 'Moscow'
    with requests_mock.Mocker() as m:
        m.register_uri('GET',
                       "https://iatacodes.org/api/v6/cities?api_key={api_key}&code=MOW".format(
                           api_key=os.environ['IATA_CODES_API_KEY']),
                       json=json_from_file('mow.json'),
                       headers={'Content-Type': 'application/json; charset=utf-8'}, )
        m.register_uri('GET',
                       "https://iatacodes.org/api/v6/autocomplete?api_key={api_key}&query=Moscow".format(
                           api_key=os.environ['IATA_CODES_API_KEY']),
                       json=json_from_file('moscow.json'),
                       headers={'Content-Type': 'application/json; charset=utf-8'}, )
        res = client.get(name=city_name)
    assert res
    assert len(res) == 1
    assert res[0]['code'] == 'MOW'
    assert res[0]['country_code'] == 'RU'
    assert res[0]['name'] == city_name


def test_one(client):
    city_code = 'MOW'
    with requests_mock.Mocker() as m:
        m.get("https://iatacodes.org/api/v6/cities?api_key={api_key}&code=MOW".format(
            api_key=os.environ['IATA_CODES_API_KEY']),
            json=json_from_file('mow.json'),
            headers={'Content-Type': 'application/json; charset=utf-8'}, )
        res = client.get_one(code=city_code)
    assert res
    assert len(res) >= 3
    assert res['code'] == city_code
    assert res['country_code'] == 'RU'
    assert res['name'] == 'Moscow'


def test_country_code(client):
    country_code = 'RU'
    with requests_mock.Mocker() as m:
        m.get("https://iatacodes.org/api/v6/cities?api_key={api_key}&country_code=RU".format(
            api_key=os.environ['IATA_CODES_API_KEY']),
            json=json_from_file('ru.json'),
            headers={'Content-Type': 'application/json; charset=utf-8'}, )
        res = client.get(country_code=country_code)
    assert res
    assert len(res) >= 150
    assert res[0]['country_code'] == country_code
    assert res[-1]['country_code'] == country_code


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
