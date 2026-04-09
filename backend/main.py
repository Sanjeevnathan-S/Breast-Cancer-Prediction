from fastapi import FastAPI, HTTPException
import pickle
import numpy as np

app = FastAPI(title="Breast Cancer Prediction API")

# Load artifacts
with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)

with open("model/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("model/selected_features.pkl", "rb") as f:
    selected_features = pickle.load(f)


@app.get("/")
def home():
    return {"message": "Breast Cancer Prediction API Running"}


@app.post("/predict")
def predict(data: dict):
    try:
      
        missing = [f for f in selected_features if f not in data]
        if missing:
            raise HTTPException(
                status_code=400,
                detail=f"Missing features: {missing}"
            )

      
        input_data = [data[feature] for feature in selected_features]

        input_array = np.array([input_data])

   
        input_scaled = scaler.transform(input_array)

        prediction = model.predict(input_scaled)[0]

        
        confidence = float(np.max(model.predict_proba(input_scaled)))

        result = "Malignant" if prediction == 1 else "Benign"

        return {
            "prediction": result,
            "confidence": confidence
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    