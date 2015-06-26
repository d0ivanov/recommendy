class DataProvider:
    """Represents the interface each data provider class should implement."""

    def __init__(self, source):
        self._source = source

    def get_data(self):
        """Return a hash of the parsed data"""
        raise NotImplementedError

    def transpose_data(self):
        """Transpose the data so that properties become keys
        and keys become properties."""
        result = {}
        for key, value in self.get_data().items():
            for property, score in value.items():
                result.setdefault(property, {})
                result[property][key] = score
        return result
