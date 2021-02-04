import streamlit as st
import pymongo
from pymongo import MongoClient
import matplotlib as plot
import pandas as pd
import numpy as np

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

songs_per_duration = pd.DataFrame({
    "time": ["0min", "1min", "3min", "6min", "9min", "12min", "15min"],
    "count": [
        spotify_db.songs.find(
            {"duration_ms": {"$lt": 60000}}).count(),
        spotify_db.songs.find(
            {"duration_ms": {"$gte": 60000, "$lt": 180000}}).count(),
        spotify_db.songs.find(
            {"duration_ms": {"$gte": 180000, "$lt": 360000}}).count(),
        spotify_db.songs.find(
            {"duration_ms": {"$gte": 360000, "$lt": 540000}}).count(),
        spotify_db.songs.find(
            {"duration_ms": {"$gte": 540000, "$lt": 720000}}).count(),
        spotify_db.songs.find(
            {"duration_ms": {"$gte": 720000, "$lt": 900000}}).count(),
        spotify_db.songs.find({"duration_ms": {"$gte": 900000}}).count()
    ]
}).set_index('time')

df_valences = pd.DataFrame(
    correlations[correlations["base_col"] == "valence"], columns=["compared_col"])
df_danceability = pd.DataFrame(
    correlations[correlations["base_col"] == "danceability"], columns=["compared_col"])

correlations_valence = pd.DataFrame(
    correlations[correlations["base_col"] == "valence"], columns=["value"]).set_index(df_valences['compared_col'])
correlations_danceability = pd.DataFrame(
    correlations[correlations["base_col"] == "danceability"], columns=["value"]).set_index(df_danceability['compared_col'])


st.write("Correlation valence")
st.bar_chart(correlations_valence)

st.write("Correlation danceability")
st.bar_chart(correlations_danceability)

# st.write(songs_per_duration)

st.line_chart(songs_per_duration)
