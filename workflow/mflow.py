import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import mlflow
import mlflow.sklearn

# Ensure the MLflow tracking URI is set
mlflow.set_tracking_uri('http://localhost:5000')

data = pd.read_csv('data.csv')
X = data.drop('house_price', axis=1)
y = data['house_price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

for n_est in [10, 50, 100]:
    with mlflow.start_run():
        model = RandomForestRegressor(n_estimators=n_est, random_state=42)
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)

        # Log model with signature and input example
        signature = mlflow.models.infer_signature(X_train, model.predict(X_train))
        input_example = X_train.head(1)

        mlflow.sklearn.log_model(model, "model", signature=signature, input_example=input_example)
        mlflow.log_param("n_estimators", n_est)
        mlflow.log_metric("mse", mse)

        print(f"Run with n_estimators={n_est}, MSE={mse}")
