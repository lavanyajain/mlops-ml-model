# Tests for our simple machine learning model

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'model')))

from model import train_model, predict
def test_model_predictions():
    model = train_model()
    predictions = predict(model, np.array([[3, 5]]))
    expected = np.array([16.])
    assert np.allclose(predictions, expected), "Test failed: Predictions do not match expected values"
