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
