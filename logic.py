import pandas as pd

def calculate_wealth(monthly_investment, annual_rate, years):

    months = years * 12
    monthly_rate = (annual_rate / 100) / 12

    