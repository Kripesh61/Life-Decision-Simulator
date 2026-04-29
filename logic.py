import pandas as pd

def calculate_wealth(monthly_investment, annual_rate, years):

    months = years * 12
    monthly_rate = (annual_rate / 100) / 12

    balances = []
    labels = []
    current_balance = 0

    for m in range(1, months + 1):

        current_balance = (current_balance + monthly_investment) * (1 + monthly_rate)
        if m % 12 == 0:

            balances.append(round(current_balance, 2))
            labels.append(f"Year {m//12}")


    return labels, balances

def get_ai_insight(rate, total):

    if rate > 10:
       return " High-risk profile. While returns are high, prepare for potential market volatility." 
    
    





