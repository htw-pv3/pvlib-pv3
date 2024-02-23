#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This script contains the pv-inverter of the htw pv-system.
"""

import numpy as np
from pvlib import inverter


def inv1():
    """
    Import the Inverter Danfoss DLX 2.9 to pvlib

    Returns
    -------
    Dictionary
        inverter dictionary, type: sandia model
    """
    # inverter efficiency at different power points (source: PV*SOL)
    eta_min = [0, 0.953, 0.959, 0.963, 0.9612, 0.959]  # P/P_max = 0, 0.2, 0.3, 0.5, 0.75, 1; U = 210V
    eta_nom = [0, 0.961, 0.967, 0.971, 0.969, 0.967]  # P/P_max = 0, 0.2, 0.3, 0.5, 0.75, 1; U = 530V
    eta_max = [0, 0.952, 0.958, 0.962, 0.96, 0.958]  # P/P_max = 0, 0.2, 0.3, 0.5, 0.75, 1; U = 560V
    # dc voltage at min, nom and max
    dc_voltage = [[230.], [350.], [480.]]
    # calculate dc power
    p_dc_nom = 3750
    p_dc = [0, 0.2 * p_dc_nom, 0.3 * p_dc_nom, 0.5 * p_dc_nom, 0.75 * p_dc_nom, 1 * p_dc_nom]
    p_ac_min = []
    p_ac_nom = []
    p_ac_max = []
    val_count = len(eta_min)

    # calculate ac power
    for i in range(val_count):
        p_ac_min.append(p_dc[i] * eta_min[i])
        p_ac_nom.append(p_dc[i] * eta_nom[i])
        p_ac_max.append(p_dc[i] * eta_max[i])

    ac_power = np.array(p_ac_min + p_ac_nom + p_ac_max)

    # save all necessary inverter data to a dictionary
    sma_sb_data = {
        "ac_power": ac_power,
        "dc_power": np.array(p_dc + p_dc + p_dc),  # Annahme: Strom bleibt in allen Punkten gleich
        "dc_voltage": np.array(dc_voltage[0] * val_count + dc_voltage[1] * val_count + dc_voltage[2] * val_count),
        "dc_voltage_level": np.array(["Vmin"] * val_count + ["Vnom"] * val_count + ["Vmax"] * val_count),
        "p_ac_0": 2900.,
        "p_nt": 1.  # power consumed while inverter is not delivering AC power
    }

    # call method that creates sandia inverter model
    inverter_1 = inverter.fit_sandia(sma_sb_data["ac_power"], sma_sb_data["dc_power"], sma_sb_data["dc_voltage"],
                                     sma_sb_data["dc_voltage_level"], sma_sb_data["p_ac_0"], sma_sb_data["p_nt"])
    return inverter_1


def inv2():
    """
    Import the Inverter SMA SUNNY BOY 3000HF to pvlib

    Returns
    -------
    Dictionary
        inverter dictionary, type: sandia model
    """
    # inverter efficiency at different power points (source: SMA WirkungDerat-TI-de-36 | Version 3.6)
    eta_min = [0, 0.942, 0.95, 0.951, 0.94, 0.932]  # P/P_max = 0, 0.2, 0.3, 0.5, 0.75, 1; U = 210V
    eta_nom = [0, 0.953, 0.961, 0.963, 0.96, 0.954]  # P/P_max = 0, 0.2, 0.3, 0.5, 0.75, 1; U = 530V
    eta_max = [0, 0.951, 0.959, 0.96, 0.96, 0.955]  # P/P_max = 0, 0.2, 0.3, 0.5, 0.75, 1; U = 560V
    # dc voltage at min, nom and max
    dc_voltage = [[210.], [530.], [560.]]
    # calculate dc power
    p_dc_nom = 3150
    p_dc = [0, 0.2 * p_dc_nom, 0.3 * p_dc_nom, 0.5 * p_dc_nom, 0.75 * p_dc_nom, 1 * p_dc_nom]
    p_ac_min = []
    p_ac_nom = []
    p_ac_max = []
    val_count = len(eta_min)

    # calculate ac power
    for i in range(val_count):
        p_ac_min.append(p_dc[i] * eta_min[i])
        p_ac_nom.append(p_dc[i] * eta_nom[i])
        p_ac_max.append(p_dc[i] * eta_max[i])

    ac_power = np.array(p_ac_min + p_ac_nom + p_ac_max)

    # save all necessary inverter data to a dictionary
    sma_sb_data = {
        "ac_power": ac_power,
        "dc_power": np.array(p_dc + p_dc + p_dc),  # Annahme: Strom bleibt in allen Punkten gleich
        "dc_voltage": np.array(dc_voltage[0] * val_count + dc_voltage[1] * val_count + dc_voltage[2] * val_count),
        "dc_voltage_level": np.array(["Vmin"] * val_count + ["Vnom"] * val_count + ["Vmax"] * val_count),
        "p_ac_0": 3000.,
        "p_nt": 1.
    }

    # call method that creates sandia inverter model
    inverter_2 = inverter.fit_sandia(sma_sb_data["ac_power"], sma_sb_data["dc_power"], sma_sb_data["dc_voltage"],
                                     sma_sb_data["dc_voltage_level"], sma_sb_data["p_ac_0"], sma_sb_data["p_nt"])
    return inverter_2


if __name__ == "__main__":
    print(inv1())
    print(inv2())
