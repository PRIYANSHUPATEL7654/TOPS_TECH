"""
CORRECTED version — fixed by hand, without AI assistance (Step 2).

Fixes applied vs. ai_original_code.py:
  1. Output layer activation changed from `sigmoid` -> `softmax`, so the three
     class probabilities are mutually exclusive and sum to 1.
  2. Loss function changed from `mean_squared_error` -> `categorical_crossentropy`,
     the correct loss for one-hot-encoded multi-class classification.

Everything else (data generation, layer sizes, epochs, plotting, save/reload)
is unchanged from the AI's original structure.
"""

import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical

# --- Synthetic dataset (identical to original) -----------------------------
np.random.seed(1)
n = 500
order_value = np.random.uniform(50, 1000, n)
distance_km = np.random.uniform(1, 30, n)
prep_time_min = np.random.uniform(5, 45, n)

priority = []
for v, d, p in zip(order_value, distance_km, prep_time_min):
    score = v / 200 + d / 10 + p / 15
    if score < 5:
        priority.append(0)
    elif score < 8:
        priority.append(1)
    else:
        priority.append(2)
priority = np.array(priority)

X = np.column_stack([order_value, distance_km, prep_time_min])
y = to_categorical(priority, num_classes=3)

split = int(0.8 * n)
X_train, X_val = X[:split], X[split:]
y_train, y_val = y[:split], y[split:]

# --- Model (FIXED) ---------------------------------------------------------
model = Sequential([
    Dense(32, activation="relu", input_shape=(3,)),
    Dense(16, activation="relu"),
    Dense(3, activation="softmax"),   # FIXED: softmax for mutually-exclusive classes
])

model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",   # FIXED: correct loss for classification
    metrics=["accuracy"],
)

history = model.fit(
    X_train, y_train,
    validation_data=(X_val, y_val),
    epochs=20,
    verbose=1,
)

# --- Plot loss curves ------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
axes[0].plot(history.history["loss"])
axes[0].set_title("Training Loss")
axes[0].set_xlabel("Epoch")
axes[0].set_ylabel("Loss")

axes[1].plot(history.history["val_loss"])
axes[1].set_title("Validation Loss")
axes[1].set_xlabel("Epoch")
axes[1].set_ylabel("Loss")

plt.tight_layout()
plt.savefig("corrected_loss_curves.png")

# --- Save, reload, predict --------------------------------------------------
model.save("food_priority_model.keras")
reloaded = load_model("food_priority_model.keras")

sample = np.array([[500, 10, 20]])
prediction = reloaded.predict(sample)
print("Predicted priority probabilities:", prediction, "sum =", prediction.sum())
print("Predicted class:", np.argmax(prediction))
