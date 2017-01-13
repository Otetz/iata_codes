==========
iata_codes
==========

.. image:: https://travis-ci.org/Otetz/iata_codes.svg?branch=master
   :alt: Build Status
   :target: https://travis-ci.org/Otetz/iata_codes

.. image:: https://codecov.io/gh/Otetz/iata_codes/branch/master/graph/badge.svg
   :alt: codecov
   :target: https://codecov.io/gh/Otetz/iata_codes

.. image:: https://coveralls.io/repos/github/Otetz/iata_codes/badge.svg?branch=master
   :alt: Coverage Status
   :target: https://coveralls.io/github/Otetz/iata_codes?branch=master

Python client for IATA Codes Database REST API

Features
--------

- Search city by IATA code
- Search cities by country code
- Search IATA code by name of the city
- …

Installation
------------

Install iata_codes package from PyPi::

  pip install iata_codes

Getting started
---------------

Make sure to include this line in the beginning of your file::

  from iata_codes.cities import IATACodesClient

Set your API Key::

  client = IATACodesClient('YOUR_API_KEY')

Make queries::

  print(client.get(code='MOW'))
  print(client.get(country_code='RU'))
  print(client.get(name='Moscow'))

Links
-----

- `IATA Codes Database <http://iatacodes.org/>`_
