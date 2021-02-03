import pandas as pd
from pymongo import MongoClient
import streamlit as st

client = MongoClient('localhost',
                    port=4344,
                    username='root',
                    password='root',
                    authMechanism='SCRAM-SHA-256')
db = client.crimes
table = db.documents

st.write("""
Bonjour, 

bienvenue sur une représentation de crime commis par année pour chaque arme
""")

@st.cache
def load_data(year: int):
    victimWithEachWeapon = table.aggregate([
    {"$match": {"Year": year}},
    { "$group" : {
        "_id": "$Weapon", "victimes": {"$sum": "$Victim Count"}
    }}
])

    return list(victimWithEachWeapon)

user_input = st.number_input("Année du crime commis", value=1980)

data = load_data(user_input)
df = pd.DataFrame(data)

if(len(df)):
    st.write(df)
    st.bar_chart(df.rename(columns={'_id': 'index'}).set_index('index'))
else:
    st.write("""
    Aucun crime commis sur cette date
""")