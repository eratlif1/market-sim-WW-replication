
def base_config(env, background=24, mm=0, T_base=1):
    pv_var = 5_000_000
    if env == "A":
        bg_rate = 0.0005
        shock_var = 1_000_000
    elif env == "B":
        bg_rate = 0.005
        shock_var = 1_000_000
    elif env == "C":
        bg_rate = 0.005
        shock_var = 500_000
    return {
        'configuration': {
            # "randomSeed": 271828,
            'simLength': T_base * 1_000, # length of simulation - SIMULATION_LENGTH
            'CDA': 'num_1', # Number of stock exchanges - 
            'meanValue': 100_000, # mean fundamental value of security
            'fundamentalMean': 100_000, # mean fundamental value of security - FUNDAMENTAL_MEAN
            'fundamentalKappa': 0.05, # strength of mean reversion for security's fundamental value - FUNDAMENTAL_KAPPA
            'fundamentalShockVar': shock_var, # variance of random shock to security fundamental value - FUNDAMENTAL_SHOCK_VAR
            'privateValueVar': pv_var, # variance of ZI private valuations - PRIVATE_VALUE_VAR
            # 'alpha': 0.001, # threshold from which the LA agent determines whether an opportunity is worth pursuing - ALPHA
            'maxPosition': 10, # max quantity ZI agent can be long or short - MAX_POSITION
            "backgroundReentryRate": bg_rate, # Poisson arrival rate for ZI agents - BACKGROUND_REENTRY_RATE
            "reentryRate": bg_rate, # Poisson arrival rate for agents - REENTRY_RATE
            "arrivalRate": bg_rate, # Rate of initial arrival of agents - ARRIVAL_RATE
        },
        'role_counts': {
            'background': background, # Number of background traders
            # 'LA': LA, # Number of latency arbitrageurs
            "marketMaker": mm,
        }
    }

environments = {}

www_N66_noMM = {}
A = base_config('A', background=66, T_base=1)
B = base_config('B', background=66, T_base=1)
C = base_config('C', background=66, T_base=1)

www_N66_noMM['A'] = A
www_N66_noMM['B'] = B
www_N66_noMM['C'] = C


