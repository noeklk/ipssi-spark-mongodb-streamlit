import streamlit as st
from pymongo import MongoClient

def load_mongo_data(collection):
    data = collection.find()
    return data.count()


st.text('This is some text.')

client = MongoClient(
                    host = 'mongo:27017',
                    serverSelectionTimeoutMS = 3000,
                    username='root',
                    password='root'
)

db = client.laDB

st.write("Showing data for: ", db.test)
st.write(load_mongo_data(db.test))