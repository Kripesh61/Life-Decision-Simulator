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
#Life-Decision-Simulatorc
name = st.sidebar.text_input("Scenario Name", "New Car vs Savings")
monthly = st.sidebar.number_input("Monthly Contribution ($)", 0, 10000, 500)
years = st.sidebar.slider("Time Horizon (Years)", 1, 40, 10)
rate = st.sidebar.slider("Expected Return (%)", 1, 15, 7)

labels, balances = calculate_wealth(monthly, rate, years)

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader(f"Projection: {name}")
    chart_data = pd.DataFrame({"Wealth": balances}, index=labels)
    st.line_chart(chart_data)

    with col2:
     final_total = balances[-1] if balances else 0
     st.metric("Estimated Final Balance", f"${final_total:,.2f}")
     st.info(f"**AI Insight:** \n\n {get_ai_insight(rate, final_total)}")

     # --- SAVE/LOAD SECTION ---
st.divider()
st.header("Scenario Manager")

data_file = get_data_path("scenarios.json")

# 1. Load data safely
history = []
if os.path.exists(data_file):
    with open(data_file, "r") as f:
        history = json.load(f) 

if history:
    # 2. ADD COMPARISON (The "Unique/Complex" requirement)
   
    st.subheader("Compare Scenarios")
    to_compare = st.multiselect("Select scenarios to compare side-by-side:", options=[h["Scenario"] for h in history])
    
    
    if to_compare:
        
        # Filter data for chart
        
        compare_df = pd.DataFrame([h for h in history if h["Scenario"] in to_compare])
        st.bar_chart(data=compare_df, x="Scenario", y="Total") 



        




