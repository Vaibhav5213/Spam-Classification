import streamlit as st
import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "../models/spam_classifier_model.pkl")
VECT_PATH = os.path.join(BASE_DIR, "../models/vectorizer.pkl")

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECT_PATH)

st.title("Spam Classifier")
st.write("Enter a message below to check if it looks like Spam or Ham (Safe).")

user_input = st.text_area("Message Content:", height = 100)

if st.button("Check Message"):
    if user_input:
        vec_input = vectorizer.transform([user_input])
        prediction = model.predict(vec_input)[0]
        if prediction == "spam":
            st.error("🚨 SPAM DETECTED! Be careful with this message.")
        else:
            st.success("✅ HAM (Safe). This message looks fine.")
    else:
        st.warning("Please enter a message first.")