import streamlit as st
from pymongo import MongoClient
import matplotlib as plot
import pandas as pd
import numpy as np


# def load_mongo_data(collection):
#     data = collection.find()
#     return data.count()


st.text('Spotify Dashboard')

client = MongoClient(
    host='mongo:27017',
    serverSelectionTimeoutMS=3000,
    username='root',
    password='root'
)

spotify_db = client.spotify

correlations = pd.DataFrame(list(spotify_db.correlations.find()), columns=[
                            "base_col", "compared_col", "value"])


df_valences = pd.DataFrame(
    correlations[correlations["base_col"] == "valence"], columns=["compared_col"])
df_danceability = pd.DataFrame(
    correlations[correlations["base_col"] == "danceability"], columns=["compared_col"])

correlations_valence = pd.DataFrame(
    correlations[correlations["base_col"] == "valence"], columns=["value"]).set_index(df_valences['compared_col'])
correlations_danceability = pd.DataFrame(
    correlations[correlations["base_col"] == "danceability"], columns=["value"]).set_index(df_danceability['compared_col'])



st.write("Correlation avec la valence")
st.bar_chart(correlations_valence)

st.write("Correlation avec la danceability")
st.bar_chart(correlations_danceability)

