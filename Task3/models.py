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
    customerId: str
    orderDate: str
    discountOffered: float
    productId: str

# Shipment model
class Shipment(BaseModel):
    orderId: str
    warehouseBlock: str
    modeOfShipment: str
    customerCareCalls: int
    customerRating: int
    reachedOnTime: int
