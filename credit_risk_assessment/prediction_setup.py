import pandas as pd

# Predicting after selecting the best model.
def predict_new_data(model, new_data):
    new_data_df = pd.DataFrame(new_data)
    predictions = model.predict_proba(new_data_df)[:, 1]
    return predictions