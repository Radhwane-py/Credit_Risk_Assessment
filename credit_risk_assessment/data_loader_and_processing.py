import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(file_path):
    return pd.read_csv(file_path)

def preprocess_data(df):
# Processing steps.
    df.dropna(inplace=True)
    df['loan_amount'] = df['loan_amount'].astype(float)
    df['default'] = df['default'].astype(int)
    return df

def split_data(df):
    X = df.drop('default', axis=1)
    y = df['default']
    return train_test_split(X, y, test_size=0.2, random_state=42)
