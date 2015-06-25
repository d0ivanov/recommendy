"""Euclidean distance similarity metric implementation."""
from similarity_metric import SimilarityMetric

class EuclideanDistance(SimilarityMetric):
    """Implementation of the Euclidean Distance algorithm from measuring
    similarity between two items"""

    def get_similarity(self, item1, item2):
        """Return a float between 0 and 1. The bigger the number the more
        similart the two items are. A result of 1 is a perfect match."""
        sum_of_squares = 0
        common_properties = set(item1.keys()) & set(item2.keys())
        if common_properties:
            for property in common_properties:
                sum_of_squares += (item2[property] - item1[property])**2
            return 1 / (1 + sum_of_squares**0.5)
        else:
            return 0
