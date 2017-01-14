import logging

import requests
from furl import furl

log = logging.getLogger(__name__)


class IATACodesClient:
    def __init__(self, api_key):
        self.__api_key = api_key

    def get(self, code=None, name=None, country_code=None):
        f = furl('https://iatacodes.org/api/v6/cities?api_key={api_key}'.format(api_key=self.__api_key))
        if name:
            code = self.__query_by_name(name)
        if code:
            f.args['code'] = code
        if country_code:
            f.args['country_code'] = country_code
        log.info(f.url)
        r = requests.get(f.url)
        log.debug('\t' + str(r.status_code))
        if r.status_code != 200:
            raise WrongIATAResultException('r.status_code = %d' % r.status_code)
        res = r.json()
        log.debug(r.headers['content-type'])
        log.debug(res)
        if 'response' not in res:
            raise WrongIATAResultException('r.json() = %s' % res)
        return res['response']

    def get_one(self, code=None, name=None, country_code=None):
        res = self.get(code, name, country_code)
        if res and len(res) > 0:
            return res[0]
        return None

    def __query_by_name(self, name):
        url = 'https://iatacodes.org/api/v6/autocomplete?api_key={api_key}&query={query}' \
            .format(api_key=self.__api_key, query=name)
        log.info(url)
        r = requests.get(url)
        log.debug('\t' + str(r.status_code))
        if r.status_code != 200:
            raise WrongIATAResultException('r.status_code = %d' % r.status_code)
        res = r.json()
        log.debug(r.headers['content-type'])
        log.debug(res)
        if 'response' not in res:
            raise WrongIATAResultException('r.json() = %s' % res)
        result = []
        for rec in res['response']['cities']:
            result.append(rec['code'])
        log.debug('\t' + ','.join(result))
        return ','.join(result)


class WrongIATAResultException(Exception):
    pass
