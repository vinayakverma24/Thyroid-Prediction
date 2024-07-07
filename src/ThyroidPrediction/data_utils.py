import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def load_data(url):
    df = pd.read_csv(url)
    return df

def preprocess_data(df):
    # Define columns and handle missing values
    columns_thyroid_csv = ['age', 'sex', 'on_thyroxine', 'query_on_thyroxine',
                           'on_antithyroid_medication', 'sick', 'pregnant', 'thyroid_surgery',
                           'I131_treatment', 'query_hypothyroid', 'query_hyperthyroid', 'lithium',
                           'goitre', 'tumor', 'hypopituitary', 'psych', 'TSH_measured', 'TSH',
                           'T3_measured', 'T3', 'TT4_measured', 'TT4', 'T4U_measured', 'T4U',
                           'FTI_measured', 'FTI', 'TBG_measured', 'TBG', 'referral_source',
                           'Class']
    
    df[columns_thyroid_csv] = df[columns_thyroid_csv].replace('?', np.nan)
    df.drop('TBG', inplace=True, axis=1)
    columns_to_drop = ['TT4', 'TSH', 'FTI', 'T4U', 'T3']
    df.drop(columns_to_drop, inplace=True, axis=1)
    
    # Remove rows with missing values in 'age' and 'sex'
    remove_rows = ['age', 'sex']
    for col in remove_rows:
        df = df[df[col].notna()]
    
    # Convert binary categorical columns to numeric
    cols_to_binary = ['on_thyroxine', 'query_on_thyroxine',
                      'on_antithyroid_medication', 'sick', 'pregnant', 'thyroid_surgery',
                      'I131_treatment', 'query_hypothyroid', 'query_hyperthyroid', 'lithium',
                      'goitre', 'tumor', 'hypopituitary', 'psych', 'TSH_measured',
                      'T3_measured', 'TT4_measured', 'T4U_measured', 'FTI_measured',
                      'TBG_measured']
    
    for column in cols_to_binary:
        df[column] = df[column].map({'f': 0, 't': 1})
    
    # Convert 'sex' column
    df['sex'] = df['sex'].map({'F': 0, 'M': 1})
    
    # One-hot encode 'referral_source'
    df = pd.get_dummies(df, columns=['referral_source'])
    
    # Encode target variable 'Class'
    encode = LabelEncoder().fit(df['Class'])
    df['Class'] = encode.transform(df['Class'])
    
    return df, encode

def split_data(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=2)
    return X_train, X_test, y_train, y_test
