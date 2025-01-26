# A simple machine learning script that uses linear regression to make predictions

from sklearn.linear_model import LinearRegression
import numpy as np

def train_model():
    x = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
    y = np.dot(x, np.array([1, 2])) + 3
    model = LinearRegression().fit(x, y)
    return model

def predict(model, x):
    return model.predict(x)

if __name__ == "__main__":
    model = train_model()
    predictions = predict(model, np.array([[3, 5]]))
    print("Predictions:", predictions)
