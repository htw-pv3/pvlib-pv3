#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This script contains functions to prepare the weather-data from csv files.
"""

import pandas as pd
from pvlib import solarposition, irradiance

from config import HTW_LON, HTW_LAT, PATH_HTW_WEATHER, PATH_FRED_WEATHER


def calculate_diffuse_irradiation(df, parameter_name, lat, lon):
    # Index!! and changed outout!
    """
    Calculate diffuse irradiation

    Parameters
    ----------
    df : DataFrame
        Global Horizontal Irradiance (GHI)
    parameter_name : str
        Name of column with GHI
    lat : float
        Latitude
    lon : float
        Longitude
    Returns
    -------
    df_irradiance : DataFrame
        Calculated
            dni: the modeled direct normal irradiance in W/m^2.
            dhi: the modeled diffuse horizontal irradiance in W/m^2.
            kt: ratio of global to extraterrestrial irradiance on a horizontal plane.
    """

    # calculate dhi and dni for htw weatherdata
    df_solarpos = solarposition.spa_python(df.index, lat, lon)

    # Calculate dhi and dni from parameter
    df_irradiance = irradiance.erbs(ghi=df.loc[:, parameter_name],
                                    zenith=df_solarpos.zenith,
                                    datetime_or_doy=df.index.dayofyear)

    # Setup DataFrame
    df_irradiance = pd.DataFrame(df_irradiance)

    # Merge the DataFrame with the original one
    df_combined = df.merge(df_irradiance, left_index=True, right_index=True)

    return df_combined


def convert_column_names(df, time, ghi, wind_speed, temp_air):
    """ Converts the columns of a DataFrame and returns a DataFrame """
    # set the correct column names
    column_names = {time: "timestamp",
                    ghi: "ghi",
                    wind_speed: "wind_speed",
                    temp_air: "temp_air",
                    }
    df = df.rename(columns=column_names)

    # Set the timestamp as Index as a Datetime datatype
    df.set_index('timestamp', inplace=True)
    df.index = pd.to_datetime(df.index)

    return df


if __name__ == "__main__":
    # The dataframe for the weather data must fulfill the following conditions:
    # - Index named "timestamp" as Datetime datatype
    # - Contain the columns "ghi", "dhi", "dni"
    # - Sampled in hours

    # For the htw weather file you have to change the column names
    # and calculate the diffuse irradiation (dhi and dni).
    df_htw = pd.read_csv(PATH_HTW_WEATHER, sep=";")  # Read the file

    # For the fred file you only have to read the data because the column names are correct
    # and the diffuse irradiation is already available.
    df_fred = pd.read_csv(PATH_FRED_WEATHER, sep=",")  # Read the file

    # Convert the column names for the htw weather and calculate the diffuse irradiation.
    df_htw = convert_column_names(df_htw, time="timestamp", ghi="G_hor_Si", wind_speed="v_Wind", temp_air="T_Luft")
    df_htw = calculate_diffuse_irradiation(df_htw, parameter_name="ghi", lat=HTW_LAT, lon=HTW_LON)

    # Column names are already correct but the "timestamp" column has to be set as Index
    df_fred = convert_column_names(df_fred, time="time", ghi="ghi", wind_speed="wind_speed", temp_air="temp_air")

    # Assign the weather DataFrame hourly resampled
    weather_htw = df_htw.resample("h").mean()
    weather_fred = df_fred.resample("h").mean()
    weather_fred = weather_fred[weather_fred.index.year > 2014]

    # Print the results
    print(weather_htw)
    print("\n")
    print(weather_fred)
    print("\n")
    print("Maximum global horizontal irradiation:")
    print("htw:", df_htw.ghi.max())
    print("fred:", df_fred.ghi.max())

