import joblib
from prediction_setup import predict_new_data

def load_model(filename='best_model.joblib'):
    # Load a saved model from a file.
    try:
        model = joblib.load(filename)
        print("Model loaded successfully.")
        return model
    except FileNotFoundError:
        print(f"Model file '{filename}' not found. Please train and save the model using main.py.")
        return None

def prompt_predict_new_data(model):
    # Prompt user to predict risk for new data.
    print("\n--- Predict Risk for New Data ---")
    new_credit_scores = []
    new_loan_amounts = []
    while True:
        try:
            score = int(input("Enter credit score (or -1 to stop): "))
            if score == -1:
                break
            loan_amount = int(input(f"Enter loan amount for credit score {score}: "))
            new_credit_scores.append(score)
            new_loan_amounts.append(loan_amount)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    new_data_to_predict = {'credit_score': new_credit_scores, 'loan_amount': new_loan_amounts}
    predictions = predict_new_data(model, new_data_to_predict)
    print("Predictions for New Data:", predictions)
    return predictions

def main():
    # Load the saved model.
    model = load_model()
    if model is None:
        return

    # Prompt user for new data predictions.
    prompt_predict_new_data(model)

if __name__ == "__main__":
    main()
