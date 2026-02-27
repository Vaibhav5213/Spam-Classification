# 📧 SMS Spam Classifier

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://spam-classification-model.streamlit.app/)

> **[🚀 Click here to try the Live Demo](https://spam-classification-model.streamlit.app/)**
 
A machine learning project that detects spam text messages with **98.3% accuracy**. 
It uses a **Naive Bayes** classifier trained on the SMS Spam Collection dataset and includes both a visual dashboard and a production-ready API.

## 🚀 Features
* **Production API (FastAPI):** A fast, deployable backend API wrapper for seamless software integration.
* **Interactive App (Streamlit):** A web-based user interface to test messages visually in real-time.
* **Model Training:** Trains a Multinomial Naive Bayes model using Scikit-Learn.
* **Data Cleaning:** Automated pipeline to clean and preprocess raw SMS data.
* **CLI Tool:** A command-line interface for quick local testing.

## 📂 Project Structure
```text
spam_classifier_project/
├── data/          # Contains raw and cleaned CSV datasets
├── models/        # Saved model (.pkl) and vectorizer files
├── src/           # Source code (cleaning, training, CLI prediction, and FastAPI main.py)
└── requirements.txt
