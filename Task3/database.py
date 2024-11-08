from pymongo import MongoClient

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["shipping_data"]

# Collections
customers_collection = db["Customers"]
products_collection = db["Products"]
orders_collection = db["Orders"]
shipments_collection = db["Shipments"]
