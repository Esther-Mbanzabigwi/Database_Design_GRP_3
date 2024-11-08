import requests
import pickle
import pandas as pd
import numpy as np

# Load the scaler and model from pickle files
with open("scaler.pkl", "rb") as scaler_file:
    scaler = pickle.load(scaler_file)

with open("model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Function to fetch the latest data from the API
def fetch_latest_data(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        print("Fetched data:", data)  # Print the raw data for inspection
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

# Preprocess the data for prediction
def prepare_data_for_prediction(raw_data):
    # Convert raw data to DataFrame
    df = pd.DataFrame([raw_data])

    # Map categorical variables to numerical values
    df['Warehouse_block'] = df['Warehouse_block'].map({'A': 0, 'B': 1, 'C': 2, 'D': 3, 'F': 4})
    df['Mode_of_Shipment'] = df['Mode_of_Shipment'].map({'Flight': 0, 'Ship': 1, 'Road': 2})
    df['Product_importance'] = df['Product_importance'].map({'low': 0, 'medium': 1, 'high': 2})
    df['Gender'] = df['Gender'].map({'M': 0, 'F': 1})

    # Define the expected columns and fill missing ones with a default value (e.g., 0)
    expected_columns = ['Warehouse_block', 'Mode_of_Shipment', 'Customer_care_calls', 
                        'Customer_rating', 'Cost_of_the_Product', 'Prior_purchases', 
                        'Product_importance', 'Gender', 'Discount_offered', 'Weight_in_gms']
    df = df.reindex(columns=expected_columns, fill_value=0)

    # Scale the data
    scaled_data = scaler.transform(df)
    return scaled_data

# Make prediction
def make_prediction(preprocessed_data):
    prediction = model.predict(preprocessed_data)
    return prediction

# Main script
if __name__ == "__main__":
    api_url = 'https://databases-assignment-g3.onrender.com/customers/672e5ce9e093adcf1fdf5a34'
    raw_data = fetch_latest_data(api_url)

    if raw_data:
        try:
            preprocessed_data = prepare_data_for_prediction(raw_data)
            prediction = make_prediction(preprocessed_data)
            print(f"Prediction: {prediction[0]}")
        except Exception as e:
            print(f"Error during prediction: {e}")
    else:
        print("No data to process.")
