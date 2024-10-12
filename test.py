import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd



st.title('Map plotter')

file_uploaded = st.file_uploader('Upload a file', type='csv')

text_input = st.text_input('List of towns seperated by comma')


if file_uploaded is not None:
    st.write('file uploaded')

    df = pd.read_csv(file_uploaded)

    columns = df.columns.to_list()

    LON = st.selectbox('Select Longitude column', columns)

    LAT = st.selectbox('Select latittude column', columns)

    # label = st.selectbox('Select label columns', columns)

    working_df = df[[LON, LAT,]]

    zoom = st.slider(label='Zoom level', min_value=4, max_value=8)

    map = st.map(data=working_df, longitude=LON, latitude=LAT, zoom=zoom)

    map


# elif text_input is not None:
#     pass



st.map

