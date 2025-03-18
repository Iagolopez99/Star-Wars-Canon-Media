import pandas as pd
import streamlit as st

def load_media(domain):
    df = pd.read_csv(domain)
    
    return df

def filter_media_type(df, media_types):
    if media_types:
        df = df[df['Media'].isin(media_types)]  
        
    return df

def filter_title(df, title):
    if title:
        df = df[df['Title'].str.contains(title, case=False)]
        
    return df

def filter_release_date(df, start, end):
    df = df[df['Released'].between(start, end)]
    return df


def reset_filters():
    st.session_state.media_types = []
    st.session_state.title_search = ""

#def save_changes():