"""Main Recommender module."""


class Recommender(object):
    """Performs recommendations based on supplied data and a comparison
    algorithm.

    Attributes:
        data_provider         DataProvider instance
        similarity_algorithm  SimilarityMetric instance
    """

    def __init__(self, data_provider, similarity_metric):
        self.__provider = data_provider
        self.__similarity = similarity_metric

    def item_based_recommendations(self, subject):
        """Build a list of recommendations relevant to the items's
        properties. Returns a tuple of recommended items.

        arguments:
            item The item for which recommendations are being built
        """
        data = self.__provider.get_content()

        total_scores = {}
        score_sums = {}

        for other in data.keys():
            if other == subject:
                continue

            similarity = self.__similarity(data[subject], data[other])

            if similarity <= 0:
                continue

            for item in data[other].keys():
                if item not in data[subject] or data[subject][item] == 0:
                    total_scores.setdefault(item, 0)
                    score_sums.setdefault(item, 0)

                    total_scores[item] += data[other][item] * similarity
                    score_sums[item] += similarity

        rankings = [(total / score_sums[item], item)
                    for item, total in total_scores.items()]
        return sorted(rankings, key=lambda x: x[0], reverse=True)

    def content_based_recommendations(self, subject):
        """TODO: DOC"""
        data = self.__provider.get_content()
        content_similarities = self.calculate_similarities()

        scores = {}
        total_sim = {}

        for item, rating in data[subject].items():
            for similarity, item2 in content_similarities[item]:
                if item2 in data[subject]:
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
        data = self.__provider.transposed_content()
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
        #data = self.__provider.get_content()
        scores = [(self.__similarity(data[item], data[other]), other)
                  for other in data.keys() if other != item]
        return sorted(scores, key=lambda x: x[0], reverse=True)[:limit]
