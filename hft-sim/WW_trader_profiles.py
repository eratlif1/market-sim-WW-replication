import numpy as np


"""
[Wah dissertation]: Table 5.1: ZI strategy combinations included in empirical game-theoretic analysis of market
    structure games with varying latencies.
    Rmin    Rmax    η
    0       125     1
    0       250     1
    0       500     1
    250     500     1
    0       1000    1
    500     1000    0.4
    500     1000    1
    0       1500    0.6
    1000    2000    0.4
    0       2500    0.4
    0       2500    1
"""

profiles = {
    '125': 'ZIRP:Rmin_0_Rmax_125_thresh_1',
    '250': 'ZIRP:Rmin_0_Rmax_250_thresh_1',
    '500': 'ZIRP:Rmin_0_Rmax_500_thresh_1',
    '500_dstar': 'ZIRP:Rmin_250_Rmax_500_thresh_1',
    '1000': 'ZIRP:Rmin_0_Rmax_1000_thresh_1',
    '1000_ddagger': 'ZIRP:Rmin_500_Rmax_1000_thresh_.4',
    '1000_dstar': 'ZIRP:Rmin_500_Rmax_1000_thresh_1',
    '1500_dagger': 'ZIRP:Rmin_0_Rmax_1500_thresh_.6',
    '2000_ddagger': 'ZIRP:Rmin_1000_Rmax_2000_thresh_.4',
    '2500_circle': 'ZIRP:Rmin_0_Rmax_2500_thresh_.4',
    '2500': 'ZIRP:Rmin_0_Rmax_2500_thresh_1',
}


environments = {}

env_1 = {}
env_1['CDA'] = {}
env_1['2M'] = {}
env_1['2M LA'] = {}

# profiles = {
#     '125': ZIR_profile({'R_min': 0, 'R_max': 125, 'eta': 1}), ZIRP:Rmin_0_Rmax_125_thresh_1
#     '250': ZIR_profile({'R_min': 0, 'R_max': 250, 'eta': 1}), ZIRP:Rmin_0_Rmax_250_thresh_1
#     '500': ZIR_profile({'R_min': 0, 'R_max': 500, 'eta': 1}), ZIRP:Rmin_0_Rmax_500_thresh_1
#     '500_dstar': ZIR_profile({'R_min': 250, 'R_max': 500, 'eta': 1}), ZIRP:Rmin_250_Rmax_500_thresh_1
#     '1000': ZIR_profile({'R_min': 0, 'R_max': 1000, 'eta': 1}), ZIRP:Rmin_0_Rmax_1000_thresh_1
#     '1000_ddagger': ZIR_profile({'R_min': 500, 'R_max': 1000, 'eta': 0.4}), ZIRP:Rmin_500_Rmax_1000_thresh_.4
#     '1000_dstar': ZIR_profile({'R_min': 500, 'R_max': 1000, 'eta': 1}), ZIRP:Rmin_500_Rmax_1000_thresh_1
#     '1500_dagger': ZIR_profile({'R_min': 0, 'R_max': 1500, 'eta': 0.6}), ZIRP:Rmin_0_Rmax_1500_thresh_.6
#     '2000_ddagger': ZIR_profile({'R_min': 1000, 'R_max': 2000, 'eta': 0.4}), ZIRP:Rmin_1000_Rmax_2000_thresh_.4
#     '2500_circle': ZIR_profile({'R_min': 0, 'R_max': 2500, 'eta': 0.4}), ZIRP:Rmin_0_Rmax_2500_thresh_.4
#     '2500': ZIR_profile({'R_min': 0, 'R_max': 2500, 'eta': 1}), ZIRP:Rmin_0_Rmax_2500_thresh_1
# }
#Env 1 rows: 
# 2 - CDA 0
env_1['CDA'][0] = {
    "background":
    {
        "ZIRP:Rmin_1000_Rmax_2000_thresh_.4": 0.507,
        "ZIRP:Rmin_0_Rmax_2500_thresh_.4": 0.493
    }
}

env_1['CDA'][0] = {
    0.507: profiles['2000_ddagger'],
    0.493: profiles['2500_circle'],
}
# 3 - 2M 0
env_1['2M'][0] = {
    1.0: profiles['2500_circle'],
}
# 7 - 2M 100
env_1['2M'][100] = {
0.602: profiles['1000_ddagger'],
0.239: profiles['2000_ddagger'],
0.159: profiles['2500_circle'],
}
# 8 - 2M LA 100
env_1['2M LA'][100] = {
0.237: profiles['1000_ddagger'],
0.537: profiles['2000_ddagger'],
0.226: profiles['2500_circle'],
}
# 10 - 2M 200
env_1['2M'][200] = {
0.381: profiles['1000_ddagger'],
0.338: profiles['2000_ddagger'],
0.281: profiles['2500_circle'],
}
# 11 - 2M LA 200
env_1['2M LA'][200] = {
0.679: profiles['2000_ddagger'],
0.321: profiles['2500_circle'],
}
# 14 - 2M 300
env_1['2M'][300] = {
0.692: profiles['1000_ddagger'],
0.036: profiles['2000_ddagger'],
0.272: profiles['2500_circle'],
}
# 15 - 2M LA 300
env_1['2M LA'][300] = {
0.655: profiles['2000_ddagger'],
0.345: profiles['2500_circle'],
}
# 19 - 2M 400
env_1['2M'][400] = {
0.595: profiles['2000_ddagger'],
0.405: profiles['2500_circle'],
}
# 20 - 2M LA 400
env_1['2M LA'][400] = {
0.470: profiles['1000_ddagger'],
0.258: profiles['2000_ddagger'],
0.272: profiles['2500_circle'],
}
# 25 - 2M 600
env_1['2M'][600] = {
0.810: profiles['1000_ddagger'],
0.190: profiles['2500_circle'],
}
# 26 - 2M LA 600
env_1['2M LA'][600] = {
0.029: profiles['1000_dstar'],
0.971: profiles['2500_circle'],
}
# 32 - 2M 700
env_1['2M'][700] = {
0.739: profiles['1000_ddagger'],
0.261: profiles['2500_circle'],
}
# 33 - 2M LA 700
env_1['2M LA'][700] = {
0.006: profiles['1000_ddagger'],
0.826: profiles['2000_ddagger'],
0.168: profiles['2500_circle'],
}
# 36 - 2M 900
env_1['2M'][900] = {
1.0:   profiles['2500_circle'],
}
# 39 - 2M LA 900
env_1['2M LA'][900] = {
0.131: profiles['1000_ddagger'],
0.869: profiles['2500_circle'],
}

environments['1'] = env_1

env_2 = {}
env_2['CDA'] = {}
env_2['2M'] = {}
env_2['2M LA'] = {}

env_2['CDA'][0] = {
    0.659: profiles['2500_circle'],
    0.341: profiles['2500'],
}

env_2['2M'][0] = {
    0.146: profiles['125'],
    0.854: profiles['2500_circle'],
}

# - 2M 50
env_2['2M'][50] = {
0.162: profiles['250'],
0.838: profiles['2500_circle'],
}

# - 2M LA 50
env_2['2M LA'][50] = {
0.188: profiles['500'],
0.812: profiles['2500_circle'],
}

# - 2M 100
env_2['2M'][100] = {
0.051: profiles['125'],
0.76: profiles['2500_circle'],
0.189: profiles['2500'],
}

# - 2M LA 100
env_2['2M LA'][100] = {
0.233: profiles['2000_ddagger'],
0.767: profiles['2500_circle'],
}

environments['2'] = env_2

# profiles = {
#     '125': ZIR_profile({'R_min': 0, 'R_max': 125, 'eta': 1}), ZIRP:Rmin_0_Rmax_125_thresh_1
#     '250': ZIR_profile({'R_min': 0, 'R_max': 250, 'eta': 1}), ZIRP:Rmin_0_Rmax_250_thresh_1
#     '500': ZIR_profile({'R_min': 0, 'R_max': 500, 'eta': 1}), ZIRP:Rmin_0_Rmax_500_thresh_1
#     '500_dstar': ZIR_profile({'R_min': 250, 'R_max': 500, 'eta': 1}), ZIRP:Rmin_250_Rmax_500_thresh_1
#     '1000': ZIR_profile({'R_min': 0, 'R_max': 1000, 'eta': 1}), ZIRP:Rmin_0_Rmax_1000_thresh_1
#     '1000_ddagger': ZIR_profile({'R_min': 500, 'R_max': 1000, 'eta': 0.4}), ZIRP:Rmin_500_Rmax_1000_thresh_.4
#     '1000_dstar': ZIR_profile({'R_min': 500, 'R_max': 1000, 'eta': 1}), ZIRP:Rmin_500_Rmax_1000_thresh_1
#     '1500_dagger': ZIR_profile({'R_min': 0, 'R_max': 1500, 'eta': 0.6}), ZIRP:Rmin_0_Rmax_1500_thresh_.6
#     '2000_ddagger': ZIR_profile({'R_min': 1000, 'R_max': 2000, 'eta': 0.4}), ZIRP:Rmin_1000_Rmax_2000_thresh_.4
#     '2500_circle': ZIR_profile({'R_min': 0, 'R_max': 2500, 'eta': 0.4}), ZIRP:Rmin_0_Rmax_2500_thresh_.4
#     '2500': ZIR_profile({'R_min': 0, 'R_max': 2500, 'eta': 1}), ZIRP:Rmin_0_Rmax_2500_thresh_1
# }

env_3 = {}
env_3['CDA'] = {}
env_3['2M'] = {}
env_3['2M LA'] = {}

env_3['CDA'][0] = {
    0.248: profiles['2000_ddagger'],
    0.752: profiles['2500_circle'],
}

env_3['2M'][0] = {
    0.017: profiles['500'],
    0.004: profiles['2000_ddagger'],
    0.979: profiles['2500_circle'],
}

env_3['2M'][25] = {
    0.854: profiles['2500_circle'],
    0.146: profiles['2500'],
}

env_3['2M LA'][25] = {
    0.21: profiles['2000_ddagger'],
    0.79: profiles['2500_circle'],
}

env_3['2M'][50] = {
    0.948: profiles['2500_circle'],
    0.052: profiles['2500'],
}

env_3['2M LA'][50] = {
    0.065: profiles['1500_dagger'],
    0.043: profiles['2000_ddagger'],
    0.892: profiles['2500_circle'],
}

env_3['2M'][75] = {
    0.823: profiles['2500_circle'],
    0.177: profiles['2500'],
}

env_3['2M LA'][75] = {
    0.142: profiles['2000_ddagger'],
    0.858: profiles['2500_circle'],
}

env_3['2M'][100] = {
    0.839: profiles['2500_circle'],
    0.161: profiles['2500'],
}

env_3['2M LA'][100] = {
    0.015: profiles['500'],
    0.231: profiles['2000_ddagger'],
    0.754: profiles['2500_circle'],
}

environments['3'] = env_3


### Test code
env_test = {}
env_test['CDA'] = {}
env_test['CDA'][0] = {
    1.0: profiles['2500'],
}
environments['test'] = env_test

