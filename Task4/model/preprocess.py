import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Initialize scaler and encoder
scaler = StandardScaler()
encoder = OneHotEncoder(handle_unknown="ignore")

# Specify which columns are numerical and which are categorical
numerical_features = ["feature1", "feature2"]  # Replace with actual numerical feature names
categorical_features = ["feature3"]  # Replace with actual categorical feature names

# Define a preprocessing pipeline for numerical and categorical features
preprocessor = ColumnTransformer(
    transformers=[
        ("num", scaler, numerical_features),
        ("cat", encoder, categorical_features)
    ]
)

def preprocess_data(data):
    """
    Preprocess incoming data to match the model's input requirements.
    
    Parameters:
    data (dict): The data to preprocess (this could come from the API in the future).
    
    Returns:
    numpy.ndarray: Preprocessed data ready for model prediction.
    """
    # Convert data to DataFrame
    df = pd.DataFrame([data])
    
    # Check for missing values and fill them (e.g., with median for numerical, "unknown" for categorical)
    for col in numerical_features:
        if df[col].isnull().any():
            df[col].fillna(df[col].median(), inplace=True)
    
    for col in categorical_features:
        if df[col].isnull().any():
            df[col].fillna("unknown", inplace=True)
    
    # Apply transformations using the preprocessing pipeline
    df_preprocessed = preprocessor.fit_transform(df)  # Use transform only if pipeline has been pre-fitted
    
    return df_preprocessed
if __name__ == "__main__":
    # Sample dummy data that matches the model's expected input format
    dummy_data = {
    "feature1": 2.0,
    "feature2": 5.3,
    "feature3": 1.5  # Add 'feature3' if the model expects it
}

    
    # Test preprocessing
    preprocessed_data = preprocess_data(dummy_data)
    print("Preprocessed Data:", preprocessed_data)

