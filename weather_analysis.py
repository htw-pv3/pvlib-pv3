#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This module is used to analyze the htw and openfred weather data.
"""


# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Import default modules
import calendar as cal

# Import own modules
from htw_weather import convert_column_names, calculate_diffuse_irradiation
from config import PATH_HTW_WEATHER, PATH_FRED_WEATHER, HTW_LON, HTW_LAT


def get_month_list(df):
    """
    Creates a daily list with the month names and empty strings between.
    This is used for the x-tick strings of bar plots with huge data to avoid crowded x-ticks.

    Parameters
    ----------
    df: pd.DataFrame
        Pandas DataFrame or Series with a daily based Datetime Index.

    Returns
    -------
    month_list: list[str]
        Daily list with the month names and empty strings between.
    """

    month_list = []
    i = 0
    for day in df.index:
        if day.month > i:
            month_list.append(cal.month_name[day.month])
            i += 1
        else:
            month_list.append('')

    return month_list


def year_plot(series, title):
    """
    Plots the complete year of the Series.

    Parameters
    ----------
    series: Series
        Pandas Series with daily based Datetime Index.

    title: Str
        Plot title

    Returns
    -------
    Plot
        matplotlib.pyplot.plot object
    """
    # Basic stacked bar-plot command
    ax = series.plot(kind='bar', figsize=(14, 6))

    # Define a y-limit
    plt.ylim([0, 8200])

    # Define the labels.
    plt.title(title)
    plt.ylabel("Global horizontal irradiation in $Wh/m²$")
    plt.xlabel("")
    plt.grid(axis='y')

    # Create a daily list with the month names and empty strings between
    # This is necessary because otherwise the x-ticks would be completely crowded
    month = get_month_list(series)

    # To show the month and day in a defined distance of days
    # tick_rate = 19 #  for every x day
    # Make most of the tick labels empty so the labels don't get too crowded
    # tick_labels = [''] * len(stacked.index)
    # tick_labels[::tick_rate] = [item.strftime('%b %d') for item in stacked.index[::tick_rate]]
    # ax.xaxis.set_major_formatter(ticker.FixedFormatter(tick_labels))

    # Set the month list as x-ticks
    ax.xaxis.set_major_formatter(ticker.FixedFormatter(month))

    # Use the tight_layout property to avoid cut off text
    plt.tight_layout()

    return plt


def year_plot_stacked(df):
    """
    Stacked plot the complete year of the DataFrame.

    Parameters
    ----------
    df: pd.DataFrame
        Pandas DataFrame with daily based Datetime Index and the columns to be in a stacked bar plot.

    Returns
    -------
    Plot
        matplotlib.pyplot.plot object
    """
    # Basic stacked bar-plot command
    ax = df.plot(kind='bar', stacked=True, figsize=(14, 6))

    # Define the Y-label
    plt.ylabel("Global horizontal irradiation in $Wh/m²$")
    plt.xlabel("")

    month = get_month_list(df)

    # Set the month list as x-ticks
    ax.xaxis.set_major_formatter(ticker.FixedFormatter(month))

    # Use the tight_layout property to avoid cut off text
    plt.tight_layout()

    return plt


if __name__ == "__main__":
    ####################################################
    # Analyzing the HTW Weather-Data Plot with the gaps
    ####################################################
    month_names = [cal.month_name[i] for i in range(1, 13)]  # Create a list of month name strings

    # Read the Dataframe
    # For the htw weather file you have to change the column names
    # and calculate the diffuse irradiation (dhi and dni).
    df_htw = pd.read_csv(PATH_HTW_WEATHER, sep=";")  # Read the file (mview!)

    # Convert the column names for the htw weather and calculate the diffuse irradiation.
    df_htw = convert_column_names(df_htw, time="timestamp", ghi="g_hor_si", wind_speed="v_wind", temp_air="t_Luft")
    df_htw = calculate_diffuse_irradiation(df_htw, parameter_name="ghi", lat=HTW_LAT, lon=HTW_LON)

    # Create another DataFrame for the plot
    stacked = pd.DataFrame({
        "normal": df_htw.ghi[df_htw.is_filled == "f"],
        "filled_day": df_htw.ghi[(df_htw.is_filled == "t") & (df_htw.is_during_day == "t")],
        "filled_night": df_htw.ghi[(df_htw.is_filled == "t") & (df_htw.is_during_day == "f")]
    })

    # Resample the DataFrame
    stacked = stacked.resample("h").mean()  # in Wh/m²
    stacked = stacked.resample("d").sum()  # into daily data

    ###########################################
    # Analyzing the HTW Weather-Data Plot
    ###########################################
    # Read the DataFrame
    df_htw = df_htw.copy()
    # Just keep the column to plot
    df_htw = df_htw.ghi  # Column name could be slightly different !

    # Resample the DataFrame
    df_htw = df_htw.resample("h").mean()  # in Wh/m²
    df_htw = df_htw.resample("d").sum()  # into daily data
    htw_monthly = df_htw.resample("ME").sum() / 1000  # into monthly data
    htw_monthly.index = month_names  # change index names

    ###########################################
    # Analyzing the open_fred Weather-Data Plot
    ###########################################
    # Read the DataFrame
    df_fred = pd.read_csv(PATH_FRED_WEATHER, sep=",")

    # Just keep the column to plot
    # Column names are already correct but the "timestamp" column has to be set as Index
    df_fred = convert_column_names(df_fred, time="time", ghi="ghi", wind_speed="wind_speed", temp_air="temp_air")
    df_fred = df_fred[df_fred.index.year > 2014]  # Filtering the data
    df_fred = df_fred.ghi

    # Resample the DataFrame
    # Into daily data:
    df_fred = df_fred.resample("h").mean()  # in Wh/m²
    df_fred = df_fred.resample("d").sum()  # into daily data
    fred_monthly = df_fred.resample("ME").sum() / 1000  # into monthly data
    fred_monthly.index = month_names  # change index names

    ################
    # Plot the data
    ################
    plot_yearly = False  # Set to True or False
    if plot_yearly:
        year_plot_stacked(stacked).show()
        year_plot(df_htw, title="HTW Data").show()
        year_plot(df_fred, title="Open_fred Data").show()

    ########################
    # Plot monthly results
    ########################
    plot_monthly = True  # Set to True or False

    results_monthly = pd.DataFrame()
    results_monthly["HTW"] = htw_monthly
    results_monthly["Openfred"] = fred_monthly

    if plot_monthly:
        results_monthly.plot(kind="bar", figsize=(14, 6))
        plt.grid(axis="y")
        plt.ylabel("Irradiation in kWh/m²")
        plt.tight_layout()
        plt.show()

    ##################
    # Print total sum
    ##################
    print(f"{' Results ':#^50}")
    print(f"HTW: Total anual irradiation: {round(df_htw.sum() / 1000, 1)} kWh/m²")
    print(f"Openfred: Total anual irradiation: {round(df_fred.sum() / 1000, 1)} kWh/m²")
    print("\n")
    print("Monthly results HTW:")
    print(results_monthly)
