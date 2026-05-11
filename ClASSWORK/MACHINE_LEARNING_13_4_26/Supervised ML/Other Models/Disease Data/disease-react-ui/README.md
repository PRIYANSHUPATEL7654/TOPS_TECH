# Disease Prediction React UI

## Install
npm install

## Run
npm run dev

## Backend API Expected
POST http://127.0.0.1:8000/predict

JSON Body:
{
  "age": 30,
  "bp": 120,
  "sugar": 180
}

Expected Response:
{
  "prediction": 1
}