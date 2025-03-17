import pandas as pd

def load_media():
    return pd.read_csv("data/all_media.csv")

def filter_media(df, media_type=None, year=None, consumed=None):
    # filters media table based on user selection
    if media_type:
        df = df[df["Media"] == media_type]
    if year:
        df = df[df["Year"] == year]
    return df