# recommendy

##Usage

data_hander = JSONDataHandler("http://your_data_resource")
similarity_metric = pearson_corellation

racommender = Recommender(data_handler, similarity_metric)

To get item based recommendations:
recommender.item_based_recommendations("<subject_to_get_recommendations_for>")

For content based recommendations:

recommender.content_based_recommendations("<subject_to_get_recommendations_for>")

##Similarity metrics

There are three similarity metrics currently built in the recommender:
 * euclidean distance
 * pearson corellation coefficient
 * tanimoto score
Euclidean distance and pearson corellation coefficient can be used when calculating
similarities based on given scores, for example when users rate movies.

Tanimoto score is best suited when similarities are calculated based on the presence or absence of a property.
For example if you have a web store and you just
indicate wheather an item was bought or not and want to make recommendations based
on items bought.

You are free to implement whatever other similarity algorithm most suits you and
pass it to the recommender. It should take two maps, formatted like {<property>: <score>} as arguments and always
return a number between 0 and 1.

##Data Providers
The recommender relies on a data provider to feed it necessairy data in order to make recommendations. Check the
data_handler interface to see what methods each data provider must implement. There are currently two abstract data
handlers - XMLDataHandler and JSONDataHandler, but as long as it implements the data handler interface, you can pass
to the recommender whatever classes you find most suitable.

##Precomputing similarities

As your data set grows computing similarities between items may become slower and slower. That's why the recommender class
has a calculate_similarities method, that when called will compute similarities for us. It's advised that similarities are precomputed and
stored via the data handler class so that there would be no need to compute them each time recommendations are required.
