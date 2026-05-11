import { useState } from "react";
import axios from "axios";
import { FaHeartbeat, FaUserAlt, FaTint } from "react-icons/fa";

function App() {
  const [formData, setFormData] = useState({
    age: "",
    bp: "",
    sugar: "",
  });

  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handlePredict = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      // Replace with your backend URL
      const response = await axios.post(
        "/predict",
        {
          age: Number(formData.age),
          bp: Number(formData.bp),
          sugar: Number(formData.sugar),
        }
      );

      setPrediction(response.data.prediction);
    } catch (error) {
      console.error(error);
      alert("Prediction failed. Check backend connection.");
    }

    setLoading(false);
  };

  return (
    <div className="container">
      <div className="glass-card">
        <div className="left-panel">
          <h1>
            <FaHeartbeat className="heart-icon" />
            Disease Predictor
          </h1>

          <p className="subtitle">
            Predict disease possibility using Machine Learning.
          </p>

          <form onSubmit={handlePredict}>
            <div className="input-box">
              <FaUserAlt />
              <input
                type="number"
                name="age"
                placeholder="Enter Age"
                value={formData.age}
                onChange={handleChange}
                required
              />
            </div>

            <div className="input-box">
              <FaHeartbeat />
              <input
                type="number"
                name="bp"
                placeholder="Blood Pressure"
                value={formData.bp}
                onChange={handleChange}
                required
              />
            </div>

            <div className="input-box">
              <FaTint />
              <input
                type="number"
                name="sugar"
                placeholder="Sugar Level"
                value={formData.sugar}
                onChange={handleChange}
                required
              />
            </div>

            <button type="submit" className="predict-btn">
              {loading ? "Predicting..." : "Predict Disease"}
            </button>
          </form>
        </div>

        <div className="right-panel">
          <div className="result-card">
            <h2>Prediction Result</h2>

            {prediction === null ? (
              <p className="waiting-text">
                Enter details to get prediction.
              </p>
            ) : prediction === 1 ? (
              <div className="danger">
                Disease Detected
              </div>
            ) : (
              <div className="safe">
                No Disease Detected
              </div>
            )}
          </div>

          <div className="info-box">
            <h3>Model Inputs</h3>
            <ul>
              <li>Age</li>
              <li>Blood Pressure</li>
              <li>Sugar Level</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;