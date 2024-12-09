import pandas as pd


# Function to convert latitude and longitude into numeric
def convert_lat_lon(value):
    """
    Converts a latitude or longitude value from a string format with a direction
    indicator (N, S, E, W) to a float. North (N) and East (E) are positive values,
    while South (S) and West (W) are negative values.

    Parameters:
        value (str): The latitude or longitude value as a string, ending with a
                     direction indicator (N, S, E, W).

    Returns:
        float: The converted latitude or longitude value as a float.
    """
    if value[-1] in ["N", "E"]:
        return float(value[:-1])  # North and East are positive
    else:
        return -float(value[:-1])  # South and West are negative


def preprocess_data(df):
    """
    Preprocess the input DataFrame by performing the following steps:

    1. Convert the 'dt' column to datetime format.
    2. Extract the year, month, and day from the 'dt' column into separate columns.
    3. Remove rows where the year is before 1870.
    4. Remove rows with missing values in 'AverageTemperature' and 'AverageTemperatureUncertainty' columns.
    5. Convert 'Latitude' and 'Longitude' columns to float if they are not already.
    6. Perform one-hot encoding for the 'Country' column.
    7. Drop the 'City' and 'dt' columns if they exist in the DataFrame.

    Parameters:
    df (pandas.DataFrame): The input DataFrame containing weather data.

    Returns:
    pandas.DataFrame: The preprocessed DataFrame.
    """
    df["dt"] = pd.to_datetime(df["dt"])  # Convert dt to datetime format
    df["Year"] = df["dt"].dt.year  # Extract the year
    df["Month"] = df["dt"].dt.month  # Extract the Month
    df["Day"] = df["dt"].dt.day  # Extract the day

    # Remove rows where the year is before 1870
    df = df[df["Year"] >= 1870]

    # Remove rows with missing values
    df = df.dropna(subset=["AverageTemperature", "AverageTemperatureUncertainty"])

    # Apply the function to Latitude and Longitude columns, only if needed
    if df["Latitude"].dtype != "float64" and df["Latitude"].dtype != "int64":
        df["Latitude"] = df["Latitude"].apply(convert_lat_lon)
    if df["Longitude"].dtype != "float64" and df["Longitude"].dtype != "int64":
        df["Longitude"] = df["Longitude"].apply(convert_lat_lon)

    # Perform one-hot encoding for the 'Country' column in place
    df = pd.get_dummies(df, columns=["Country"], drop_first=True)

    # Drop the 'City' and 'dt' columns only if they exist
    columns_to_drop = ["City", "dt"]
    df = df.drop(columns=[col for col in columns_to_drop if col in df.columns])

    return df
