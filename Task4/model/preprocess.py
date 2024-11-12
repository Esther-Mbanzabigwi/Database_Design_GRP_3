import requests
from keras.models import load_model
import numpy as np


# # load model
model = load_model("model.keras")


# Function to fetch the latest data from the API
def fetch_latest_data(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        print("Fetched data:", data)
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


def preprocess_data(customer_data, product_data, order_data, shipment_data):
    # Mapping for categorical variables
    warehouse_block_map = {3: "D", 4: "F", 0: "A", 1: "B", 2: "C"}
    mode_of_shipment_map = {0: "Flight", 2: "Ship", 1: "Road"}
    product_importance_map = {1: "low", 2: "medium", 0: "high"}
    gender_map = {0: "F", 1: "M"}

    # Reverse mappings for encoding
    warehouse_block_reverse_map = {v: k for k, v in warehouse_block_map.items()}
    mode_of_shipment_reverse_map = {v: k for k, v in mode_of_shipment_map.items()}
    product_importance_reverse_map = {v: k for k, v in product_importance_map.items()}
    gender_reverse_map = {"Female": 0, "Male": 1}

    # Extract features and preprocess them in the correct order
    preprocessed_data = [
        # Shipment data
        warehouse_block_reverse_map.get(
            shipment_data["warehouseBlock"], 0
        ),  # Encode warehouse block
        mode_of_shipment_reverse_map.get(
            shipment_data["modeOfShipment"], 0
        ),  # Encode mode of shipment
        shipment_data.get("customerCareCalls", 0),
        shipment_data.get("customerRating", 0),
        # Product data
        product_data.get("cost", 0.0),
        # Customer data
        customer_data.get("priorPurchases", 0),
        product_importance_reverse_map.get(
            product_data["productImportance"].lower(), 1
        ),  # Encode product importance
        gender_reverse_map.get(customer_data["gender"], 0),
        # Order data
        order_data.get("discountOffered", 0.0),
        product_data.get("weightInGms", 0.0),
    ]

    # Return the preprocessed data in the required order
    return preprocessed_data


def make_prediction(preprocessed_data):
    prediction = model.predict(preprocessed_data)
    return prediction


if __name__ == "__main__":
    BASE_URL = "https://databases-assignment-g3.onrender.com"
    CUSTOMER_API_URL = f"{BASE_URL}/customer/latest"
    PRODUCT_API_URL = f"{BASE_URL}/product/latest"
    ORDER_API_URL = f"{BASE_URL}/order/latest"
    SHIPMENT_API_URL = f"{BASE_URL}/shipment/latest"

    customer_data = fetch_latest_data(CUSTOMER_API_URL)
    product_data = fetch_latest_data(PRODUCT_API_URL)
    order_data = fetch_latest_data(ORDER_API_URL)
    shipment_data = fetch_latest_data(SHIPMENT_API_URL)

    if customer_data and product_data and order_data and shipment_data:
        preprocessed_data = preprocess_data(
            customer_data, product_data, order_data, shipment_data
        )
        prediction = make_prediction(np.array([preprocessed_data]))
        prediction = 0 if prediction < 0.5 else 1
        print("Prediction:", prediction)
