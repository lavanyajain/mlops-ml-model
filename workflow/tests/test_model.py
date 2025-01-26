# Tests for our simple machine learning model

from model.model import train_model, predict
import numpy as np

def test_model_predictions():
    model = train_model()
    predictions = predict(model, np.array([[3, 5]]))
    expected = np.array([16.])
    assert np.allclose(predictions, expected), "Test failed: Predictions do not match expected values"
