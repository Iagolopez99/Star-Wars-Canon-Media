import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder, ColumnsAutoSizeMode
from app import load_media, filter_media_type, filter_title, filter_release_date, reset_filters, hide_consumed, filter_unreleased

st.set_page_config(
    page_title="Media Tracker",
    page_icon="☑",
)

st.title("Canon Media Tracker")

full_df = load_media("data/progress.csv")
if 'Consumed' not in full_df:
    full_df['Consumed'] = False

df = full_df.copy()
df = df.drop(df.columns[[0]], axis=1)

#progress_df = load_media("data/all_media.csv")
#if 'Consumed' not in progress_df:
#    progress_df['Consumed'] = False

# Initialize session state for filters
if 'media_types' not in st.session_state:
    st.session_state.media_types = []
if 'title_search' not in st.session_state:
    st.session_state.title_search = ""
if 'hide' not in st.session_state:
    st.session_state.hide = 'Show Both'
if 'unreleased' not in st.session_state:
    st.session_state.unreleased = False

with st.expander('Click for filtering options.'):
    media_types = st.multiselect(
        'Select a type of media:', 
        df['Media'].sort_values().unique(), 
        help='A: Audio, C: Comics, F: Films, JR: Junior novels, N: Novels, TV: Television, VG: Videogame',
        default=st.session_state.media_types
    )
    title_search = st.text_input('Search for a title:', value=st.session_state.title_search)

    unreleased = st.toggle('Hide unreleasead media.', value=st.session_state.unreleased, disabled=False)
    
    hide = st.select_slider('Hide/Show Consumed/Unsonsumed media.', ['Hide Consumed', 'Show Both', 'Hide Unconsumed'], value=st.session_state.hide)
   
    st.session_state.media_types = media_types
    st.session_state.title_search = title_search
    st.session_state.hide = hide
    st.session_state.unreleased = unreleased

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
if hide:
    df = hide_consumed(df, hide)
if unreleased:
    df = filter_unreleased(df)

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

    for index, row in updated_data.iterrows():   
        full_df.loc[full_df['Title'] == row['Title'], 'Consumed'] = row['Consumed']

    full_df.to_csv('data/progress.csv', index=False)
    # hay q meterlo con un wait para que se vea tantito
    st.success("Changes saved successfully!")
    st.rerun()

st.markdown("**Consumed items:**") 
st.info(df['Consumed'].value_counts().get(True,0))
st.markdown("**Total items:**") 
st.info(len(df))

