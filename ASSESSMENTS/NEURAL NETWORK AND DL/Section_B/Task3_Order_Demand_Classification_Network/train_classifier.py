"""
Task 3 — Order Demand Classification Network
Section B, Module 9 (Neural Networks & Deep Learning)

Trains a Keras ANN to classify food-delivery demand into Low / Medium / High
from hour_of_day, day_of_week, and temperature_celsius.

Run with:
    python train_classifier.py

Outputs:
    demand_model.keras          - trained model (also used by Task 4 / Capstone)
    training_history.png        - accuracy curve (training vs validation)
    training_output.txt         - captured console log / final test accuracy
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Input
from tensorflow.keras.utils import to_categorical

# ---------------------------------------------------------------------------
# Requirement 1 — Synthetic dataset (>=500 samples, 3 numeric features, 3 classes)
# ---------------------------------------------------------------------------
rng = np.random.default_rng(7)
N = 1500

hour_of_day = rng.integers(0, 24, N)
day_of_week = rng.integers(0, 7, N)
temperature_celsius = rng.uniform(10, 45, N)


def demand_label(hour, dow, temp):
    """Heuristic ground-truth generator: peak lunch/dinner hours + weekends +
    moderate temps push demand higher, with a bit of noise for realism."""
    score = 0.0
    if hour in (12, 13, 19, 20, 21):
        score += 2.0
    elif hour in (11, 14, 18, 22):
        score += 1.0
    if dow in (5, 6):  # weekend
        score += 1.0
    if 18 <= temp <= 30:
        score += 0.5
    score += rng.normal(0, 0.7)
    if score >= 2.3:
        return 2  # High
    elif score >= 1.0:
        return 1  # Medium
    return 0  # Low


labels = np.array(
    [demand_label(h, d, t) for h, d, t in zip(hour_of_day, day_of_week, temperature_celsius)]
)

X = np.column_stack([hour_of_day, day_of_week, temperature_celsius]).astype("float32")
# simple feature scaling
X_scaled = X.copy()
X_scaled[:, 0] /= 23.0
X_scaled[:, 1] /= 6.0
X_scaled[:, 2] = (X_scaled[:, 2] - 10) / (45 - 10)

y_cat = to_categorical(labels, num_classes=3)

X_train_full, X_test, y_train_full, y_test = train_test_split(
    X_scaled, y_cat, test_size=0.15, random_state=42, stratify=labels
)

# ---------------------------------------------------------------------------
# Requirement 2 — Sequential model: Dense(64) -> Dropout(0.3) -> Dense(32) ->
# Dropout(0.3) -> Dense(3, softmax)
# ---------------------------------------------------------------------------
model = Sequential(
    [
        Input(shape=(3,)),
        Dense(64, activation="relu"),
        Dropout(0.3),
        Dense(32, activation="relu"),
        Dropout(0.3),
        Dense(3, activation="softmax"),
    ]
)

# ---------------------------------------------------------------------------
# Requirement 3 — Compile & train (30 epochs, 0.2 validation split)
# ---------------------------------------------------------------------------
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

history = model.fit(
    X_train_full,
    y_train_full,
    epochs=30,
    validation_split=0.2,
    batch_size=32,
    verbose=2,
)

# ---------------------------------------------------------------------------
# Requirement 4 — Evaluate on held-out test set + plot accuracy curves
# ---------------------------------------------------------------------------
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)
log_lines = [f"Final test accuracy: {test_acc:.4f}", f"Final test loss: {test_loss:.4f}"]
print("\n".join(log_lines))

with open("training_output.txt", "w") as f:
    f.write("Order Demand Classification Network — Training Summary\n")
    f.write("=" * 55 + "\n")
    f.write(f"Train samples: {len(X_train_full)} | Test samples: {len(X_test)}\n\n")
    f.write("\n".join(log_lines) + "\n")

plt.figure(figsize=(8, 5))
plt.plot(history.history["accuracy"], label="Training Accuracy")
plt.plot(history.history["val_accuracy"], label="Validation Accuracy")
plt.title("Order Demand Classifier — Training vs Validation Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("training_history.png", dpi=150)
print("Saved training_history.png")

model.save("demand_model.keras")
print("Saved demand_model.keras")

import json

with open("training_history.json", "w") as f:
    json.dump(
        {
            "accuracy": [float(v) for v in history.history["accuracy"]],
            "val_accuracy": [float(v) for v in history.history["val_accuracy"]],
            "loss": [float(v) for v in history.history["loss"]],
            "val_loss": [float(v) for v in history.history["val_loss"]],
            "test_accuracy": float(test_acc),
            "test_loss": float(test_loss),
        },
        f,
        indent=2,
    )
print("Saved training_history.json")
