"""Assessment B1: train, evaluate, save, reload, and compare predictions."""
from pathlib import Path
import numpy as np
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

ROOT=Path(__file__).resolve().parents[1]
MODEL_PATH=ROOT/"delivery_model.joblib"
def train():
    rng=np.random.default_rng(42)
    n=200
    distance=rng.uniform(0.5, 20, n)
    items=rng.integers(1, 9, n)
    rain=rng.integers(0, 2, n)
    noise=rng.normal(0, 3, n)
    y=18 + 3.1*distance + 1.7*items + 7*rain + noise
    X=np.column_stack([distance,items,rain])
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.2,random_state=42)
    model=LinearRegression().fit(X_train,y_train)
    rmse=float(np.sqrt(mean_squared_error(y_test,model.predict(X_test))))
    print(f"Test RMSE: {rmse:.2f} minutes")
    joblib.dump(model,MODEL_PATH)
    print(f"Saved model: {MODEL_PATH.name} ({MODEL_PATH.stat().st_size/1024:.2f} KB)")
    restored=joblib.load(MODEL_PATH)
    sample=np.array([[4.2,2,0]])
    original=float(model.predict(sample)[0]); loaded=float(restored.predict(sample)[0])
    passed=bool(np.isclose(original,loaded,rtol=0,atol=1e-12))
    print(f"Prediction original={original:.6f}; reloaded={loaded:.6f}; {'PASS' if passed else 'FAIL'}")
    assert passed
    return model
if __name__=="__main__": train()
