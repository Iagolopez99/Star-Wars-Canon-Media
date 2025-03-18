import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder, ColumnsAutoSizeMode
from app import load_media, filter_media_type, filter_title, filter_release_date, reset_filters

st.set_page_config(
    page_title="Media Tracker",
    page_icon="☑",
)

st.title("Canon Media Tracker")

df = load_media("data/progress.csv")
all_media = load_media("data/all_media.csv")
df = df.drop(df.columns[[0]], axis=1)

# Initialize session state for filters
if 'media_types' not in st.session_state:
    st.session_state.media_types = []
if 'title_search' not in st.session_state:
    st.session_state.title_search = ""

with st.expander('Click for filtering options.'):
    media_types = st.multiselect(
        'Select a type of media:', 
        df['Media'].sort_values().unique(), 
        help='A: Audio, C: Comics, F: Films, JR: Junior novels, N: Novels, TV: Television, VG: Videogame',
        default=st.session_state.media_types
    )
    title_search = st.text_input('Search for a title:', value=st.session_state.title_search)

    st.session_state.media_types = media_types
    st.session_state.title_search = title_search

    if title_search:
        st.info(f"Last search: '{title_search}'")

    if st.button('Reset Filters'):
        reset_filters()
        st.rerun()

    #filtered_release_dates = pd.to_datetime(df['Released'], errors='coerce').dropna().sort_values().dt.strftime('%Y-%m-%d').unique()
    #release_date_range = st.select_slider(
    #    'Select a range for the release date.',
    #    options=filtered_release_dates,
    #    value=(filtered_release_dates[0], filtered_release_dates[-1])  # Default: Full range
    #)
    #start_release_date, end_release_date = release_date_range

if media_types:
    df = filter_media_type(df, media_types)
if title_search:
    df =  filter_title(df, title_search)
#if release_date_range:
#    df = filter_release_date(df, start_release_date, end_release_date)

gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_default_column(editable=True)
gb.configure_column('Consumed', editable=True, cellEditor='agCheckboxCellEditor')
grid_options = gb.build()

st.write("Mark media as consumed by interacting with the table.")

grid_response = AgGrid(
    df,
    gridOptions=grid_options,
    enable_enterprise_modules=False,
    allow_unsafe_jscode=True,
    columns_auto_size_mode=ColumnsAutoSizeMode.FIT_CONTENTS
)


updated_data = grid_response['data']

if st.button('Save Changes', icon='🗳️', use_container_width=True):
    #updated_data = grid_response['data']
    #media_types = ''
    #title_search = ''
    updated_data.to_csv('data/progress.csv')
    st.rerun()

st.markdown("**Consumed items:**") 
st.info(df['Consumed'].value_counts().get(True,0))
st.markdown("**Total items:**") 
st.info(len(df))

