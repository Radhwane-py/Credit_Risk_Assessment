import pandas as pd
from credit_score_calculation import calculate_credit_score
from sklearn.preprocessing import StandardScaler

def process_and_save_risk_profiles(data, filename="risk_profiles_for_Model_Training.csv"):
    # Save original loan amount.
    original_loan_amount = data['loan_amount'].copy()

    # One-hot encode for categorical columns.
    data = pd.get_dummies(data, columns=['credit_utilization', 'loan_type', 'employment_status'])

    # Standardize the numeric columns.
    scaler = StandardScaler()
    numeric_features = ['age', 'annual_income', 'debt_to_income_ratio', 'employment_years', 'num_credit_accounts', 'loan_amount', 'loan_term']
    data[numeric_features] = scaler.fit_transform(data[numeric_features])

    # Calculate credit score for each row.
    credit_scores = data.apply(lambda row: calculate_credit_score(
        row['age'], row['annual_income'], row['debt_to_income_ratio'], row['employment_years'],
        row['num_credit_accounts'], row.filter(regex='^credit_utilization_').to_dict(), row['loan_amount'],
        row['loan_term'], row.filter(regex='^loan_type_').to_dict(), row.filter(regex='^employment_status_').to_dict()
    ), axis=1)

    # Create final DataFrame and save the result to a CSV file.
    result_df = pd.DataFrame({
        'credit_score': credit_scores,
        'loan_amount': original_loan_amount,
        'default': data['default']
    })

    result_df.to_csv(filename, index=False)
    print(f"Results saved to {filename}")

# Prepare the dataset for the Model training.
dataset = pd.read_csv(r'D:\PROJECT\bank_dataset_with_default.csv')
process_and_save_risk_profiles(dataset)
