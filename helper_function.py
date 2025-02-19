import re
from gensim.models.phrases import Phrases, Phraser
from collections import Counter

def find_most_common_phrase_per_cluster_gensim(df, cluster_column_name, column_name, custom_stopwords=[]):
    '''
    @param df: DataFrame containing the data.
    @param cluster_column_name: The column representing the cluster IDs.
    @param column_name: The column whose values are used to extract words (e.g., "Course Description").
    @param custom_stopwords: A list of stopwords to ignore.
    @return: A dictionary mapping each cluster ID to the most common word or phrase in that cluster.
    '''
    cluster_names = {}

    for cluster_id in df[cluster_column_name].unique():
        # Join all the text in the column for the current cluster
        cluster_text = " ".join(df[df[cluster_column_name] == cluster_id][column_name])

        # Step 1: Clean and tokenize the text
        cluster_text = re.sub(r'\s+', ' ', cluster_text.lower().strip())
        words = re.findall(r'\b\w+\b', cluster_text)  # Tokenizing the text

        # Step 2: Remove stopwords
        filtered_words = [word for word in words if word not in custom_stopwords]

        # Step 3: Use Gensim's Phrases to detect collocations (bigrams and trigrams)
        phrases = Phrases([filtered_words], min_count=1, threshold=1)  # Low threshold to capture more phrases
        bigram_phraser = Phraser(phrases)

        # Step 4: Transform the words into phrases
        phrases_list = bigram_phraser[filtered_words]

        # Step 5: Count the frequency of words and phrases
        term_counts = Counter(phrases_list)

        # Step 6: Get the most common term (word or phrase)
        if term_counts:
            most_common_term = term_counts.most_common(10)[0]
            cluster_names[cluster_id] = most_common_term
        else:
            cluster_names[cluster_id] = "No terms found"

    return cluster_names
