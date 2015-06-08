class SimilarityMetric:
    """Represents the interface each similarity algorithm should implement.
    Similarity algorithms are used to determine which items are most similar
    so that the recommender can draw conclusions."""

    def get_similarity(self, item1, item2):
        """Calculates a similarity rating between two data items. Returns
        a float value between 0 and 1. A value of 1 represents a high
        similarity rating, a value of 0 represents the lowest
        similarity rating.

        arguments:
        item1 & item2 - the itmes being compared
        """
        pass
