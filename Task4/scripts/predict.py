import sys
import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.image import resize

# Add Task4 directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from model.preprocess import preprocess_data  # Importing preprocess_data function

# Load the pre-trained model
model = load_model('Task4/model/simple_model.keras')

def make_prediction(input_data):
    """
    Make a prediction using the pre-trained model.
    
    Parameters:
    input_data (numpy.ndarray): Preprocessed data for the model.
    
    Returns:
    numpy.ndarray: Model's prediction.
    """
    resized_data = resize(input_data, (128, 128))  # Resize to expected model input shape
    resized_data = np.expand_dims(resized_data, axis=0)  # Add batch dimension
    prediction = model.predict(resized_data)
    return prediction

def fetch_dummy_image():
    """
    Generate a dummy image of shape (128, 128, 3).
    
    Returns:
    numpy.ndarray: Dummy image data.
    """
    return np.random.rand(128, 128, 3).astype(np.float32)

if __name__ == "__main__":
    # Fetch a dummy image data
    dummy_image = fetch_dummy_image()
    
    # Make a prediction
    prediction = make_prediction(dummy_image)
    print("Prediction:", prediction)
