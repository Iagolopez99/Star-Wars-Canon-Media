import pandas as pd
from app import load_media

df = load_media()
df = df.drop(df.columns[[0]], axis=1)
df['Consumed'] = False
df.to_csv('data/progress.csv')