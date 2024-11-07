def calculate_credit_score(age, annual_income, debt_to_income_ratio, employment_years, num_credit_accounts,
                           credit_utilization_data, loan_amount, loan_term, loan_type_data, employment_status_data):
    # Define weights for each factor.
    factors = {
        "age": 0.10,
        "annual_income": 0.15,
        "debt_to_income_ratio": 0.15,
        "employment_years": 0.10,
        "num_credit_accounts": 0.15,
        "credit_utilization": 0.10,
        "loan_amount": 0.05,
        "loan_term": 0.05,
        "loan_type": 0.05,  
        "employment_status": 0.10  
    }

    # Calculate weighted values for each factor.
    weighted_age = age * factors["age"]
    weighted_annual_income = annual_income * factors["annual_income"]
    weighted_debt_to_income_ratio = debt_to_income_ratio * factors["debt_to_income_ratio"]
    weighted_employment_years = employment_years * factors["employment_years"]
    weighted_num_credit_accounts = num_credit_accounts * factors["num_credit_accounts"]
    weighted_loan_amount = loan_amount * factors["loan_amount"]
    weighted_loan_term = loan_term * factors["loan_term"]

    # Assign weights for categorical columns.
    loan_type_impact = {'loan_type_personal': 0.8, 'loan_type_mortgage': 1.2, 'loan_type_auto': 1.0, 'loan_type_student': 0.9}
    employment_status_impact = {'employment_status_employed': 1.0, 'employment_status_self-employed': 0.9, 'employment_status_unemployed': 0.5, 'employment_status_retired': 0.8}
    credit_utilization_impact = {'credit_utilization_low': 1.0, 'credit_utilization_medium': 0.9, 'credit_utilization_high': 0.8}

    weighted_loan_type = sum(loan_type_data.get(col, 0) * impact for col, impact in loan_type_impact.items())
    weighted_employment_status = sum(employment_status_data.get(col, 0) * impact for col, impact in employment_status_impact.items())
    weighted_credit_utilization = sum(credit_utilization_data.get(col, 0) * impact for col, impact in credit_utilization_impact.items())

    credit_score = (weighted_age + weighted_annual_income +
                    weighted_debt_to_income_ratio + weighted_employment_years +
                    weighted_num_credit_accounts + weighted_credit_utilization +
                    weighted_loan_amount + weighted_loan_term +
                    weighted_loan_type + weighted_employment_status)
    
    # Scaling the credit score to a range of 300 to 850.

    min_score = 300
    max_score = 850
    normalized_credit_score = int(min_score + (credit_score / 100) * (max_score - min_score))

    return normalized_credit_score
