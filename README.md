# mini-project_on-amazon-Review_predict-
An NLP-based Streamlit web app that predicts Amazon mobile review ratings (1 to 5 stars) from text.
# Amazon Mobile Review Rating Predictor 

An end-to-end Natural Language Processing (NLP) web application built to predict user ratings (1 to 5 stars) based on the text of Amazon mobile phone reviews. 

##  Project Overview
Customer reviews contain valuable sentiments, but reading thousands of them is difficult. This project uses Machine Learning to analyze the sentiment and text patterns of a review and automatically predicts the star rating the user likely gave. 

**Key Highlights:**
* **Text Preprocessing:** Cleaned the raw review text by removing special characters, converting to lowercase, and removing English stopwords using `NLTK`.
* **Vectorization:** Converted the cleaned text data into numerical format using `CountVectorizer`.
* **Model Training:** Trained a classification model to categorize reviews into 5 distinct rating classes.
* **Web Interface:** Built an interactive frontend using `Streamlit` where users can type a real-time review and get instant rating predictions.

## 🛠️ Tech Stack & Libraries
- **Language:** Python
- **Machine Learning:** Scikit-Learn, NLTK, Pandas, NumPy
- **Web Framework:** Streamlit
- **Model Saving:** Joblib

##  Project Structure
```text
Amazon-Review-Rating-Predictor
  amazon.py               # Main Streamlit web application script
  amzon_work.ipynb        # Jupyter Notebook with EDA and model training
  count_vectorizer.pkl    # Saved NLP vectorizer
  nlp_model.pkl           # Saved Machine Learning model
  requirements.txt        # Required Python dependencies
