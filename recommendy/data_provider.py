class DataProvider:
    """Represents the interface each data provider class should implement."""
    def fetch_data(self):
        """Fetches data and returns a tuple in which each data item
        is associated with a numeric value (rating)."""
        pass

