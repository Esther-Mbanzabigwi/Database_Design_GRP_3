import pandas as pd
from pymongo import MongoClient


# Loading the dataset
data = '/dataset/shipping_dataset.csv'
dataset = pd.read_csv(data)
print(dataset)

# Connecting to MongoDB
client = MongoClient("mongodb://atlas-sql-672bcdc5aee49224a042282e-chn0e.a.query.mongodb.net/shipping_dataset?ssl=true&authSource=admin")
db = client["shipping_dataset"] 

customers_collection = db["Customers"]
products_collection = db["Products"]
orders_collection = db["Orders"]
shipments_collection = db["Shipments"]


# Preparing the documents for the collections using for loop
for _, row in dataset.iterrows():

  customers_doc = {
     "_id": row['CustomerID'],
    "gender": row['Gender'],
    "priorPurchases": row['PriorPurchases'] 
  }

  products_doc = {
    "_id": row['ProductID'],
    "cost": row['Cost'],
    "productImportance": row['ProductImportance'],
    "weightInGms": row['WeightInGms']
  }

  orders_doc = {
    "_id": row['OrderID'],
    "customerId": row['CustomerID'], 
    "orderDate": row['OrderDate'],
    "discountOffered": row['DiscountOffered'],
    "productId": row['ProductID']
    }

  shipments_doc = {
    "_id": row['ShipmentID'],
    "orderId": row['OrderID'], 
    "warehouseBlock": row['WarehouseBlock'],
    "modeOfShipment": row['ModeOfShipment'],
    "customerCareCalls": row['CustomerCareCalls'],
    "customerRating": row['CustomerRating'],
    "reachedOnTime": row['ReachedOnTime']
  }

  # Inserting the documents into the collections
  customers_collection.insert_one(customers_doc)
  products_collection.insert_one(products_doc)
  orders_collection.insert_one(orders_doc)
  shipments_collection.insert_one(shipments_doc)
