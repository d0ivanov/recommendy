from data_provider import DataProvider
import urllib.request
import json

class JSONDataProvider(DataProvider):

    def __init__(self, source):
        self.source = source

    def get_data(self):
        return self._parse_data()

    def _fetch_data(self):
        return urllib.request.urlopen(self.source).read().decode('utf-8')

    def _parse_data(self):
        return json.loads(self._fetch_data())
