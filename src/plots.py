from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from loguru import logger

# Configure Matplotlib global settings
plt.rc("font", size=14)
plt.rc("axes", labelsize=14, titlesize=14)
plt.rc("legend", fontsize=14)
plt.rc("xtick", labelsize=10)
plt.rc("ytick", labelsize=10)

# Define the path for saving figures
IMAGES_PATH = Path("..") / "reports" / "figures"
IMAGES_PATH.mkdir(parents=True, exist_ok=True)


# Define the save_fig function
def save_fig(fig_id, tight_layout=True, fig_extension="png", resolution=300):
    """
    Save a matplotlib figure to a file.

    Parameters:
    fig_id (str): The identifier for the figure, used as the filename.
    tight_layout (bool, optional): Whether to use tight layout for the figure. Defaults to True.
    fig_extension (str, optional): The file extension for the saved figure (e.g., 'png', 'jpg'). Defaults to 'png'.
    resolution (int, optional): The resolution in dots per inch (DPI) for the saved figure. Defaults to 300.

    Raises:
    Exception: If there is an error during the saving process, an exception is raised and logged.
    """
    try:
        path = IMAGES_PATH / f"{fig_id}.{fig_extension}"
        logger.info(f"Attempting to save figure as {path}")

        if tight_layout:
            plt.tight_layout()

        plt.savefig(path, format=fig_extension, dpi=resolution)
        logger.success(f"Figure successfully saved at {path}")
    except Exception as e:
        logger.error(f"Failed to save figure: {e}")
        raise


def plot_results(results_df, top_n=3):
    """
    Generate and save various plots for model performance comparison.

    Parameters:
        results_df (pd.DataFrame): DataFrame containing model names and their metrics.
        top_n (int, optional): Number of top models to include in specific plots. Defaults to 3.

    Returns:
        None
    """
    # Convert results to DataFrame
    results_df = pd.DataFrame(results_df)

    # Define metrics to plot
    metrics = ["MAE", "MedAE", "MSE", "RMSE", "R2"]
    colors = ["lightcoral", "lightgreen", "gold", "skyblue", "mediumpurple"]

    # Sort results by R² descending and MAE ascending
    results_df = results_df.sort_values(by=["R2", "MAE"], ascending=[False, True])

    # Plot individual metrics as bar charts
    for metric, color in zip(metrics, colors):
        plt.figure(figsize=(10, 6))
        plt.bar(results_df["Model"], results_df[metric], color=color, edgecolor="black")
        plt.ylabel(metric)
        plt.title(f"Model Comparison: {metric}")
        plt.xticks(rotation=45, ha="right")
        plt.grid(axis="y", linestyle="--", alpha=0.7)
        save_fig(f"Comparison_{metric.replace(' ', '_')}")
        plt.show()

    # Heatmap of all metrics
    plt.figure(figsize=(10, 6))
    sns.heatmap(
        results_df.set_index("Model").T, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5
    )
    plt.title("Models Performance Metrics Heatmap")
    save_fig("Models_Performance_Metrics_Heatmap")
    plt.show()

    # Top N models grouped bar chart
    top_results_df = results_df.head(top_n)
    num_metrics = len(metrics)
    num_models = len(top_results_df)
    bar_width = 0.15
    x = np.arange(num_models)  # Positions for the models

    plt.figure(figsize=(12, 8))
    for i, metric in enumerate(metrics):
        plt.bar(
            x + i * bar_width,
            top_results_df[metric],
            bar_width,
            label=metric,
            color=colors[i],
            edgecolor="black",
        )

    plt.xticks(
        x + bar_width * (num_metrics - 1) / 2,
        top_results_df["Model"],
        rotation=45,
        ha="right",
        fontsize=10,
    )
    plt.title(f"Top {top_n} Models Comparison Across All Metrics", fontsize=16)
    plt.xlabel("Models", fontsize=12)
    plt.ylabel("Metric Value", fontsize=12)
    plt.legend(title="Metrics")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    save_fig(f"Top_{top_n}_Models_Comparison_Across_All_Metrics")
    plt.show()

    # Line chart for all metrics across top models
    plt.figure(figsize=(12, 6))
    for metric in metrics:
        plt.plot(top_results_df["Model"], top_results_df[metric], marker="o", label=metric)

    plt.title(f"Metrics Comparison Across Top {top_n} Models", fontsize=16)
    plt.xlabel("Models", fontsize=12)
    plt.ylabel("Metric Values", fontsize=12)
    plt.xticks(rotation=45, ha="right", fontsize=10)
    plt.legend(title="Metrics")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    save_fig(f"Multi_Line_Chart_Top_{top_n}_Models")
    plt.show()


def plot_model_results(y_test, y_pred, model_name):
    """
    Plots the results of a weather prediction model, including actual vs. predicted temperatures,
    a histogram of the predicted and actual temperatures, and a residual plot.

    Parameters:
    y_test (array-like): The actual temperature values.
    y_pred (array-like): The predicted temperature values from the model.
    model_name (str): The name of the model used for prediction.

    Returns:
    None
    """
    # Plot Actual vs. Predicted
    plt.figure(figsize=(8, 6))
    plt.scatter(
        y_test, y_pred, alpha=0.6, color="blue", edgecolor="k", label="Predicted vs Actual"
    )
    plt.plot(
        [y_test.min(), y_test.max()],
        [y_test.min(), y_test.max()],
        "r--",
        lw=2,
        label="Perfect Prediction",
    )
    plt.title(f"Actual vs Predicted Temperatures ({model_name})")
    plt.xlabel("Actual Temperatures")
    plt.ylabel("Predicted Temperatures")
    plt.grid(True)
    save_fig(f"Actual_vs_Predicted_{model_name.replace(' ', '_')}")
    plt.show()

    # Plot histogram for predicted temperatures
    plt.figure(figsize=(8, 6))
    plt.hist(y_pred, bins=25, alpha=0.7, label="Predicted", color="skyblue", edgecolor="black")
    plt.hist(y_test, bins=25, alpha=0.5, label="Actual", color="orange", edgecolor="black")
    plt.xlabel("Temperature")
    plt.ylabel("Frequency")
    plt.title(f"Distribution of Predicted vs Actual Temperatures ({model_name})")
    plt.legend()
    save_fig(f"Histogram_{model_name.replace(' ', '_')}")
    plt.show()

    # Calculate residuals (errors)
    residuals = y_test - y_pred

    # Plot residuals
    plt.figure(figsize=(8, 6))
    plt.scatter(y_pred, residuals, alpha=0.6, color="purple", edgecolor="k")
    plt.axhline(y=0, color="r", linestyle="--", lw=2)
    plt.title(f"Residual Plot ({model_name})")
    plt.xlabel("Predicted Temperatures")
    plt.ylabel("Residuals (Actual - Predicted)")
    plt.grid(True)
    save_fig(f"Residuals_{model_name.replace(' ', '_')}")
    plt.show()
