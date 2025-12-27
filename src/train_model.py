import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib
from sklearn.metrics import accuracy_score, confusion_matrix

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_PATH = os.path.join(BASE_DIR, "../data/cleaned_sms.csv")
MODEL_PATH = os.path.join(BASE_DIR, "../models/spam_classifier_model.pkl")
VECT_PATH = os.path.join(BASE_DIR, "../models/vectorizer.pkl")

df = pd.read_csv(DATA_PATH)
x = df['message']
y = df['label']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

vectorizer = CountVectorizer()
x_train_vec = vectorizer.fit_transform(x_train)
x_test_vec = vectorizer.transform(x_test)

model = MultinomialNB()
model.fit(x_train_vec, y_train)

joblib.dump(model, MODEL_PATH)
joblib.dump(vectorizer, VECT_PATH)
print(f"Model saved to {MODEL_PATH}, vectorizer saved to {VECT_PATH}")

y_pred = model.predict(x_test_vec)
print("Accuracy: ", accuracy_score(y_test, y_pred))
print("Confusion Matrix: \n", confusion_matrix(y_test, y_pred))