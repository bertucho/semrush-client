import requests

def merge_dicts(*dict_args):
    '''
    Given any number of dicts, shallow copy and merge into a new dict,
    precedence goes to key value pairs in latter dicts.
    '''
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result


class SemrushClientException(BaseException):

    def __init__(self, error):
        self.error = error

    def __str__(self):
        return repr(self.error)

class SemrushAnalyticsClient:

    def __init__(self, key, limit):
        if not key:
            raise SemrushClientException("SEMRush API key required")

        self.url = "http://api.semrush.com/"
        self.key = key
        self.display_limit = limit


    def get_domain_organic(self, domain, database):
        return self._query("domain_organic", domain=domain, database=database)


    def get_url_organic(self, url, database):
        return self._query("url_organic", url=url, database=database)


    def get_domain_ranks(self, domain, database=""):
        return self._query("domain_ranks", domain=domain, database=database)


    def get_domain_rank(self, domain, database):
        return self._query("domain_rank", domain=domain, database=database)


    def get_domain_rank_history(self, domain, database):
        return self._query("domain_rank_history", domain=domain, database=database)


    def get_rank_difference(self, database):
        return self._query("rank_difference", database=database)


    def get_rank(self, database):
        return self._query("rank", database=database)


    def get_domain_adwords(self, domain, database):
        return self._query("domain_adwords", domain=domain, database=database)


    def get_domain_adwords_unique(self, domain, database):
        return self._query("domain_adwords_unique", domain=domain, database=database)


    def get_domain_organic_organic(self, domain, database):
        return self._query("domain_organic_organic", domain=domain, database=database)


    def get_domain_adwords_adwords(self, domain, database):
        return self._query("domain_adwords_adwords", domain=domain, database=database)


    def get_domain_adwords_historical(self, domain, database):
        return self._query("domain_adwords_historical", domain=domain, database=database)


    def get_domain_domains(self, domains, database):
        return self._query("domain_domains", domains=domains, database=database)


    def get_domain_shopping(self, domain, database):
        return self._query("domain_shopping", domain=domain, database=database)


    def get_domain_shopping_unique(self, domain, database):
        return self._query("domain_shopping_unique", domain=domain, database=database)


    def get_domain_shopping_shopping(self, domain, database):
        return self._query("domain_shopping_shopping", domain, database=database)


    def get_phrase_all(self, phrase, database=""):
        return self._query("phrase_all", phrase=phrase, database=database)


    def get_phrase_this(self, phrase, database):
        return self._query("phrase_this", phrase=phrase, database=database)


    def get_phrase_organic(self, phrase, database):
        return self._query("phrase_organic", phrase=phrase, database=database)


    def _query(self, report, **kwargs):

        universal = {
            'type': report,
            'key': self.key,
            'display_limit': self.display_limit
        }
        params = merge_dicts(universal, kwargs)
        response = requests.get(self.url, params=params)

        if response.status_code == 200:
            return response.content
        else:
            raise SemrushClientException(response.content)