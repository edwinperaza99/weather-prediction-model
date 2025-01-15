import pickle
from pathlib import Path

import numpy as np
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    median_absolute_error,
    r2_score,
)
from sklearn.model_selection import train_test_split

from src.plots import plot_model_results


def train_model(model, X, y, model_name, plot_results=True):
    """
    Trains a given machine learning model, evaluates its performance, and saves the trained model to a file.

    Parameters:
    model (object): The machine learning model to be trained.
    X (array-like): The input features for training the model.
    y (array-like): The target variable for training the model.
    model_name (str): The name of the model, used for saving the model file.

    Returns:
    dict: A dictionary containing the model name and various evaluation metrics:
        - "Model": The name of the model.
        - "MSE": Mean Squared Error.
        - "MAE": Mean Absolute Error.
        - "MedAE": Median Absolute Error.
        - "RMSE": Root Mean Squared Error.
        - "R2": R² Score.
    """
    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Evaluate the model
    mae = mean_absolute_error(y_test, y_pred)
    medae = median_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)

    # Ensure the `models` directory exists
    models_dir = Path(__file__).resolve().parents[2] / "models"
    models_dir.mkdir(parents=True, exist_ok=True)

    # Save the model
    file_path = models_dir / f"{model_name.replace(' ', '_')}.sav"
    with open(file_path, "wb") as file:
        pickle.dump(model, file)

    if plot_results:
        plot_model_results(y_test, y_pred, model_name)

    print(f"{model_name} - Mean Squared Error (MSE): {mse:.4f}")
    print(f"{model_name} - Mean Absolute Error (MAE): {mae:.4f}")
    print(f"{model_name} - Median Absolute Error (MedAE): {medae:.4f}")
    print(f"{model_name} - Root Mean Squared Error (RMSE): {rmse:.4f}")
    print(f"{model_name} - R² Score: {r2:.4f}")
    print(f"Model saved to: {file_path}")

    return {
        "Model": model_name,
        "MSE": mse,
        "MAE": mae,
        "MedAE": medae,
        "RMSE": rmse,
        "R2": r2,
    }
