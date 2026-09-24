"""Assessment B2: Flask prediction service. Model is loaded once at startup."""
from pathlib import Path
import joblib
import numpy as np
from flask import Flask, jsonify, request
ROOT=Path(__file__).resolve().parents[1]
MODEL_PATH=ROOT/"delivery_model.joblib"
if not MODEL_PATH.exists():
    raise FileNotFoundError(f"{MODEL_PATH} is missing. Run `python -m quickbite.train_model` first.")
MODEL=joblib.load(MODEL_PATH)
app=Flask(__name__)
REQUIRED=("distance_km","num_items","rain_flag")
@app.get("/health")
def health(): return jsonify({"status":"ok","model_loaded":True}),200
@app.post("/predict")
def predict():
    body=request.get_json(silent=True)
    if not isinstance(body,dict): return jsonify({"error":"Request body must be a JSON object."}),400
    missing=[field for field in REQUIRED if field not in body]
    if missing: return jsonify({"error":"Missing required field(s).","missing_fields":missing}),400
    try:
        distance=float(body["distance_km"]); items=float(body["num_items"]); rain=float(body["rain_flag"])
        if not np.isfinite([distance,items,rain]).all() or distance<0 or items<1 or rain not in (0,1): raise ValueError
    except (TypeError,ValueError):
        return jsonify({"error":"distance_km must be >= 0, num_items must be >= 1, and rain_flag must be 0 or 1."}),400
    estimate=float(MODEL.predict([[distance,items,rain]])[0])
    return jsonify({"predicted_delivery_time_min":round(max(estimate,1.0),1)}),200
if __name__=="__main__": app.run(host="127.0.0.1",port=5000,debug=False)
