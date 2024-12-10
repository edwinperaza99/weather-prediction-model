import pickle

import pandas as pd


def predict_with_all_models(model_names, future_input, df):
    """
    Predict future values using multiple pre-trained models.

    Parameters:
    model_names (list of str): List of model names to use for prediction.
    future_input (list of lists): Input data for future prediction, where each inner list represents a row of features.
    df (pandas.DataFrame): DataFrame containing the historical data (not used in the current implementation).

    Returns:
    dict: A dictionary where keys are model names and values are the predicted values. If a model file is not found, the value will be None.
    """
    predictions = {}

    for model_name in model_names:
        filename = f'../models/{model_name.replace(" ", "_")}.sav'

        try:
            # Load the model from disk
            loaded_model = pickle.load(open(filename, "rb"))

            # Ensure future_input is a DataFrame with valid feature names
            feature_names = ["Year", "Latitude", "Longitude", "Month"]
            future_input_df = pd.DataFrame(future_input, columns=feature_names)

            # Predict with the future input
            future_prediction = loaded_model.predict(future_input_df)[0]

            # Store the prediction
            predictions[model_name] = future_prediction
        except FileNotFoundError:
            print(f"Model file '{filename}' not found.")
            predictions[model_name] = None

    return predictions
