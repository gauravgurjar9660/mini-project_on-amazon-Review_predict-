import streamlit as st
import joblib
import re
import nltk
from nltk.corpus import stopwords

# NLTK stopwords download (sirf ek baar zaroorat padti hai)
nltk.download('stopwords', quiet=True)
stop_words = set(stopwords.words('english'))

# Saved model aur vectorizer load karein
cv = joblib.load('count_vectorizer.pkl')
model = joblib.load('nlp_model.pkl')

def clean_text(text):
    text = re.sub('[^A-Za-z]', ' ', text).lower().strip()
    text = ' '.join([word for word in text.split() if word not in stop_words])
    return text

st.title("Amazon Mobile Review Rating Predictor ")
st.write("Submit a mobile phone review, and our AI will predict the user's rating (from 1 to 5)!")

user_input = st.text_area("Please enter your review here (in English):")

if st.button("Predict Rating"):
    if user_input:
        cleaned_review = clean_text(user_input)
        vectorized_review = cv.transform([cleaned_review])
        prediction = model.predict(vectorized_review)
        
        st.success(f"Predicted Rating: {prediction[0]} ")
    else:
        st.warning("Please provide a review to predict the rating.")