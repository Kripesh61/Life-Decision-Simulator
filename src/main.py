import streamlit as st
import pandas as pd
import json
import os
from logic import calculate_wealth, get_ai_insight, get_spending_verdict

# Mandatory Path Logic
APP_PATH = os.path.dirname(os.path.abspath(__file__))
def get_data_path(filename: str) -> str:
    return os.path.join(APP_PATH, "data", filename)

st.set_page_config(page_title="Life Decision Simulator Pro", layout="wide")
st.title(" Life Decision & Spending Simulator")

# --- SIDEBAR: DYNAMIC FINANCIAL PROFILE ---
st.sidebar.header(" Your Profile")
salary = st.sidebar.number_input("Annual Salary ($)", 0, 1000000, 60000)
tax_rate = st.sidebar.slider("Estimated Tax Rate (%)", 0, 50, 25)
after_tax_monthly = (salary * (1 - tax_rate/100)) / 12

st.sidebar.divider()
st.sidebar.header(" Strategy")
name = st.sidebar.text_input("Scenario Name", "Retirement Goal")
save_pct = st.sidebar.slider("Percent of Income to Save (%)", 0, 100, 20)
monthly_val = after_tax_monthly * (save_pct / 100)
years = st.sidebar.slider("Growth Years", 1, 40, 20)
rate = st.sidebar.slider("Annual Return (%)", 1, 15, 7)

st.sidebar.divider()
st.sidebar.header("⚡ Sudden Events")
windfall = st.sidebar.number_input("Sudden Income (Bonus/Gift) ($)", 0, 1000000, 0)
expense = st.sidebar.number_input("Emergency Expense ($)", 0, 1000000, 0)
initial_capital = windfall - expense

# --- CORE CALCULATIONS ---
labels, balances = calculate_wealth(monthly_val, rate, years, initial_capital)
final_total = balances[-1] if balances else 0

# --- SPENDING ADVISOR ---
st.header("🛒 The Spending Advisor")
item = st.text_input("What are you thinking of buying?", "A New Car")
cost = st.number_input(f"Cost of {item} ($)", 0, 1000000, 0)

if cost > 0:
    st.warning(get_spending_verdict(cost, final_total, years, rate))

# --- VISUALIZATION & HISTORY COMPARISON ---
st.divider()
col1, col2 = st.columns([2, 1])

data_file = get_data_path("scenarios.json")
history = []
if os.path.exists(data_file):
    with open(data_file, "r") as f:
        history = json.load(f)

with col1:
    st.subheader(f"Projection: {name}")
    chart_df = pd.DataFrame({"Current Path": balances}, index=labels)
    
    # Overlay Comparison
    if history:
        to_compare = st.multiselect("Overlay Saved Scenarios to Compare:", [h['Scenario'] for h in history])
        for h in history:
            if h['Scenario'] in to_compare:
                _, h_bal = calculate_wealth(h.get('Monthly', 500), h.get('Rate', 7), h.get('Years', 10), h.get('Initial', 0))
                chart_df[h['Scenario']] = h_bal
    
    st.line_chart(chart_df)

with col2:
    st.metric("Future Wealth", f"${final_total:,.2f}")
    st.write(f"Monthly Savings: **${monthly_val:,.2f}**")
    st.info(f"**AI Insight:** {get_ai_insight(rate, final_total)}")

# --- SCENARIO MANAGER: SAVE / DELETE ---
st.header(" Scenario Manager")
if st.button("Save Current Scenario"):
    os.makedirs(os.path.dirname(data_file), exist_ok=True)
    history.append({
        "Scenario": name, "Monthly": monthly_val, "Years": years, 
        "Rate": rate, "Initial": initial_capital, "Total": final_total
    })
    with open(data_file, "w") as f:
        json.dump(history, f, indent=4)
    st.rerun()

if history:
    df_history = pd.DataFrame(history)
    st.table(df_history[["Scenario", "Total", "Monthly"]])
    
    # Delete Feature
    target = st.selectbox("Select Scenario to Delete:", df_history["Scenario"].unique())
    if st.button("🗑️ Delete Selected"):
        history = [h for h in history if h["Scenario"] != target]
        with open(data_file, "w") as f:
            json.dump(history, f, indent=4)
        st.rerun()