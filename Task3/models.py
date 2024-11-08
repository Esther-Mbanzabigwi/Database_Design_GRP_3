from pydantic import BaseModel
from typing import Optional

# Customer model
class Customer(BaseModel):
    gender: str
    priorPurchases: int

# Product model
class Product(BaseModel):
    cost: float
    productImportance: str
    weightInGms: float

# Order model
class Order(BaseModel):
    discountOffered: float

# Shipment model
class Shipment(BaseModel):
    warehouseBlock: str
    modeOfShipment: str
    customerCareCalls: int
    customerRating: int
