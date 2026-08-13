"""
Trains a simple scikit-learn regression model that predicts delivery time
(minutes) from distance (km), order value (Rs), and time-of-day (encoded 0-3).
Saves the fitted model as delivery_model.pkl, which app.py loads at runtime.

Run once before launching app.py:
    python train_model.py
"""

import joblib
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

rng = np.random.default_rng(42)
n = 800

distance_km = rng.uniform(1, 50, n)
order_value = rng.uniform(100, 2000, n)
time_of_day = rng.integers(0, 4, n)  # 0=Morning, 1=Afternoon, 2=Evening, 3=Night

# Synthetic ground truth: base time + distance effect + rush-hour penalty + noise
rush_hour_penalty = np.select(
    [time_of_day == 0, time_of_day == 1, time_of_day == 2, time_of_day == 3],
    [2, 8, 12, 4],
)
delivery_time = (
    15
    + distance_km * 1.3
    + rush_hour_penalty
    + rng.normal(0, 3, n)
)

X = np.column_stack([distance_km, order_value, time_of_day])
y = delivery_time

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

score = model.score(X_test, y_test)
print(f"Model trained. R^2 on held-out test set: {score:.3f}")

joblib.dump(model, "delivery_model.pkl")
print("Saved model to delivery_model.pkl")
