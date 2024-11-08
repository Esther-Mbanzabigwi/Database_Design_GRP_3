import requests
import joblib
import numpy as np
import pandas as pd

# Load the saved model and scaler
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

# API endpoint URLs
BASE_URL = "https://databases-assignment-g3.onrender.com"
CUSTOMER_API_URL = f"{BASE_URL}/customers/latest"
PRODUCT_API_URL = f"{BASE_URL}/products/latest"
ORDER_API_URL = f"{BASE_URL}/orders/latest"
SHIPMENT_API_URL = f"{BASE_URL}/shipments/latest"

# Fetch the latest entries from the API
def fetch_latest_data():
    try:
        customer_data = requests.get(CUSTOMER_API_URL).json()
        product_data = requests.get(PRODUCT_API_URL).json()
        order_data = requests.get(ORDER_API_URL).json()
        shipment_data = requests.get(SHIPMENT_API_URL).json()
        
        return customer_data, product_data, order_data, shipment_data
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None, None, None, None

# Prepare data for prediction based on dataset columns
def prepare_data(customer_data, product_data, order_data, shipment_data):
    # Encoding categorical features (get dummies)
    block_encoding = {"A": "warehouseBlock_A", "B": "warehouseBlock_B", "C": "warehouseBlock_C", "D": "warehouseBlock_D", "F": "warehouseBlock_F"}
    mode_encoding = {"Ship": "modeOfShipment_Ship", "Flight": "modeOfShipment_Flight", "Road": "modeOfShipment_Road"}
    importance_encoding = {"low": "productImportance_low", "medium": "productImportance_medium", "high": "productImportance_high"}
    gender_encoding = {"Male": "gender_Male", "Female": "gender_Female"}

    # Create a DataFrame for the input data
    input_data = {
        "warehouseBlock": block_encoding.get(shipment_data.get("warehouseBlock", "A")),
        "modeOfShipment": mode_encoding.get(shipment_data.get("modeOfShipment", "Ship")),
        "customerCareCalls": shipment_data.get("customerCareCalls", 0),
        "customerRating": shipment_data.get("customerRating", 0),
        "costOfTheProduct": product_data.get("cost", 0),
        "priorPurchases": customer_data.get("priorPurchases", 0),
        "productImportance": importance_encoding.get(product_data.get("productImportance", "low")),
        "gender": gender_encoding.get(customer_data.get("gender", "Male")),
        "discountOffered": order_data.get("discountOffered", 0),
        "weightInGms": product_data.get("weightInGms", 0)
    }

    # Convert input data to a DataFrame
    df = pd.DataFrame([input_data])

    # Apply one-hot encoding (get dummies)
    df = pd.get_dummies(df)

    # Ensure the DataFrame has all the required columns (add missing dummy columns as zeros)
    expected_columns = [
        "customerCareCalls", "customerRating", "costOfTheProduct", "priorPurchases",
        "discountOffered", "weightInGms",
        "warehouseBlock_A", "warehouseBlock_B", "warehouseBlock_C", "warehouseBlock_D", "warehouseBlock_F",
        "modeOfShipment_Ship", "modeOfShipment_Flight", "modeOfShipment_Road",
        "productImportance_low", "productImportance_medium", "productImportance_high",
        "gender_Male", "gender_Female"
    ]
    for col in expected_columns:
        if col not in df.columns:
            df[col] = 0

    # Reorder columns to match the expected input format
    df = df[expected_columns]

    # Scale the data using the loaded scaler
    scaled_data = scaler.transform(df)

    return scaled_data

# Make prediction using the model
def make_prediction(data):
    prediction = model.predict(data)
    return prediction[0]

# Main function
if __name__ == "_main_":
    # Fetch data from the live API
    customer_data, product_data, order_data, shipment_data = fetch_latest_data()

    if None in [customer_data, product_data, order_data, shipment_data]:
        print("Failed to fetch data. Please check the API endpoints.")
    else:
        # Prepare input data for prediction
        input_data = prepare_data(customer_data, product_data, order_data, shipment_data)
        
        # Make a prediction
        prediction = make_prediction(input_data)
        
        # Display the prediction result
        print("Predicted Value:", prediction)