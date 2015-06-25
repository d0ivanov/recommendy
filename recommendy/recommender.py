"""Main Recommender module."""
from json_data_provider import JSONDataProvider
from euclidean_distance import EuclideanDistance

class Recommender:
    """Performs recommendations based on supplied data and a comparison
    algorithm.

    Attributes:
        data_provider         DataProvider instance
        similarity_algorithm  SimilarityMetric instance
    """

    def __init__(self, data_provider, similarity_algorithm):
        self.data = data_provider.get_data()
        self.similarity = similarity_algorithm.get_similarity

    def recommend(self, subject):
        """Build a list of recommendations relevant to the subject's
        preferences. Returns a tuple of recommended items.

        arguments:
            subject The subject for which recommendations are being built
        """
        total_scores = {}
        score_sums = {}
        subject_properties = self.data[subject]
        for item, properties in self.data.items():
            if item == subject:
                continue

            similarity = self.similarity(properties, subject_properties)

            if similarity == 0:
                continue

            for property in properties.keys():
                if(property not in subject_properties or
                   subject_properties[property] == 0):

                    total_scores.setdefault(property, 0)
                    score_sums.setdefault(property, 0)

                    score_sums[property] += similarity
                    total_scores[property] += properties[property] * similarity

        recommendations = [(total / score_sums[item], item)
                           for item, total in total_scores.items()]
        return sorted(recommendations, key=lambda x: x[0], reverse=True)
