"""Main Recommender module."""

class Recommender(object):
    """Performs recommendations based on supplied data and a comparison
    algorithm.

    Attributes:
        data_provider         DataProvider instance
        similarity_algorithm  SimilarityMetric instance
    """

    def __init__(self, data_provider, similarity_metric):
        self._provider = data_provider
        self._similarity = similarity_metric

    def get_recommendations(self, subject):
        raise NotImplementedError


class ItemBasedRecommender(Recommender):
    """TODO: DOC"""

    def get_recommendations(self, subject):
        """Build a list of recommendations relevant to the items's
        properties. Returns a tuple of recommended items.

        arguments:
            item The item for which recommendations are being built
        """
        data = self._provider.get_data()
        total_scores = {}
        score_sums = {}
        subject_properties = data[subject]

        for item, properties in data.items():
            if subject == item:
                continue

            similarity = self._similarity(properties, subject_properties)

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

class ContentBasedRecommender(Recommender):
    """TODO: DOC"""

    def __init__(self, data_provider, similarity_metric):
        super(ContentBasedRecommender, self).__init__(data_provider,
                                                      similarity_metric)
        self.__data = data_provider.get_data()

    def get_recommendations(self, subject):
        ratings = self.__data[subject]
        scores = {}
        total_sim = {}
        content_similarities = self.calculate_similarities()

        for item, rating in ratings.items():
            for similarity, item2 in content_similarities[item]:
                if item2 in ratings:
                    continue

                scores.setdefault(item2, 0)
                total_sim.setdefault(item2, 0)

                scores[item2] += similarity * rating
                total_sim[item2] += similarity

        rankings = [(score / total_sim[item], item)
                    for item, score in scores.items()]
        return sorted(rankings, key=lambda x: x[0], reverse=True)

    def calculate_similarities(self, limit=3):
        """Generate a dictionary in which each key is an item and the
        value is a list of its top matches, e.g.:
        {"<item>": [(<similarity_score>, <similar_item>)]}

        arguments:
            limit The max number of top matching items returned"""
        result = {}
        data = self._provider.transpose_data()
        for item in data.keys():
            result[item] = self.__top_matches(item, data, limit)
        return result

    def __top_matches(self, item, data, limit=3):
        """Generate a list of top matching items to another item. The list
        consists of tuples: (<similarity_score>, <item>)

        arguments:
            item The item for which the top matches are calculated
            data The dataset from which scores are pulled
            limit The max number of top matching items returned"""
        scores = [(self._similarity(data[item], data[other]), other)
                  for other in data.keys() if other != item]
        return sorted(scores, key=lambda x: x[0], reverse=True)[:limit]
