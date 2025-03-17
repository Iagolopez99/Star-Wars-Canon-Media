import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from app import load_media

st.set_page_config(
    page_title="Media Table",
    page_icon="📚",
)

st.title("Canon Media Table")

df = load_media()
df = df.drop(df.columns[[0]], axis=1)
AgGrid(df)
