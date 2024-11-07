from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import roc_auc_score
import pandas as pd
from collections import OrderedDict

def calculate_risk_profile(X_train, y_train, model_type='x'):
    if model_type == 'logistic':
        model = LogisticRegression()
    elif model_type == 'random_forest':
        model = RandomForestClassifier()
    elif model_type == 'decision_tree':
        model = DecisionTreeClassifier()
    else:
        raise ValueError("Invalid model type. Choose from 'logistic', 'random_forest', or 'decision_tree'.")

    model.fit(X_train, y_train)
    risk_profiles = model.predict_proba(X_train)[:, 1]
    initial_risk_profiles = pd.DataFrame({'credit_score': X_train['credit_score'], 'risk_profile': risk_profiles})
    initial_risk_profiles_dict = OrderedDict(initial_risk_profiles.sort_values(by='credit_score', ascending = False).set_index('credit_score')['risk_profile'].to_dict())
    return initial_risk_profiles_dict, model

def evaluate_model(X_test, y_test, model):
    y_pred = model.predict_proba(X_test)[:, 1]
    return roc_auc_score(y_test, y_pred)

# Iterating on different models and selecting the best one.

def select_best_model(X_train, y_train, X_test, y_test):
    models = ['logistic', 'random_forest', 'decision_tree']
    best_model = None
    best_auc = 0
    best_model_type = ''

    for model_type in models:
        _, model = calculate_risk_profile(X_train, y_train, model_type)
        auc = evaluate_model(X_test, y_test, model)
        if auc > best_auc:
            best_auc = auc
            best_model = model
            best_model_type = model_type

    return best_model, best_model_type, best_auc
