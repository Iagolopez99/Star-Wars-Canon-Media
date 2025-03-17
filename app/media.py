import pandas as pd

def load_media():
    df = pd.read_csv("data/all_media.csv")
    
    return df

def filter_media_type(df, media_type):
    if media_type:
        df = df[df['Media'] == media_type]
    
    return df

def filter_title(df, title):
    if title:
        df = df[df['Title'].str.contains(title, case=False)]
        

        
    return df
