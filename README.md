# Credit Risk Profile Prediction

This project provides a modular system for predicting credit risk profiles using various machine learning models, *including Logistic Regression, Decision Tree, and Random Forest*. Based on the available dataset, the system trains the best-performing model and saves it for future use in credit risk assessment.

The dataset has been processed using `credit_score_calculation.py` and `risk_profile.py` to condense client profile data `(age, annual_income, debt_to_income_ratio, etc.)` into three primary features: `credit_score`, `loan_amount`, and `default` status.

This system leverages:

- **Data Preprocessing:** For efficient handling of relevant features.
- **Model Selection and Evaluation:** To identify and train the best model.
- **Risk Profile Calculation:** Using Bayesian updates for customizable risk assessments.
- **Visualization:** To support insights and data understanding.

The codebase is organized into distinct modules for easy readability, reusability, and maintainability.


## Project Structure:
.
├── risk_profile.py                             # Script to preprocess the original dataset
├── main.py                                     # Main script to train and save the model
├── data_loader_and_processing.py               # Module for data loading and processing
├── calculate_risk_and_model_selection          # Module for risk calculations and model selection
├── visualization.py                            # Data visualization functions
├── predict_new_data.py                         # Prediction module for new credit profiles
├── update_risk_profile.py                      # Module to update risk profiles using Bayesian methods
└── README.md                                   # Project documentation

## Installation:

**Prerequisites:**
This project requires several machine learning and visualization libraries, which can be installed using `pip`.

**Install Required Libraries:**
To use this project you have to install the necessary dependencies run: `pip install -r requirements.txt` in your terminal to install:
- *pandas* for data handling.
- *scikit-learn* for machine learning models and metrics.
- *matplotlib* and *seaborn* for data visualization.
- *joblib* for storing the model and risk profile for future use.


## Using This Project:
1. Clone the repository using `git clone https://github.com/Radhwane-py/Credit_Risk_Assessment` and then run the command `cd Credit_Risk_Assessment`
2. Ensure that you have all the required libraries installed.
3. Ensure that your original dataset is in CSV format and includes the relevant information about the credit profiles of your company.
4. Update `credit_score_calculation.py` and `risk_profile.py` to fit the specifics of your dataset if necessary and ensure it contains a `default` feature for model training.
5. set the filepath in `risk_profile.py` to point to your original dataset location and run it to generate `risk_profiles_for_Model_Training.csv` with `credit_score` data.
6. Update the filepath in `main.py` to point to the generated `risk_profiles_for_Model_Training.csv` location.
7. Run the command `python main.py` to train the model and save it (this script saves the best model for future predictions based on your dataset) .
8. Use the `predict_new_data.py` to predict the risk profile for new data.
9. You can use the `update_risk_profile.py`  to adjust the risk profile based on new insights or preferences, using `Bayesian Methods`.

**Author:**

This project was developed by           *RADHWANE BENAISSA*.
Contributions and suggestions are welcome.
Please feel free to raise issues or submit pull requests to improve this project.
