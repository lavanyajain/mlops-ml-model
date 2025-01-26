import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error  # Ensure this line is included

# Correct path and delimiter might need to be specified
data = pd.read_csv('data.csv')
print(data.columns)  # check actual column names

# Assume 'house_price' is the target, and it exists as per the print statement
X = data.drop('house_price', axis=1)
y = data['house_price']

# Example continuation: splitting data for training/testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define model
model = RandomForestRegressor(random_state=42)

# Setup hyperparameter grid
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10]
}

# Setup GridSearchCV
grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, scoring='neg_mean_squared_error', verbose=1)
grid_search.fit(X_train, y_train)

# Best model
best_model = grid_search.best_estimator_

# Predict and evaluate
predictions = best_model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
print(f"Best Parameters: {grid_search.best_params_}")
print(f"Test MSE: {mse}")

import joblib
joblib.dump(best_model, 'best_model.pkl')

