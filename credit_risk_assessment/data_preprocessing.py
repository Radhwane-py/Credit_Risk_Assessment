import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def preprocess_data(df):
    # Preprocessing steps
    df.dropna(inplace=True)
    df['loan_amount'] = df['loan_amount'].astype(float)
    return df
