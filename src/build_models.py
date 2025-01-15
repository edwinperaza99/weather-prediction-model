#!/usr/bin/env python3
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor

from dataset import load_data_redivis, load_preprocessed_data
from features import preprocess_data
from modeling.train import train_model

# Load preprocessed data or raw data
df = load_preprocessed_data()
if df is None:
    print("Preprocessed data not found.")
    # data = load_data_redivis()
    # df = preprocess_data(data)

# Define features and target
X = df[["Year", "Latitude", "Longitude", "Month"]]
y = df["AverageTemperature"]

# Define models to train
models = {
    "KNN M1": KNeighborsRegressor(n_neighbors=5),
    "Random Forest M1": RandomForestRegressor(n_estimators=100, random_state=42),
    "Linear Regression M1": LinearRegression(),
}

# Train models and save results
results = []
for model_name, model in models.items():
    print(f"Training model: {model_name}")
    result = train_model(model, X, y, model_name, False)
    results.append(result)

print("\nModel training complete.")
for result in results:
    print(result)
