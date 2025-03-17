import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from app import load_media, filter_media_type, filter_title

st.set_page_config(
    page_title="Media Table",
    page_icon="📚",
)

st.title("Canon Media Table")

df = load_media()
df = df.drop(df.columns[[0]], axis=1)

media_types = st.multiselect('Select a type of media.', df['Media'].sort_values().unique())
title_search = st.text_input('Search for a title.')

if media_types:
    df = filter_media_type(df, media_types)
if title_search:
    df =  filter_title(df, title_search)
   

AgGrid(df)

st.markdown("**Total items:**") 
st.info(len(df))
