#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This script contains the pv-modules of the htw pv-system.
"""

import pandas as pd
from pvlib import pvsystem, ivtools


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
        'PTC',  # (PVUSA Test Conditions) PTC are 1,000 Watts per square meter solar irradiance,
        # 20 degrees C air temperature, and wind speed of 1 meter per second at 10 meters above ground level.
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
        'a_ref',  # The product of the usual diode ideality factor (n, unitless), number of cells in series (Ns),
        # and cell thermal voltage at reference conditions, in V
        'I_L_ref',  # The light-generated current (or photocurrent) at reference conditions, in A
        'I_o_ref',  # The dark or diode reverse saturation current at reference conditions, in A
        'R_s',  # The series resistance at reference conditions, in Ohm
        'R_sh_ref',  # The shunt resistance at reference conditions, in Ohm
        'Adjust',  # The adjustment to the temperature coefficient for short circuit current, in %
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

    Returns
    -------
    DataFrame
        Contains the module parameters due to CEC convention.

    """
    # Typical manufacturer data-sheet parameters:
    celltype = "amorphous"  # 'monoSi', 'multiSi', 'polySi', 'cis', 'cigs', 'cdte', 'amorphous'
    width = 1.108
    length = 1.308
    ptc = 95
    stc = 105
    bifacial = 0  # 0: Not Bifacial ; 1: Bifacial
    technology = "2-a-Si"
    t_noct = 49

    # Parameters for the fit_cec_sam function
    v_mp = 31.1
    i_mp = 3.38
    v_oc = 41.0
    i_sc = 3.98
    alpha_sc = 0.003184  # 0.08 %/K * 4.05 A = 0,0008 1/K * 4,05 A = 0.00324 A/K
    beta_voc = -0.1353  # -0.33%/K * 41.1 V = -0.0033 1/K * 41.1 V =  −0.13563 V/K
    gamma_pmp = -0.2
    cells_in_series = 72
    temp_ref = 25

    cec_params = ivtools.sdm.fit_cec_sam(
                celltype=celltype,
                v_mp=v_mp,
                i_mp=i_mp,
                v_oc=v_oc,
                i_sc=i_sc,
                alpha_sc=alpha_sc,
                beta_voc=beta_voc,
                gamma_pmp=gamma_pmp,
                cells_in_series=cells_in_series,
                temp_ref=temp_ref)
    # Returns: I_L_ref, I_o_ref, R_s, R_sh_ref, a_ref and Adjust.

    modules = create_modules_df()
    module_1 = {
        #"Name": "Schott_ASI_105",
        "Technology": technology,
        "Bifacial": bifacial,
        "STC": stc,
        "PTC": ptc,
        "A_c": width*length,
        "Length": length,
        "Width": width,
        "N_s": cells_in_series,
        "I_sc_ref": i_sc,
        "V_oc_ref": v_oc,
        "I_mp_ref": i_mp,
        "V_mp_ref": v_mp,
        "alpha_sc": alpha_sc,
        "beta_oc": beta_voc,
        "T_NOCT": t_noct,
        "a_ref": cec_params[4],
        "I_L_ref": cec_params[0],
        "I_o_ref": cec_params[1],
        "R_s": cec_params[2],
        "R_sh_ref": cec_params[3],
        "Adjust": cec_params[5],
        "gamma_r": gamma_pmp,
        "BIPV": "N",
        "Version": "",
        "Date": ""
    }
    modules["Schott_ASI_105"] = list(module_1.values())

    # return pvsystem.retrieve_sam('CECMod')["BannerSolar_ISB20_1BSTC_105"]
    return modules["Schott_ASI_105"]


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

    Returns
    -------
    DataFrame
        Contains the module parameters due to CEC convention.

    """
    # Typical manufacturer data-sheet parameters:
    celltype = "monoSi"  # 'monoSi', 'multiSi', 'polySi', 'cis', 'cigs', 'cdte', 'amorphous'
    width = 0.990
    length = 1.660
    ptc = 215.04
    stc = 240
    bifacial = 0  # 0: Not Bifacial ; 1: Bifacial
    technology = "mono-si"
    t_noct = 48

    # Parameters for the fit_cec_sam function
    v_mp = 29.5
    i_mp = 8.13
    v_oc = 37.0
    i_sc = 8.65
    alpha_sc = 0.00346  # 0.04 %/K * 8.65 A = 0.0004 1/K * 8.65 A = 0.00346 A/K
    beta_voc = -0.1258  # -0.34%/K * 37 V = -0.0034 1/K * 37 V =  −0.1258 V/K
    gamma_pmp = -0.46
    cells_in_series = 60
    temp_ref = 25

    cec_params = ivtools.sdm.fit_cec_sam(
                celltype=celltype,
                v_mp=v_mp,
                i_mp=i_mp,
                v_oc=v_oc,
                i_sc=i_sc,
                alpha_sc=alpha_sc,
                beta_voc=beta_voc,
                gamma_pmp=gamma_pmp,
                cells_in_series=cells_in_series,
                temp_ref=temp_ref)
    # Returns: I_L_ref, I_o_ref, R_s, R_sh_ref, a_ref and Adjust.

    modules = create_modules_df()
    module_3 = {
        #"Name": "Aleo_Solar_S18_240",
        "Technology": technology,
        "Bifacial": bifacial,
        "STC": stc,
        "PTC": ptc,
        "A_c": width*length,
        "Length": length,
        "Width": width,
        "N_s": cells_in_series,
        "I_sc_ref": i_sc,
        "V_oc_ref": v_oc,
        "I_mp_ref": i_mp,
        "V_mp_ref": v_mp,
        "alpha_sc": alpha_sc,
        "beta_oc": beta_voc,
        "T_NOCT": t_noct,
        "a_ref": cec_params[4],
        "I_L_ref": cec_params[0],
        "I_o_ref": cec_params[1],
        "R_s": cec_params[2],
        "R_sh_ref": cec_params[3],
        "Adjust": cec_params[5],
        "gamma_r": gamma_pmp,
        "BIPV": "N",
        "Version": "",
        "Date": ""
    }

    modules["Aleo_Solar_S18_240"] = list(module_3.values())

    # return pvsystem.retrieve_sam('CECMod')["alfasolar_alfasolar_P6L60_240"]
    return modules["Aleo_Solar_S18_240"]


def modul4():
    """
    Creates a pandas dataframe of modul 3 (Aleo Solar S19 245) of the htw pv-system.

    Returns
    -------
    DataFrame
        Contains the module parameters due to CEC convention.

    """
    # Typical manufacturer data-sheet parameters:
    celltype = "amorphous"  # 'monoSi', 'multiSi', 'polySi', 'cis', 'cigs', 'cdte', 'amorphous'
    width = 0.990
    length = 1.660
    ptc = 220
    stc = 245
    bifacial = 0  # 0: Not Bifacial ; 1: Bifacial
    technology = "Thin Film a-Si"
    t_noct = 47

    # Parameters for the fit_cec_sam function
    v_mp = 31.3
    i_mp = 7.84
    v_oc = 37.1
    i_sc = 8.48
    alpha_sc = 0.002544  # 0.03 %/K * 8.48 A = 0.0003 1/K * 8.48 A = 0.002544 A/K
    beta_voc = -0.12614  # -0.34%/K * 37.1 V = -0.0034 1/K * 37.1 V =  -0.12614 V/K
    gamma_pmp = -0.48
    cells_in_series = 60
    temp_ref = 25

    cec_params = ivtools.sdm.fit_cec_sam(
                celltype=celltype,
                v_mp=v_mp,
                i_mp=i_mp,
                v_oc=v_oc,
                i_sc=i_sc,
                alpha_sc=alpha_sc,
                beta_voc=beta_voc,
                gamma_pmp=gamma_pmp,
                cells_in_series=cells_in_series,
                temp_ref=temp_ref)
    # Returns: I_L_ref, I_o_ref, R_s, R_sh_ref, a_ref and Adjust.

    modules = create_modules_df()
    module_4 = {
        #"Name": "Aleo_Solar_S19_245",
        "Technology": technology,
        "Bifacial": bifacial,
        "STC": stc,
        "PTC": ptc,
        "A_c": width*length,
        "Length": length,
        "Width": width,
        "N_s": cells_in_series,
        "I_sc_ref": i_sc,
        "V_oc_ref": v_oc,
        "I_mp_ref": i_mp,
        "V_mp_ref": v_mp,
        "alpha_sc": alpha_sc,
        "beta_oc": beta_voc,
        "T_NOCT": t_noct,
        "a_ref": cec_params[4],
        "I_L_ref": cec_params[0],
        "I_o_ref": cec_params[1],
        "R_s": cec_params[2],
        "R_sh_ref": cec_params[3],
        "Adjust": cec_params[5],
        "gamma_r": gamma_pmp,
        "BIPV": "N",
        "Version": "",
        "Date": ""
    }

    modules["Aleo_Solar_S19_245"] = list(module_4.values())

    # return pvsystem.retrieve_sam('CECMod')["American_Solar_Wholesale_ASW_245P"]
    return modules["Aleo_Solar_S19_245"]


if __name__ == "__main__":
    print("\n", modul1())
    print("\n", modul2())
    print("\n", modul3())
    print("\n", modul4())
