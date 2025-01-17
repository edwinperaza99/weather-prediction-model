import logging

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from utils import load_models, make_predictions

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, restrict this to specific URLs later
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("weather_app.log"),  # Log to a file
        logging.StreamHandler(),  # Log to the console
    ],
)


# Define a model for the input data
class PredictionRequest(BaseModel):
    year: int
    latitude: float
    longitude: float
    month: int


# Load models on startup
logging.info("Loading models...")
try:
    MODELS = load_models()
    logging.info("Models loaded successfully.")
except FileNotFoundError as e:
    logging.error(f"Error loading models: {e}")
    MODELS = {}


@app.post("/predict")
async def predict(request: PredictionRequest):
    """
    Predicts weather data based on the input features using various machine learning models.

    This endpoint accepts the year, latitude, longitude, and month as inputs and generates predictions
    using multiple models like KNN, Random Forest, and Linear Regression.

    **Request Body Example:**
    ```json
    {
      "year": 2025,
      "latitude": 37.7749,
      "longitude": -122.4194,
      "month": 5
    }
    ```

    **Response Example:**
    ```json
    {
      "predictions": [
        {
          "model": "KNN M1",
          "prediction": 22.5
        },
        {
          "model": "Random Forest M1",
          "prediction": 21.8
        },
        {
          "model": "Linear Regression M1",
          "prediction": 23.1
        }
      ]
    }
    ```

    - **year**: The year for prediction (e.g., 2025).
    - **latitude**: The latitude of the location (e.g., 37.7749).
    - **longitude**: The longitude of the location (e.g., -122.4194).
    - **month**: The month of the year (1-12) for which the prediction is to be made (e.g., 5).

    Responses:
        - 200: Predictions successfully generated for all models.
        - 400: Missing or invalid input parameters.
        - 500: Internal server error during prediction.
    """
    try:
        # Prepare features as a list
        features = [request.year, request.latitude, request.longitude, request.month]

        # Make predictions using all models
        raw_predictions = make_predictions(MODELS, features)

        # Format predictions
        formatted_predictions = [
            {
                "model": model_name,
                "prediction": value if value is not None else "Error: Model failed",
            }
            for model_name, value in raw_predictions.items()
        ]

        logging.info(f"Predictions generated for input {features}: {formatted_predictions}")
        return {"predictions": formatted_predictions}

    except Exception as e:
        logging.error(f"Error during prediction: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
