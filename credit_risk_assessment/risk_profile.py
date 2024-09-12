import numpy as np
import pandas as pd
from credit_score_calculation import calculate_credit_score

def calculate_risk_profile(df):
    # Calculate credit score for each row
    df['credit_score'] = df.apply(lambda row: calculate_credit_score(
        row['age'],
        row['annual_income'],
        row['credit_score'],
        row['debt_to_income_ratio'],
        row['employment_years'],
        row['num_credit_accounts'],
        row['payment_history'],
        row['credit_utilization'],
        row['recent_inquiries'],
        row['loan_amount'],
        row['loan_term']
    ), axis=1)
    
    # Risk profile calculation
    risk_profiles = df.groupby('credit_score')['default'].mean()
    return risk_profiles
