from pathlib import Path

import pandas as pd
import redivis

RAW_DATA_PATH = Path("..") / "data" / "raw"
RAW_DATA_PATH.mkdir(parents=True, exist_ok=True)


def load_data_redivis(save=True):
    """
    Loads climate change earth surface temperature data from Redivis.

    This function connects to the Redivis platform using a specified user and dataset,
    retrieves the table containing global temperatures by major city, and converts it
    into a pandas DataFrame.

    Returns:
        pandas.DataFrame: A DataFrame containing the global temperatures by major city data.
    """
    user = redivis.user("cdpdemo")
    dataset = user.dataset("climate_change_earth_surface_temperature_data:1e0a:v1_0")
    table = dataset.table("global_temperatures_by_major_city:7x6x")
    df = table.to_pandas_dataframe()

    if save:
        raw_file_path = RAW_DATA_PATH / "global_temperature_raw.csv"
        df.to_csv(raw_file_path, index=False)
        print(f"Raw data saved to {raw_file_path}")

    return df

PROCESSED_DATA_PATH = Path("..") / "data" / "processed"
PROCESSED_DATA_PATH.mkdir(parents=True, exist_ok=True)

def load_preprocessed_data(processed_file_name="global_temperature_final.csv"):
    """
    Load preprocessed data if available; otherwise, notify that it doesn't exist.

    Args:
        processed_file_name (str, optional): The name of the processed data file. Defaults to "global_temperature_final.csv".

    Returns:
        pd.DataFrame or None: The preprocessed dataset if available, or None if the file doesn't exist.
    """
    processed_file_path = PROCESSED_DATA_PATH / processed_file_name

    # Check if processed data exists
    if processed_file_path.exists():
        print(f"Loading preprocessed data from {processed_file_path}")
        return pd.read_csv(processed_file_path)

    # If not, notify the user
    print(f"Processed data file '{processed_file_name}' does not exist in {PROCESSED_DATA_PATH}.")
    return None