#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This is the main script which collects all functions and calculates the yield for the PV-System.

Infos: Pandas throws a warning:
    (df["col"][row_indexer] = value
    This is caused by pvlib because they are using an older syntax of pandas. This can be ignored.

    nomenclature for pv-software: https://duramat.github.io/pv-terms/
"""

# Import libraries
import pvlib
import pandas as pd
import matplotlib.pyplot as plt

# Import own modules
from config import HTW_LON, HTW_LAT, PATH_HTW_WEATHER, PATH_FRED_WEATHER
import htw_modules, htw_inverter
import htw_weather


def setup_model(name, system, location):
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

    # Set the temperature model
    temperature_model_parameters = pvlib.temperature.TEMPERATURE_MODEL_PARAMETERS['sapm']['close_mount_glass_glass']

    # pvwatts default losses:
    pvwatts_losses = {"soiling": 2,
                      "shading": 3,
                      "snow": 0,
                      "mismatch":2,
                      "wiring": 2,
                      "connections": 0.5,
                      "lid": 1.5,
                      "nameplate_rating":1,
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
    df_htw = pd.read_csv(PATH_HTW_WEATHER, sep=";")
    df_fred = pd.read_csv(PATH_FRED_WEATHER, sep=",")

    # Convert the column names for the htw weather.
    df_htw = htw_weather.convert_column_names(df_htw, time="timestamp", ghi="G_hor_Si",
                                              wind_speed="v_Wind", temp_air="T_Luft")
    df_fred = htw_weather.convert_column_names(df_fred, time="time", ghi="ghi",
                                               wind_speed="wind_speed", temp_air="temp_air")

    # Calculate the diffuse irradiation.
    df_htw = htw_weather.calculate_diffuse_irradiation(df_htw, parameter_name="ghi", lat=HTW_LAT, lon=HTW_LON)

    # Assign the weather DataFrame hourly resampled
    weather_htw = df_htw.resample("h").mean()  # in Wh
    weather_fred = df_fred.resample("h").mean()  # in Wh
    weather_fred = weather_fred[weather_fred.index.year > 2014]

    # Run the model
    for model in models:
        model.run_model(weather=weather_htw)

    # Show the results
    result_monthly = pd.DataFrame()
    result_annual = []

    # Monthly
    for model in models:
        result_monthly[model.name] = model.results.ac.resample('ME').sum() / 1000  # in kWh
        result_annual.append(result_monthly.sum().values[-1])

    print("#" * 50)
    print("Execution complete!")
    print("#" * 50)
    print("\n")
    print("#"*10, "Result Monthly", "#"*10)
    print(result_monthly)
    print("\n")
    print("#" * 10, "Result Annual", "#" * 10)
    print(result_annual)
    print("\n")
    print("#" * 10, "Result Total", "#" * 10)
    print(sum(result_annual))

    # Plot the monthly yield
    result_monthly.index = result_monthly.index.astype(str)
    result_monthly.plot.bar(rot=90, title="Monthly yield", ylabel="Energy in kWh", grid=True)
    plt.tight_layout()
    plt.show()