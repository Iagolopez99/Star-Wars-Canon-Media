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
    st.session_state.hide = 'Show Both'
    st.session_state.unreleased = False

def hide_consumed(df, hide):
    if hide == 'Hide Consumed':
        df = df.loc[df['Consumed'] == False]
    if hide == 'Hide Unconsumed':
        df = df.loc[df['Consumed'] == True]
    if hide == 'Show Both':
        pass

    return df

def filter_unreleased(df):
    df = df[df['Released'] != 'Uknown']
    df = df[~df['Released'].str.contains('XX', na=False)]
    df['Released'] = pd.to_datetime(df['Released']).dt.strftime('%Y-%m-%d')

    return df

#def save_changes():