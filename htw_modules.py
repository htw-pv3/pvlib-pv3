#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This script contains the pv-modules of the htw pv-system.
"""

import pandas as pd
from pvlib import pvsystem


def create_modules_df():
    """
    Creates a pandas dataframe with the correct parameter designation due to CEC method.

    Returns
    -------
    DataFrame
        Empty pandas DataFrame with index rows due to the CEC (California Energy Commission) convention.
    """
    # Module parameter due to CEC module database (California Energy Commission)
    module_param_keys = [
        #'Name',
        'Technology',  # example: Mono-c-Si or Multi-c-Si
        'Bifacial',  # 0: not Bifacial, 1: Bifacial
        'STC',  # Power at STC in W
        'PTC',  # (PVUSA Test Conditions) PTC are 1,000 Watts per square meter solar irradiance, 20 degrees C air temperature, and wind speed of 1 meter per second at 10 meters above ground level.
        'A_c',  # Module Area in m²
        'Length',  # Module length in m
        'Width',  # Module width in m
        'N_s',  # Number of cells
        'I_sc_ref',  # Short-Circuit current (Reference) in A
        'V_oc_ref',  # Open-Circuit voltage (Reference) in V
        'I_mp_ref',  # Current at maximum power point (Reference) in A
        'V_mp_ref',  # Voltage at maximum power point (Reference) in A
        'alpha_sc',  # Temperature coefficient of short circuit current in A/°C (= A/K)
        'beta_oc',  # Temperature coefficient of open circuit voltage in V/°C = V/K)
        'T_NOCT',  # Temperature at NOCT in °C (Nominal Operating Cell Temperature)
        'a_ref',  # The product of the usual diode ideality factor (n, unitless), number of cells in series (Ns), and cell thermal voltage at reference conditions, in V
        'I_L_ref',  # The light-generated current (or photocurrent) at reference conditions, in A
        'I_o_ref',  # The dark or diode reverse saturation current at reference conditions, in A
        'R_s',  # The series resistance at reference conditions, in Ohm
        'R_sh_ref',  # The shunt resistance at reference conditions, in Ohm
        'Adjust',  #  The adjustment to the temperature coefficient for short circuit current, in %
        'gamma_r',  # Temperature coefficient of power at maximum point point %/°C (= %/K)
        'BIPV',  # N: no, Y: yes
        'Version',  # Version
        'Date'  # Date
        ]
    modules = pd.DataFrame(index=module_param_keys)
    return modules


def modul1():
    """
    Creates a pandas dataframe of modul 1 (Schott ASI 105) of the htw pv-system.

    **WARNING**: This function currently returns the "BannerSolar_ISB20_1BSTC_105" module!

    Returns
    -------
    DataFrame
        Contains the module parameters due to CEC convention.

    """

    modules = create_modules_df()
    module_1 = {
        #"Name": "Schott_ASI_105",
        "Technology": "Thin Film a-Si",
        "Bifacial": 0,  # passt
        "STC": 105,  # passt
        "PTC": 95,  # ???
        "A_c": 1.449,  # Korrigiert 1.301
        "Length": 1.308,  # passt
        "Width": 1.108,  # passt
        "N_s": 72,  # Korrigiert 99
        "I_sc_ref": 4.05,  # Korrigiert 3.98
        "V_oc_ref": 41.1,  # Korrigiert 41.0
        "I_mp_ref": 3.44,  # Korrigiert 3.38
        "V_mp_ref": 30.5,  # Korrigiert 31.1
        "alpha_sc": 0.00324,  # 0.08 %/K * 4.05 A = 0,0008 1/K * 4,05 A = 0.00324 A/K
        "beta_oc": -0.136,  # -0.33%/K * 41.1 V = -0.0033 1/K * 41.1 V =  −0.13563 V/K
        "T_NOCT": 49,  # passt
        "a_ref": 1.8,  # ???? # Korrigiert 4.992423 -> from Schott_Solar_SAPC_165
        "I_L_ref": 5,  # ? 1.555012 -> from Schott_Solar_SAPC_165
        "I_o_ref": 0.0,  # ?
        "R_s": 0.6,  # ? 18.133308,  -> from Schott_Solar_SAPC_165
        "R_sh_ref": 125,  # ? 357.773926,  -> from Schott_Solar_SAPC_165
        "Adjust": 9,  # ?  -11.692039,  -> from Schott_Solar_SAPC_165
        "gamma_r": -0.2,  # passt
        "BIPV": "N",
        "Version": "",
        "Date": ""
    }
    modules["module_1"] = list(module_1.values())

    # TEST!!!
    return pvsystem.retrieve_sam('CECMod')["BannerSolar_ISB20_1BSTC_105"]
    #return modules["module_1"]


def modul2():
    """
    Creates a pandas dataframe of modul 2 (Aleo Solar S19 285) of the htw pv-system.

    Returns
    -------
    DataFrame
        Contains the module parameters due to CEC convention.

    """

    module_2 = pvsystem.retrieve_sam('CECMod')["Aleo_Solar_S19y285"]
    return module_2


def modul3():
    """
    Creates a pandas dataframe of modul 3 (Aleo Solar S18 240) of the htw pv-system.

    **WARNING**: This function currently returns the "alfasolar_alfasolar_P6L60_240" module!

    Returns
    -------
    DataFrame
        Contains the module parameters due to CEC convention.

    """

    modules = create_modules_df()
    module_3 = {
        #"Name": "aleo_solar_s18_240",
        "Technology": "Thin Film a-Si",
        "Bifacial": 0,  #
        "STC": 240,  #
        "PTC": 215.04,  #
        "A_c": 1.643,  #
        "Length": 1.660,  #
        "Width": 0.990,  #
        "N_s": 60,  #
        "I_sc_ref": 8.65,  #
        "V_oc_ref": 37.0,  #
        "I_mp_ref": 8.13,  #
        "V_mp_ref": 29.5,  #
        "alpha_sc": 0.00346,  # 0.04 %/K * 8.65 A = 0,0004 1/K * 8.65 A = 0.00346 A/K
        "beta_oc": -0.126,  # -0.34%/K * 37 V = -0.0034 1/K * 37 V =  −0.1258 V/K
        "T_NOCT": 48,  #
        "a_ref": 2.6,  # ? -> from Aleo_Solar_S19y285
        "I_L_ref": 8.66,  # ? -> from Aleo_Solar_S19y285
        "I_o_ref": 0.0,  # ? -> from Aleo_Solar_S19y285
        "R_s": 0.38,  # ? -> from Aleo_Solar_S19y285
        "R_sh_ref": 180,  # ? -> from Aleo_Solar_S19y285
        "Adjust": 5,  # ? -> from Aleo_Solar_S19y285
        "gamma_r": -0.46,  #
        "BIPV": "N",
        "Version": "",
        "Date": ""
    }
    modules["module_3"] = list(module_3.values())

    # TEST!!!
    return pvsystem.retrieve_sam('CECMod')["alfasolar_alfasolar_P6L60_240"]
    #return modules["module_3"]


def modul4():
    """
    Creates a pandas dataframe of modul 3 (Aleo Solar S19 245) of the htw pv-system.

    **WARNING**: This function currently returns the "American_Solar_Wholesale_ASW_245P" module!

    Returns
    -------
    DataFrame
        Contains the module parameters due to CEC convention.

    """

    modules = create_modules_df()
    module_4 = {
        #"Name": "aleo_solar_s19_245",
        "Technology": "Thin Film a-Si",
        "Bifacial": 0,  #
        "STC": 245,  #
        "PTC": 220,  #
        "A_c": 1.643,  #
        "Length": 1.660,  #
        "Width": 0.990,  #
        "N_s": 60,  #
        "I_sc_ref": 8.48,  #
        "V_oc_ref": 37.1,  #
        "I_mp_ref": 7.84,  #
        "V_mp_ref": 31.3,  #
        "alpha_sc": 0.00254,  # 0.03 %/K * 8.48 A = 0.0003 1/K * 8.48 A = 0.002544 A/K
        "beta_oc": -0.126,  # -0.34%/K * 37.1 V = -0.0034 1/K * 37.1 V =  -0.12614 V/K
        "T_NOCT": 47,  #
        "a_ref": 1.543921,  # ? -> from Aleo_Solar_S19Y270
        "I_L_ref": 9.208019,  # ? -> from Aleo_Solar_S19Y270
        "I_o_ref": 0.0,  # ? -> from Aleo_Solar_S19Y270
        "R_s": 0.299333,  # ? -> from Aleo_Solar_S19Y270
        "R_sh_ref": 343.407196,  # ? -> from Aleo_Solar_S19Y270
        "Adjust": 12.272744,  # ? -> from Aleo_Solar_S19Y270
        "gamma_r": -0.48,  #
        "BIPV": "N",
        "Version": "",
        "Date": ""
    }
    modules["module_4"] = list(module_4.values())

    # TEST!!!
    return pvsystem.retrieve_sam('CECMod')["American_Solar_Wholesale_ASW_245P"]
    #return modules["module_4"]


if __name__ == "__main__":
    print("\n", modul1())
    print("\n", modul2())
    print("\n", modul3())
    print("\n", modul4())
