import pandas as pd

def calculate_wealth(monthly_investment, annual_rate, years, initial_funds=0):
    
    """Calculates yearly growth including starting capital."""
   
    months = years * 12
    monthly_rate = (annual_rate / 100) / 12
    balances = []
    labels = []
    current_balance = initial_funds             # Factor in windfalls or existing savings

    for m in range(1, months + 1):
        current_balance = (current_balance + monthly_investment) * (1 + monthly_rate)
        if m % 12 == 0:
            balances.append(round(current_balance, 2))
            labels.append(f"Year {m//12}")
    return labels, balances

def get_spending_verdict(item_cost, project_total, years, rate):
    
    """Calculates the 'Opportunity Cost' of a purchase."""
    if item_cost <= 0:
        return "Enter a cost to see the impact."
    
    # Calculate what that money would grow into if invested instead
    
    future_loss = item_cost * ((1 + (rate/100)) ** years)
    impact_pct = (item_cost / project_total) * 100 if project_total > 0 else 100

    if impact_pct > 10:
        return f" **Verdict: DO NOT BUY.** This costs {impact_pct:.1f}% of your wealth. That money would have become **${future_loss:,.2f}**."
    elif impact_pct > 3:
        return f" **Verdict: CAUTION.** This is {impact_pct:.1f}% of your goal. You lose **${future_loss:,.2f}** in potential growth."
    else:
        return f" **Verdict: SAFE.** This purchase has a minor impact on your long-term wealth."

def get_ai_insight(rate, total):
    """Feedback based on simulation results."""
    if rate > 10:
       return "High-risk profile. Prepare for market volatility."
    elif total < 50000:
       return "Conservative growth. Consider increasing monthly contributions."
    else: 
        return "Balanced approach. Consistent accumulation detected."