import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import mlflow
import mlflow.sklearn

# Ensure the MLflow tracking URI is set
mlflow.set_tracking_uri('http://localhost:5000')

# Load data
data = pd.read_csv('data.csv')
X = data.drop('house_price', axis=1)
y = data['house_price']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Parameters to try
n_estimators_options = [10, 50, 100]
max_depth_options = [None, 10, 20]

# Run experiments
for n_estimators in n_estimators_options:
    for max_depth in max_depth_options:
        with mlflow.start_run():
            model = RandomForestRegressor(n_estimators=n_estimators, max_depth=max_depth, random_state=42)
            model.fit(X_train, y_train)
            predictions = model.predict(X_test)
            mse = mean_squared_error(y_test, predictions)

            # Log parameters, metrics, and model
            mlflow.log_params({"n_estimators": n_estimators, "max_depth": max_depth})
            mlflow.log_metric("mse", mse)
            signature = mlflow.models.infer_signature(X_train, predictions)
            input_example = X_train.head(1)
            mlflow.sklearn.log_model(model, "model", signature=signature, input_example=input_example)

            print(f"Run: n_estimators={n_estimators}, max_depth={max_depth}, MSE={mse}")
