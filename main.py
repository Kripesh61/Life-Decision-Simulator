import streamlit as st
import pandas as pd
import json
import os
from logic import calculate_wealth, get_ai_insight

APP_PATH = os.path.dirname(os.path.abspath(__file__))

def get_data_path(filename: str) -> str:

    return os.path.join(APP_PATH, "data", filename)


st.set_page_config(page_title="Life Decision Simulator", layout="wide")
st.title("Life Decision Simulator")

# --- SIDEBAR INPUTS ---
st.sidebar.header("Scenario Settings")

name = st.sidebar.text_input("Scenario Name", "New Car vs Savings")
monthly = st.sidebar.number_input("Monthly Contribution ($)", 0, 10000, 500)
years = st.sidebar.slider("Time Horizon (Years)", 1, 40, 10)
rate = st.sidebar.slider("Expected Return (%)", 1, 15, 7)

labels, balances = calculate_wealth(monthly, rate, years)

