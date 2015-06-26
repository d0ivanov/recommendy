from data_provider import DataProvider
import urllib.request
import json

class JSONDataProvider(DataProvider):

    def __init__(self, source):
        super().__init__(source)

    def get_data(self):
        return self._fetch_data()

    def _fetch_data(self):
        """Fetches data and returns it. All items must be comprised of
        properties that have some numeric values."""
        data = urllib.request.urlopen(self._source).read().decode('utf-8')
        return json.loads(data)
