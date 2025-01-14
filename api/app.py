from flasgger import Swagger
from flask import Flask, jsonify, request

# from flask_cors import CORS
from utils import load_models, make_predictions

app = Flask(__name__)
# NOTE: probably won't need CORS if hosting from same EC2 instance
# CORS(app)
Swagger(app)

# Load models on startup
MODELS = load_models()


@app.route("/predict", methods=["POST"])
def predict():
    """
    Make predictions using all models.
    ---
    parameters:
      - name: year
        in: formData
        type: integer
        required: true
        description: Year for prediction (e.g., 2025)
      - name: latitude
        in: formData
        type: number
        required: true
        description: Latitude of the location (e.g., 37.7749)
      - name: longitude
        in: formData
        type: number
        required: true
        description: Longitude of the location (e.g., -122.4194)
      - name: month
        in: formData
        type: integer
        required: true
        description: Month of the year (1-12) (e.g., 5)
    responses:
      200:
        description: Predictions for all models
        schema:
          type: object
          properties:
            predictions:
              type: array
              items:
                type: object
                properties:
                  model:
                    type: string
                    description: The name of the model
                  prediction:
                    type: number
                    description: The predicted value
    """
    try:
        # Extract features from the request
        year = request.form.get("year", type=int)
        latitude = request.form.get("latitude", type=float)
        longitude = request.form.get("longitude", type=float)
        month = request.form.get("month", type=int)

        # Validate inputs
        missing_fields = []
        if year is None:
            missing_fields.append("year")
        if latitude is None:
            missing_fields.append("latitude")
        if longitude is None:
            missing_fields.append("longitude")
        if month is None:
            missing_fields.append("month")

        if missing_fields:
            return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400

        # Prepare features as a list
        features = [year, latitude, longitude, month]

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

        return jsonify({"predictions": formatted_predictions})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
