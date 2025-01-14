import os
import pickle

import pandas as pd


def load_models():
    """
    Load all models from the root-level models/ directory.

    Returns:
        dict: A dictionary with model names as keys and loaded model objects as values.
    """
    model_names = [
        "KNN M1",
        "Random Forest M1",
        "Linear Regression M1",
    ]

    models = {}

    # Locate the models directory relative to this script
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    model_dir = os.path.join(root_dir, "models")

    # Ensure the models directory exists
    if not os.path.exists(model_dir):
        raise FileNotFoundError(f"Models directory not found at {model_dir}")

    # Load specified models
    for model_name in model_names:
        filename = os.path.join(model_dir, f"{model_name.replace(' ', '_')}.sav")
        if os.path.exists(filename):
            with open(filename, "rb") as f:
                models[model_name] = pickle.load(f)
        else:
            raise FileNotFoundError(f"Model file not found: {filename}")

    return models


def make_predictions(models, features):
    """
    Generate predictions for a given set of features using all models.

    Args:
        models (dict): A dictionary of loaded models.
        features (list): The input features for prediction.

    Returns:
        dict: A dictionary with model names as keys and predictions as values.
    """
    predictions = {}

    # Ensure features is a DataFrame with the correct columns
    columns = [
        "Year",
        "Latitude",
        "Longitude",
        "Month",
    ]
    features_df = pd.DataFrame([features], columns=columns)

    for model_name, model in models.items():
        try:
            # Predict with the model
            prediction = model.predict(features_df)
            predictions[model_name] = prediction[0]
        except Exception as e:
            # Handle prediction errors gracefully
            predictions[model_name] = None

    return predictions
