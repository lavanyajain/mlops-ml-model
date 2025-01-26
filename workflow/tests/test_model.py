import numpy as np
from model.model import train_model, predict

def test_model_predictions():
    model = train_model()
    predictions = predict(model, np.array([[3, 5]]))
    expected = np.array([16.])  # Assuming 'expected' is defined somewhere else correctly
    assert np.allclose(predictions, expected), "Predictions do not match expected values"
