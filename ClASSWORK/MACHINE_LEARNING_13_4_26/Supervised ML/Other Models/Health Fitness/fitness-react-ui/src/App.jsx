import React, { useState } from "react";
import "./App.css";

function App() {
  const [formData, setFormData] = useState({
    exercise_minutes: "",
    steps: "",
    food_calories: "",
    sleep_hours: "",
    water_intake_liters: "",
  });

  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    setLoading(true);

    try {
      // Replace with your backend API URL
      const response = await fetch("/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          exercise_minutes: Number(formData.exercise_minutes),
          steps: Number(formData.steps),
          food_calories: Number(formData.food_calories),
          sleep_hours: Number(formData.sleep_hours),
          water_intake_liters: Number(formData.water_intake_liters),
        }),
      });

      const data = await response.json();

      setPrediction(data.predicted_weight);
    } catch (error) {
      console.error(error);
      alert("Prediction failed!");
    }

    setLoading(false);
  };

  return (
    <div className="container">
      <div className="glass-card">
        <div className="header">
          <h1>Health & Fitness Predictor</h1>
          <p>
            Predict your estimated weight using your daily health activity data
          </p>
        </div>

        <form onSubmit={handleSubmit}>
          <div className="grid">
            <div className="input-group">
              <label>Exercise Minutes</label>
              <input
                type="number"
                name="exercise_minutes"
                value={formData.exercise_minutes}
                onChange={handleChange}
                placeholder="e.g. 45"
                required
              />
            </div>

            <div className="input-group">
              <label>Steps</label>
              <input
                type="number"
                name="steps"
                value={formData.steps}
                onChange={handleChange}
                placeholder="e.g. 8000"
                required
              />
            </div>

            <div className="input-group">
              <label>Food Calories</label>
              <input
                type="number"
                name="food_calories"
                value={formData.food_calories}
                onChange={handleChange}
                placeholder="e.g. 2200"
                required
              />
            </div>

            <div className="input-group">
              <label>Sleep Hours</label>
              <input
                type="number"
                step="0.1"
                name="sleep_hours"
                value={formData.sleep_hours}
                onChange={handleChange}
                placeholder="e.g. 7.5"
                required
              />
            </div>

            <div className="input-group">
              <label>Water Intake (Liters)</label>
              <input
                type="number"
                step="0.1"
                name="water_intake_liters"
                value={formData.water_intake_liters}
                onChange={handleChange}
                placeholder="e.g. 3"
                required
              />
            </div>
          </div>

          <button type="submit" className="predict-btn">
            {loading ? "Predicting..." : "Predict Weight"}
          </button>
        </form>

        {prediction !== null && (
          <div className="result-card">
            <h2>Predicted Weight</h2>
            <div className="prediction">{prediction.toFixed(2)} kg</div>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
