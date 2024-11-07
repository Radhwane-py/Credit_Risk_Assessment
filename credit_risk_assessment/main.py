from data_loader_and_processing import load_data, preprocess_data, split_data
from calculate_risk_and_model_selection import select_best_model, calculate_risk_profile
from visualization import plot_distributions, plot_correlation_matrix, plot_feature_importances, plot_roc_curve
import joblib

def main():
    # Load and preprocess data.
    df = load_data('D:\PROJECT/risk_profiles_for_Model_Training.csv')
    df = preprocess_data(df)

    # Plot distributions and correlation matrix.
    plot_distributions(df)
    plot_correlation_matrix(df)

    # Split data for training and testing. 
    X_train, X_test, y_train, y_test = split_data(df)

    # Model selection
    best_model, best_model_type, best_auc = select_best_model(X_train, y_train, X_test, y_test)
    print(f"Best Model: {best_model_type}, AUC: {best_auc}")

    # Calculate initial risk profiles.
    risk_profiles, _ = calculate_risk_profile(X_train, y_train, model_type=best_model_type)
    print("Initial Risk Profiles:", risk_profiles)

    # Plot feature importances if Random Forest is the best model.
    if best_model_type == 'random_forest':
        plot_feature_importances(best_model, X_train)

    # Evaluate model and plot ROC curve.
    y_pred = best_model.predict_proba(X_test)[:, 1]
    plot_roc_curve(y_test, y_pred)

     # Save the trained model and initial risk profile dictionary.
    
    model_filename = 'best_model.joblib'
    joblib.dump(best_model, model_filename)
    print(f"Model saved as {model_filename}")

    risk_profile_filename = 'initial_risk_profiles.joblib'
    joblib.dump(risk_profiles, risk_profile_filename)
    print(f"Initial risk profiles saved as {risk_profile_filename}")

if __name__ == "__main__":
    main()
