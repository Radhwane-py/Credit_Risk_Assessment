import os
from dotenv import load_dotenv
from data_preprocessing import load_data, preprocess_data
from risk_profile import calculate_risk_profile
from bayes_update import update_risk_profile
load_dotenv()

def main():
    # Load and preprocess data
    data_path = os.getenv('DATA_PATH')
    df = load_data(data_path)
    df = preprocess_data(df)
    
    # Calculate initial risk profiles
    risk_profiles = calculate_risk_profile(df)
    print("Initial Risk Profiles:", risk_profiles)
    
    # Update risk profiles with new data
    new_data = {'A': 0.1, 'B': 0.2, 'C': 0.3}  
    updated_profiles = update_risk_profile(risk_profiles, new_data)
    print("Updated Risk Profiles:", updated_profiles)

if __name__ == "__main__":
    main()
