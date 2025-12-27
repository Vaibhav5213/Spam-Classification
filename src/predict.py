import os
import joblib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(os.path.join(BASE_DIR, "../models/spam_classifier_model.pkl"))
vectorizer = joblib.load(os.path.join(BASE_DIR, "../models/vectorizer.pkl"))

def predict_spam(message):
  vec = vectorizer.transform([message])
  return model.predict(vec)[0]

#Example usage
if __name__ == "__main__":
  print("--- CLI Spam Classifier (Type 'exit' to quit) ---")
    while True:
        user_msg = input("\nEnter message: ")
        if user_msg.lower() == 'exit':
            break
        
        result = predict_spam(user_msg)
        print(f"Prediction: {result.upper()}")
