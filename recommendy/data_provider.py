class DataProvider:
    """Represents the interface each data provider class should implement."""

    def get_data(self):
        """Return a hash of the parsed data"""
        raise NotImplementedError

    def _fetch_data(self):
        """Fetches data and returns it. All items must be comprised of
        properties that have some numeric values."""
        raise NotImplementedError

    def _parse_data(self):
        """Parse fetched data to a hashmap and return it. Each key is a
        data item. Each data item should have a hashmap of properties and
        their corresponding numeric values
        """
        raise NotImplementedError
