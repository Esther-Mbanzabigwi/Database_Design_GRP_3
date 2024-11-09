# import load model
from keras.models import load_model
import numpy as np
import os

# load model
model = load_model("./Task4/scripts/model.keras")

# load test data
data = np.array([[3, 0, 4, 2, 177, 3, 1, 0, 44, 1233]])
# predict
result = model.predict(data)
print(result)



Warehouse_block,Mode_of_Shipment,Customer_care_calls,Customer_rating,Cost_of_the_Product,Prior_purchases,Product_importance,Gender,Discount_offered,Weight_in_gms