import os
import pandas as pd
import networkx as nx
import kagglehub

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
import seaborn as sns
import matplotlib.pyplot as plt
import pickle
plt.style.use('ggplot')

data = pd.read_csv('coursera_processed_data.csv')

with open('similarity_matrix.pkl', 'rb') as file:
    similarity_matrix = pickle.load(file)

def normalize_rating(rating_str):
    """
    Normalize the course rating to a 0-1 scale.
    """
    try:
        return (float(rating_str) - 0) / (5 - 0)  # Normalize to 0-1
    except ValueError:
        return 0  


def get_recommendations(course_id, data, similarity_matrix, top_n=3, rating_weight=0.05):
    """
    @param course_id 
    Get top N course recommendations based on similarity to the given course name.
    """
    course_id = data[data['ID'] == course_id]
    course_idx = course_id.index[0]
    similarity_scores = list(enumerate(similarity_matrix[course_idx]))
    
    recommendations = []
    for idx, similarity_score in sorted(similarity_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]:
        course_data = data.iloc[idx]
        normalized_rating = normalize_rating(course_data.get('Course Rating', '0'))

        recommendations.append({
            "course_id": course_data["ID"],
            "course_name": course_data['Course Name'],
            "course_url": course_data.get('Course URL', ''),
            "rating": course_data['Course Rating'],
            "institution": course_data.get('University', 'Unknown'),
            "difficulty_level": course_data.get('Difficulty Level', 'Unknown'),
            "similarity": similarity_score,
            "final_score": similarity_score * (1 - rating_weight) + normalized_rating * rating_weight 
        })

    return sorted(recommendations, key=lambda x: x['final_score'], reverse=True)

    
def get_recommendations_from_list_of_courses(courses_id, data, top_n=5):
    recommended = {}
    for course_id in courses_id:
        courses = get_recommendations(course_id=course_id,similarity_matrix= similarity_matrix, data= data)
        for course in courses:
            if(course['course_id'] in recommended):
                recommended[course['course_id']] += course['similarity']
            else:
                recommended[course['course_id']] = course['similarity']
    recommended = sorted(recommended.items(), key=lambda item: item[1], reverse=True)
    return [id[0] for id in recommended[0: top_n]]
    
    
print(get_recommendations_from_list_of_courses([24, 35, 28], data))