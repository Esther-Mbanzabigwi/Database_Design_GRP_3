from fastapi import FastAPI, HTTPException
from models import Customer, Product, Order, Shipment
from database import customers_collection, products_collection, orders_collection, shipments_collection
from bson import ObjectId

app = FastAPI()

# Helper function to serialize MongoDB document
def serialize_doc(doc):
    doc['_id'] = str(doc['_id'])
    return doc

# CRUD for Customers
@app.post("/create_customer/")
async def create_customer(customer: Customer):
    customer_dict = customer.dict()
    if "_id" not in customer_dict:
        customer_dict["_id"] = str(ObjectId())  # Generate a new ObjectId if not provided
    else:
        customer_dict["_id"] = str(customer_dict["_id"])  # Ensure _id is a string
    result = customers_collection.insert_one(customer_dict)
    return {"inserted_id": str(result.inserted_id)}

@app.get("/customers/{customer_id}")
async def read_customer(customer_id: str):
    customer = customers_collection.find_one({"_id": customer_id})
    if customer:
        return serialize_doc(customer)
    raise HTTPException(status_code=404, detail="Customer not found")

@app.put("/customers/{customer_id}")
async def update_customer(customer_id: str, customer: Customer):
    result = customers_collection.update_one({"_id": customer_id}, {"$set": customer.dict()})
    if result.modified_count:
        return {"message": "Customer updated successfully"}
    raise HTTPException(status_code=404, detail="Customer not found")

@app.delete("/customers/{customer_id}")
async def delete_customer(customer_id: str):
    result = customers_collection.delete_one({"_id": customer_id})
    if result.deleted_count:
        return {"message": "Customer deleted successfully"}
    raise HTTPException(status_code=404, detail="Customer not found")

# CRUD for Products
@app.post("/products/")
async def create_product(product: Product):
    result = products_collection.insert_one(product.dict())
    return {"inserted_id": str(result.inserted_id)}

@app.get("/products/{product_id}")
async def read_product(product_id: str):
    product = products_collection.find_one({"_id": product_id})
    if product:
        return serialize_doc(product)
    raise HTTPException(status_code=404, detail="Product not found")

@app.put("/products/{product_id}")
async def update_product(product_id: str, product: Product):
    result = products_collection.update_one({"_id": product_id}, {"$set": product.dict()})
    if result.modified_count:
        return {"message": "Product updated successfully"}
    raise HTTPException(status_code=404, detail="Product not found")

@app.delete("/products/{product_id}")
async def delete_product(product_id: str):
    result = products_collection.delete_one({"_id": product_id})
    if result.deleted_count:
        return {"message": "Product deleted successfully"}
    raise HTTPException(status_code=404, detail="Product not found")

# CRUD for Orders
@app.post("/orders/")
async def create_order(order: Order):
    result = orders_collection.insert_one(order.dict())
    return {"inserted_id": str(result.inserted_id)}

@app.get("/orders/{order_id}")
async def read_order(order_id: str):
    order = orders_collection.find_one({"_id": order_id})
    if order:
        return serialize_doc(order)
    raise HTTPException(status_code=404, detail="Order not found")

@app.put("/orders/{order_id}")
async def update_order(order_id: str, order: Order):
    result = orders_collection.update_one({"_id": order_id}, {"$set": order.dict()})
    if result.modified_count:
        return {"message": "Order updated successfully"}
    raise HTTPException(status_code=404, detail="Order not found")

@app.delete("/orders/{order_id}")
async def delete_order(order_id: str):
    result = orders_collection.delete_one({"_id": order_id})
    if result.deleted_count:
        return {"message": "Order deleted successfully"}
    raise HTTPException(status_code=404, detail="Order not found")

# CRUD for Shipments
@app.post("/shipments/")
async def create_shipment(shipment: Shipment):
    result = shipments_collection.insert_one(shipment.dict())
    return {"inserted_id": str(result.inserted_id)}

@app.get("/shipments/{shipment_id}")
async def read_shipment(shipment_id: str):
    shipment = shipments_collection.find_one({"_id": shipment_id})
    if shipment:
        return serialize_doc(shipment)
    raise HTTPException(status_code=404, detail="Shipment not found")

@app.put("/shipments/{shipment_id}")
async def update_shipment(shipment_id: str, shipment: Shipment):
    result = shipments_collection.update_one({"_id": shipment_id}, {"$set": shipment.dict()})
    if result.modified_count:
        return {"message": "Shipment updated successfully"}
    raise HTTPException(status_code=404, detail="Shipment not found")

@app.delete("/shipments/{shipment_id}")
async def delete_shipment(shipment_id: str):
    result = shipments_collection.delete_one({"_id": shipment_id})
    if result.deleted_count:
        return {"message": "Shipment deleted successfully"}
    raise HTTPException(status_code=404, detail="Shipment not found")
