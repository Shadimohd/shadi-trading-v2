import streamlit as st
import pandas as pd
from coinbase.wallet.client import Client

# Pulling keys safely from Streamlit Secrets
try:
    client = Client(st.secrets["API_KEY"], st.secrets["API_SECRET"])
    st.success("Successfully connected to Coinbase!")
except Exception as e:
    st.error("Connection failed. Check your Secrets in Streamlit.")

st.title("🚀 Shadi's Portfolio V2")
st.metric("Target Portfolio", "$20.96", delta="+$5.92")
