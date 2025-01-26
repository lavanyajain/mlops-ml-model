"""
This module defines a simple machine learning model.
"""

from sklearn.linear_model import LinearRegression
import numpy as np

def train_model():
    """
    Trains a linear regression model and returns the trained model.
    """
    x = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
    y = np.dot(x, np.array([1, 2])) + 3
    trained_model = LinearRegression().fit(x, y)  # Renamed to avoid name conflict with outer scope
    return trained_model

def predict(trained_model, input_data):
    """
    Makes predictions using the trained model for the given input data.
    """
    predictions = trained_model.predict(input_data)
    return predictions

if __name__ == "__main__":
    model_instance = train_model()  # Renamed to avoid name conflict
    predictions = predict(model_instance, np.array([[3, 5]]))
    print("Predictions:", predictions)
