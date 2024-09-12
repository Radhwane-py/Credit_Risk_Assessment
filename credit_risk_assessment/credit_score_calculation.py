# credit_score_calculation.py

def calculate_credit_score(age, annual_income, credit_score, debt_to_income_ratio, employment_years, num_credit_accounts, payment_history, credit_utilization, recent_inquiries, loan_amount, loan_term):
    factors = {
        "age": 0.05,
        "annual_income": 0.10,
        "credit_score": 0.20,
        "debt_to_income_ratio": 0.10,
        "employment_years": 0.10,
        "num_credit_accounts": 0.10,
        "payment_history": 0.15,
        "credit_utilization": 0.10,
        "recent_inquiries": 0.05,
        "loan_amount": 0.025,
        "loan_term": 0.025
    }

    weighted_age = age * factors["age"]
    weighted_annual_income = annual_income * factors["annual_income"]
    weighted_credit_score = credit_score * factors["credit_score"]
    weighted_debt_to_income_ratio = debt_to_income_ratio * factors["debt_to_income_ratio"]
    weighted_employment_years = employment_years * factors["employment_years"]
    weighted_num_credit_accounts = num_credit_accounts * factors["num_credit_accounts"]
    weighted_payment_history = payment_history * factors["payment_history"]
    weighted_credit_utilization = credit_utilization * factors["credit_utilization"]
    weighted_recent_inquiries = recent_inquiries * factors["recent_inquiries"]
    weighted_loan_amount = loan_amount * factors["loan_amount"]
    weighted_loan_term = loan_term * factors["loan_term"]

    credit_score = (weighted_age + weighted_annual_income + weighted_credit_score +
                    weighted_debt_to_income_ratio + weighted_employment_years +
                    weighted_num_credit_accounts + weighted_payment_history +
                    weighted_credit_utilization + weighted_recent_inquiries +
                    weighted_loan_amount + weighted_loan_term)

    min_score = 300
    max_score = 850
    normalized_credit_score = min_score + (credit_score / 100) * (max_score - min_score)

    return normalized_credit_score
