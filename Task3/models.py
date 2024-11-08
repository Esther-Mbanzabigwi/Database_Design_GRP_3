from pydantic import BaseModel
from typing import Optional

# Customer model
class Customer(BaseModel):
    #_id: str
    gender: str
    priorPurchases: int

# Product model
class Product(BaseModel):
    #_id: str
    cost: float
    productImportance: str
    weightInGms: float

# Order model
class Order(BaseModel):
    #_id: str
    customerId: str
    orderDate: str
    discountOffered: float
    productId: str

# Shipment model
class Shipment(BaseModel):
    #_id: str
    orderId: str
    warehouseBlock: str
    modeOfShipment: str
    customerCareCalls: int
    customerRating: int
    reachedOnTime: int
