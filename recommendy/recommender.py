class Recommender:
    """Performs recommendations based on supplied data and a comparison
    algorithm.

    Attributes:
        data_provider         Data set from which recommendations are made
        similarity_algorithm  Calculates the similarity between two items
    """

    def __init__(self, data_provider, similarity_algorithm):
        self.data_provider = data_provider
        self.similarity_algorithm = similarity_algorithm

    def recommend(self, subject):
        """Build a list of recommendations relevant to the subject's
        preferences. Returns a tuple of recommended items.

        arguments:
            subject The subject for which recommendations are being built
        """
        pass

    def _rank(self, subject):
        """Finds the closest matches to the subject from the data set.

        parameters:
            subject The subject being matched
        """
        pass
