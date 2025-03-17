import pandas as pd

def load_media():
    df = pd.read_csv("data/all_media.csv")
    return df