import re
from gensim.models.phrases import Phrases, Phraser
from collections import Counter
import re
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer

def find_most_common_phrase_per_cluster(df, cluster_column_name, column_name, custom_stopwords=[]):
    '''
    @param df: DataFrame containing the data.
    @param cluster_column_name: The column representing the cluster IDs.
    @param column_name: The column whose values are used to extract words (e.g., "Course Description").
    @param custom_stopwords: A list of stopwords to ignore.
    @return: A dictionary mapping each cluster ID to the most common word or phrase in that cluster.
    '''
    cluster_names = {}
    for cluster_id in df[cluster_column_name].unique():
        cluster_text = " ".join(df[df[cluster_column_name] == cluster_id][column_name])

        vectorizer = CountVectorizer(
            stop_words=list(custom_stopwords),
            ngram_range=(1, 3)
        )
        tokenized_phrases = vectorizer.fit_transform([cluster_text])
        terms = vectorizer.get_feature_names_out()
        term_counts = Counter(dict(zip(terms, tokenized_phrases.toarray().flatten())))
        most_common_term = term_counts.most_common(10)
        cluster_names[cluster_id] = most_common_term

    return cluster_names

