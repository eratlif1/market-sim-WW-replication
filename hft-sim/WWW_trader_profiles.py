N_66_noMM = {
    'A': {},
    'B': {},
    'C': {},
}

# 2 - A1 - 500: 0.106, 500**: 0.861, 1000ddagg: 0.033
N_66_noMM['A'][1] = {
    "background":
    {
        "ZIRP:Rmin_0_Rmax_500_thresh_1": 0.106,
        "ZIRP:Rmin_250_Rmax_500_thresh_1": 0.861,
        "ZIRP:Rmin_500_Rmax_1000_thresh_0.4": 0.033,
    }
}

# 3 - A4 - 125*: 0.113, 500**:0.887
N_66_noMM['A'][4] = {
    "background":
    {
        "ZIRP:Rmin_0_Rmax_125_thresh_0.8": 0.113,
        "ZIRP:Rmin_250_Rmax_500_thresh_1": 0.887
    }
}

# 5 - A12 - 250*: 0.223, 250: 0.209, 500**0.568
N_66_noMM['A'][12] ={
    "background":
    {
        "ZIRP:Rmin_0_Rmax_250_thresh_0.8": 0.223,
        "ZIRP:Rmin_0_Rmax_65_thresh_1": 0.209,
        "ZIRP:Rmin_250_Rmax_500_thresh_1": 0.568,
    }
}

# 7 - A24 - 125*: 0.296, 250: 0.704
N_66_noMM['A'][24] ={
    "background":
    {
        "ZIRP:Rmin_0_Rmax_125_thresh_0.8": 0.296,
        "ZIRP:Rmin_0_Rmax_65_thresh_1": 0.704,
    }
}

# 9 - B1 - 500**: 0.824, 1000dd: 0.176
N_66_noMM['B'][1] = {
    "background":
    {
        "ZIRP:Rmin_250_Rmax_500_thresh_1": 0.824,
        "ZIRP:Rmin_500_Rmax_1000_thresh_0.4": 0.033,
    }
}

# 10 - B4 - 500**: 0.714, 1000*: 0.193, 1000: 0.092
N_66_noMM['B'][4] = {
    "background":
    {
        "ZIRP:Rmin_250_Rmax_500_thresh_1": 0.714,
        "ZIRP:Rmin_0_Rmax_1000_thresh_0.8": 0.193,
        "ZIRP:Rmin_0_Rmax_1000_thresh_1": 0.092,
    }
}

# 11 - B12 - 500**: 0.683, 1000dd: 0.317
N_66_noMM['B'][12] ={
    "background":
    {
        "ZIRP:Rmin_250_Rmax_500_thresh_1": 0.683,
        "ZIRP:Rmin_500_Rmax_1000_thresh_0.4": 0.317,
    }
}

# 12 - B24 - 500**: 0.676, 1000dd: 0.324
N_66_noMM['B'][24] ={
    "background":
    {
        "ZIRP:Rmin_250_Rmax_500_thresh_1": 0.676,
        "ZIRP:Rmin_500_Rmax_1000_thresh_0.4": 0.324,
    }
}

# 14 - C1 - 500: 1.0
N_66_noMM['C'][1] = {
    "background":
    {
        "ZIRP:Rmin_0_Rmax_500_thresh_1": 1.0,
    }
}

# 16 - C4 - 1000*: 1.0
N_66_noMM['C'][4] = {
    "background":
    {
        "ZIRP:Rmin_0_Rmax_1000_thresh_0.8": 1.0,
    }
}

# 18 - C12 - 500: 0.011, 500**: 0.796, 1500dagg: 0.193
N_66_noMM['C'][12] = {
    "background":
    {
        "ZIRP:Rmin_0_Rmax_500_thresh_1": 0.011,
        "ZIRP:Rmin_250_Rmax_500_thresh_1": 0.796,
        "ZIRP:Rmin_0_Rmax_1500_thresh_0.6": 0.193,
    }
}

# 19 - C24 - 1000*: 0.995, 1500dagg: 0.005
N_66_noMM['C'][24] = {
    "background":
    {
        "ZIRP:Rmin_0_Rmax_1000_thresh_0.8": 0.995,
        "ZIRP:Rmin_0_Rmax_1500_thresh_0.6": 0.005,
    }
}

# profiles = {
    #     '65star': ZIR_profile({'R_min': 0, 'R_max': 65, 'eta': 0.8}), ZIRP:Rmin_0_Rmax_65_thresh_0.8
    #     '125star': ZIR_profile({'R_min': 0, 'R_max': 125, 'eta': 0.8}), ZIRP:Rmin_0_Rmax_125_thresh_0.8
    #     '125': ZIR_profile({'R_min': 0, 'R_max': 125, 'eta': 1.0}), ZIRP:Rmin_0_Rmax_125_thresh_1
    #     '250star': ZIR_profile({'R_min': 0, 'R_max': 250, 'eta': 0.8}), ZIRP:Rmin_0_Rmax_250_thresh_0.8
    #     '250': ZIR_profile({'R_min': 0, 'R_max': 65, 'eta': 1.0}), ZIRP:Rmin_0_Rmax_65_thresh_1
    #     '500': ZIR_profile({'R_min': 0, 'R_max': 500, 'eta': 1.0}), ZIRP:Rmin_0_Rmax_500_thresh_1
    #     '500dstar': ZIR_profile({'R_min': 250, 'R_max': 500, 'eta': 1.0}), ZIRP:Rmin_250_Rmax_500_thresh_1
    #     '1000star': ZIR_profile({'R_min': 0, 'R_max': 1000, 'eta': 0.8}), ZIRP:Rmin_0_Rmax_1000_thresh_0.8
    #     '1000': ZIR_profile({'R_min': 0, 'R_max': 1000, 'eta': 1.0}), ZIRP:Rmin_0_Rmax_1000_thresh_1
    #     '1000ddagg': ZIR_profile({'R_min': 500, 'R_max': 1000, 'eta': 0.4}), ZIRP:Rmin_500_Rmax_1000_thresh_0.4
    #     '1500dagg': ZIR_profile({'R_min': 0, 'R_max': 1500, 'eta': 0.6}), ZIRP:Rmin_0_Rmax_1500_thresh_0.6
    #     '2000ddagg': ZIR_profile({'R_min': 1000, 'R_max': 2000, 'eta': 0.4}), ZIRP:Rmin_1000_Rmax_2000_thresh_0.4
    #     '2500': ZIR_profile({'R_min': 0, 'R_max': 1500, 'eta': 0.6}), ZIRP:Rmin_0_Rmax_2500_thresh_1
# }

