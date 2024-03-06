#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This is the main script which collects all functions and calculates the yield for the PV-System.

Infos:
    Pandas throws a warning:
        (df["col"][row_indexer] = value
    This is caused by pvlib because they are using an older syntax of pandas. This can be ignored.

    If the following warning is showing up and you do not get a plot, you are probably using linux.
        UserWarning: FigureCanvasAgg is non-interactive, and thus cannot be shown
        plt.show()
    To fix this you just have to install pyqt5 (pip install pyqt5)

    nomenclature for pv-software: https://duramat.github.io/pv-terms/
"""

# Import default libraries
import calendar as cal

# Import libraries
import pvlib
import pandas as pd
import matplotlib.pyplot as plt

# Import own modules
from config import HTW_LON, HTW_LAT, PATH_HTW_WEATHER, PATH_FRED_WEATHER, PATH_RESULTS
import htw_modules
import htw_inverter
import htw_weather


def setup_model(name, system, location):
    """
    From: `pvlib.modelchain.ModelChain`

    Parameters
    ----------
    name: str
        name of the pv-system
    system: object
        system parameters (pvlib.pvsystem.PVSystem object)
    location: object
        location (pvlib.location.Location)

    Returns
    -------
    pvlib.modelchain.ModelChain
        pvlib ModelChain object (pvlib.modelchain.ModelChain)

    """
    return pvlib.modelchain.ModelChain(system=system,
                                       location=location,
                                       # clearsky_model='ineichen',
                                       # transposition_model='haydavies',
                                       # solar_position_method='nrel_numpy',
                                       # airmass_model='kastenyoung1989',
                                       # dc_model=None,  # "CEC" is default
                                       # ac_model='sandia',
                                       aoi_model='physical',
                                       spectral_model='no_loss',
                                       # temperature_model='sapm',
                                       # dc_ohmic_model="dc_ohms_from_percent",  # why does it not work?
                                       losses_model='pvwatts',
                                       name=name
                                       )


if __name__ == "__main__":

    # Set the location
    htw_location = pvlib.location.Location(name='HTW Berlin',
                                           latitude=HTW_LAT,
                                           longitude=HTW_LON,
                                           tz='Europe/Berlin',
                                           altitude=80)

    # Set the Angles
    # The tilt angle is defined as degrees from horizontal (surface facing up = 0, surface facing horizon = 90)
    surface_tilt = 14.57

    # Azimuth angle of the module surface. North=0, East=90, South=180, West=270.
    surface_azimuth = 215

    # Set the Albedo
    albedo = 0.2

    # Set the temperature model ("open_rack_glass_polymer" (higher yield) or "close_mount_glass_glass")
    temperature_model_parameters = pvlib.temperature.TEMPERATURE_MODEL_PARAMETERS['sapm']['open_rack_glass_polymer']

    # pvwatts default losses:
    pvwatts_losses = {"soiling": 2,
                      "shading": 3,
                      "snow": 0,
                      "mismatch": 2,
                      "wiring": 2,
                      "connections": 0.5,
                      "lid": 1.5,
                      "nameplate_rating": 1,
                      "age": 0,
                      "availability": 3
                      }

    # Set up the PV System
    # WR 1:
    module_name = "Schott_ASI_105"
    module_parameters = htw_modules.modul1()  # Schott ASI 105
    inverter_name = "Danfoss_DLX_2.9"
    inverter_parameters = htw_inverter.inv1()  # Danfoss DLX 2.9
    modules_per_string = 10
    strings_per_inverter = 3

    wr1 = pvlib.pvsystem.PVSystem(  # arrays=,  # for multiple pv-arrays (e.g. 3 arrays with different angles)
                                  surface_tilt=surface_tilt,
                                  surface_azimuth=surface_azimuth,
                                  albedo=albedo,
                                  # surface_type=,
                                  module=module_name,
                                  module_type='glass_polymer',
                                  module_parameters=module_parameters,
                                  temperature_model_parameters=temperature_model_parameters,
                                  modules_per_string=modules_per_string,
                                  strings_per_inverter=strings_per_inverter,
                                  inverter=inverter_name,
                                  inverter_parameters=inverter_parameters,
                                  racking_model='close_mount',
                                  losses_parameters=pvwatts_losses,
                                  name="wr1"
                                  )

    # WR 2:
    module_name = "Aleo_Solar_S19y285"
    module_parameters = htw_modules.modul2()  # Aleo Solar S19 G2 285
    inverter_name = "Danfoss_DLX_2.9"
    inverter_parameters = htw_inverter.inv1()  # Danfoss DLX 2.9
    modules_per_string = 11
    strings_per_inverter = 1

    wr2 = pvlib.pvsystem.PVSystem(  # arrays=,  # for multiple arrays (e.g. 3 arrays with different angles)
                                  surface_tilt=surface_tilt,
                                  surface_azimuth=surface_azimuth,
                                  albedo=albedo,
                                  # surface_type=,
                                  module=module_name,
                                  module_type='glass_polymer',
                                  module_parameters=module_parameters,
                                  temperature_model_parameters=temperature_model_parameters,
                                  modules_per_string=modules_per_string,
                                  strings_per_inverter=strings_per_inverter,
                                  inverter=inverter_name,
                                  inverter_parameters=inverter_parameters,
                                  racking_model='close_mount',
                                  losses_parameters=pvwatts_losses,
                                  name="wr2"
                                  )
    # WR 3:
    module_name = "Aleo_Solar_S18_240"
    module_parameters = htw_modules.modul3()  # Aleo Solar S18 240
    inverter_name = "Danfoss_DLX_2.9"
    inverter_parameters = htw_inverter.inv1()  # Danfoss DLX 2.9
    modules_per_string = 14
    strings_per_inverter = 1

    wr3 = pvlib.pvsystem.PVSystem(  # arrays=,  # for multiple arrays (e.g. 3 arrays with different angles)
                                  surface_tilt=surface_tilt,
                                  surface_azimuth=surface_azimuth,
                                  albedo=albedo,
                                  # surface_type=,
                                  module=module_name,
                                  module_type='glass_polymer',
                                  module_parameters=module_parameters,
                                  temperature_model_parameters=temperature_model_parameters,
                                  modules_per_string=modules_per_string,
                                  strings_per_inverter=strings_per_inverter,
                                  inverter=inverter_name,
                                  inverter_parameters=inverter_parameters,
                                  racking_model='close_mount',
                                  losses_parameters=pvwatts_losses,
                                  name="wr3"
                                  )

    # WR 4:
    module_name = "Aleo_Solar_S19_245"
    module_parameters = htw_modules.modul4()  # Aleo Solar S19 G1 245
    inverter_name = "SMA_SB_3000HF-30"
    inverter_parameters = htw_inverter.inv2()  # SMA SUNNY BOY 3000HF-30
    modules_per_string = 13
    strings_per_inverter = 1

    wr4 = pvlib.pvsystem.PVSystem(  # arrays=,  # for multiple arrays (e.g. 3 arrays with different angles)
                                  surface_tilt=surface_tilt,
                                  surface_azimuth=surface_azimuth,
                                  albedo=albedo,
                                  # surface_type=,
                                  module=module_name,
                                  module_type='glass_polymer',
                                  module_parameters=module_parameters,
                                  temperature_model_parameters=temperature_model_parameters,
                                  modules_per_string=modules_per_string,
                                  strings_per_inverter=strings_per_inverter,
                                  inverter=inverter_name,
                                  inverter_parameters=inverter_parameters,
                                  racking_model='close_mount',
                                  losses_parameters=pvwatts_losses,
                                  name="wr4"
                                  )

    # WR 5:
    module_name = "Schott_ASI_105"
    module_parameters = htw_modules.modul1()  # Schott ASI 105
    inverter_name = "SMA_SB_3000HF-30"
    inverter_parameters = htw_inverter.inv2()  # SMA SUNNY BOY 3000HF-30
    modules_per_string = 10
    strings_per_inverter = 3

    wr5 = pvlib.pvsystem.PVSystem(  # arrays=,  # for multiple arrays (e.g. 3 arrays with different angles)
                                  surface_tilt=surface_tilt,
                                  surface_azimuth=surface_azimuth,
                                  albedo=albedo,
                                  # surface_type=,
                                  module=module_name,
                                  module_type='glass_polymer',
                                  module_parameters=module_parameters,
                                  temperature_model_parameters=temperature_model_parameters,
                                  modules_per_string=modules_per_string,
                                  strings_per_inverter=strings_per_inverter,
                                  inverter=inverter_name,
                                  inverter_parameters=inverter_parameters,
                                  racking_model='close_mount',
                                  losses_parameters=pvwatts_losses,
                                  name="wr5"
                                  )

    # Create the model
    mc1 = setup_model(wr1.name, wr1, htw_location)
    mc2 = setup_model(wr2.name, wr2, htw_location)
    mc3 = setup_model(wr3.name, wr3, htw_location)
    mc4 = setup_model(wr4.name, wr4, htw_location)
    mc5 = setup_model(wr5.name, wr5, htw_location)

    # Create the model list. Comment out, if you want to run specific models.
    models = [
        mc1,
        mc2,
        mc3,
        mc4,
        mc5
    ]

    # Get the weather-data
    # Read the file
    df_htw = pd.read_csv(PATH_HTW_WEATHER, sep=";")  # (mview!)
    df_fred = pd.read_csv(PATH_FRED_WEATHER, sep=",")

    # Convert the column names for the htw weather.
    df_htw = htw_weather.convert_column_names(df_htw, time="timestamp", ghi="g_hor_si",
                                              wind_speed="v_wind", temp_air="t_luft")

    df_fred = htw_weather.convert_column_names(df_fred, time="time", ghi="ghi",
                                               wind_speed="wind_speed", temp_air="temp_air")

    # Calculate the diffuse irradiation.
    df_htw = htw_weather.calculate_diffuse_irradiation(df_htw, parameter_name="ghi", lat=HTW_LAT, lon=HTW_LON)

    # Assign the weather DataFrame hourly resampled
    weather_htw = df_htw[["ghi", "dni", "dhi"]]  # only keep the important columns which are able to resample
    weather_htw = weather_htw.resample("h").mean()  # in Wh
    weather_fred = df_fred.resample("h").mean()  # in Wh
    weather_fred = weather_fred[weather_fred.index.year > 2014]

    # TODO: Run model with both weather data and compare!
    # Run the model
    for model in models:
        model.run_model(weather=weather_htw)

    # Create monthly results DataFrame
    result_monthly = pd.DataFrame()
    for model in models:
        result_monthly[model.name] = round(model.results.ac.resample('ME').sum() / 1000, 1)  # in kWh

    # Change the index of the monthly results (month name strings)
    result_monthly.index = month_names = [cal.month_name[i] for i in range(1, 13)]

    # Create annual results DataFrame
    result_annual = pd.DataFrame({
        "annual_yield": result_monthly.sum()
    })

    # Show the results (console)
    print("#" * 50)
    print(f"{' Execution successful! ':^50}")
    print("#" * 50, "\n")

    print(f"{' Results Monthly ':#^50}")
    print(result_monthly, "\n")

    print(f"{' Results Annual ':#^50}")
    print(result_annual, "\n")

    print(f"{' Results Total ':#^50}")
    print(result_annual.sum())

    # Export the results to csv files
    result_monthly.to_csv(path_or_buf=fr"{PATH_RESULTS}results_monthly.csv", sep=";", encoding="utf-8")
    # result_annual.to_csv(path_or_buf=fr"{PATH_RESULTS}results_annual.csv", sep=";", encoding="utf-8")

    # Plot the monthly yield
    result_monthly.plot.bar(rot=90, title="Monthly yield", ylabel="Energy in $kWh$", grid=True)
    plt.tight_layout()
    # plt.show()
    plt.savefig("results_monthly.png")
