import pandas as pd
import redivis


def load_data():
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
    return df
