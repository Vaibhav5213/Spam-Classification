import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_PATH = os.path.join(BASE_DIR, "../data/raw_sms.csv")
OUTPUT_PATH = os.path.join(BASE_DIR, "../data/cleaned_sms.csv")
df = pd.read_csv(DATA_PATH, encoding = 'latin1')
df = df[['v1', 'v2']]
df.columns = ['label', 'message']
df['label'] = df['label'].str.lower().str.strip()
df.to_csv(OUTPUT_PATH, index = False)
print(f"Cleaned data saved to {OUTPUT_PATH}")