import joblib
from bayes_update_setup import update_risk_profile
   
def load_initial_risk_profile(filename='initial_risk_profiles.joblib'):
    # Load the trained initial risk profiles dictionary from the saved file.
    try:
        initial_risk_profiles = joblib.load(filename)
        print("Initial risk profiles loaded successfully.")
        return initial_risk_profiles
    except FileNotFoundError:
        print(f"Initial risk profile file '{filename}' not found. Please train and save the model using main.py.")
        return None

def prompt_update_risk_profiles(risk_profiles):
    # Prompt user to update risk profiles.
    print("\n--- Update Risk Profiles ---")
    new_data = {}
    while True:
        try:
            score = int(input("Enter credit score (or -1 to stop): "))
            if score == -1:
                break
            likelihood = float(input(f"Enter likelihood for credit score {score}: "))
            new_data[score] = likelihood
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    updated_profiles = update_risk_profile(risk_profiles, new_data)
    print("Updated Risk Profiles:", updated_profiles)
    return updated_profiles

def main():
    # Load the initial risk profiles.
    risk_profiles = load_initial_risk_profile()
    if risk_profiles is None:
        return

    # Prompt user for risk profile updates.
    updated_profiles = prompt_update_risk_profiles(risk_profiles)
    print("Final Updated Risk Profiles:", updated_profiles)

if __name__ == "__main__":
    main()
