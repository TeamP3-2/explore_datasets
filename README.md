# Course Recommendation System

This project was developed as part of a hackathon challenge to build a **Course Recommendation System** using various datasets from Coursera, Stanford, and Harvard. The final recommendation system is content-based and built using **TF-IDF vectorization** and **cosine similarity**. Below is a description of each file in the project.

---

## Project Structure and File Descriptions

### **Data Files (Stored in the `data` folder)**

- `Coursera.csv`:  
  The main dataset used for building the recommendation system, containing course descriptions and metadata.  

- `coursera_processed_data.csv`:  
  A processed version of the Coursera dataset with clean and structured data for easier analysis.  

- `coursera_processed_data_with_cluster.csv`:  
  The Coursera dataset after applying K-means clustering, with each course assigned a category label (e.g., Art, Cybersecurity).

- `mooc_action_features.tsv`, `mooc_actions.tsv`, and `mooc_action_labels.tsv`:  
  Stanford dataset files used for exploration but not incorporated into the final system.  

- `HXPC13_DI_v3_11-13-2019.csv`:  
  A dataset from the Harvard collection explored early in the project but excluded due to insufficient course data.  

- `Person Course Documentation.pdf` & `Person Course Deidentification.pdf`:  
  Documents related to the Harvard dataset describing the data and its anonymization process.

### **Exploration Files**

- `explore_harvard_data.ipynb`:  
  A Jupyter notebook used to explore the Harvard dataset. This analysis revealed a low user-course interaction rate (~1%) and only five courses.

- `explore_stanford_data.ipynb`:  
  A Jupyter notebook used to explore the Stanford dataset. The dataset only contained course IDs without names, making it difficult to use for recommendations.

### **Clustering and Recommendation Files**

- `clustering.ipynb`:  
  This notebook contains the code for applying K-means clustering to the Coursera dataset to generate course categories. Categories like "Art" and "Machine Learning" were created to help manage and filter the dataset.

- `recommendation_system.ipynb`:  
  The main notebook for building the recommendation system. It uses **TF-IDF Vectorization** to convert course descriptions into feature vectors and **cosine similarity** to recommend courses based on content.


### **Dashboard and Similarity Matrix**

- `similarity_matrix.pkl`:  
  A serialized similarity matrix used to speed up the recommendation process by storing precomputed course similarities.

## Conclusion

This project demonstrates the steps taken to create a content-based recommendation system by exploring, clustering, and analyzing multiple datasets. The system is designed for easy dataset management and includes a dashboard for viewing course categories.
