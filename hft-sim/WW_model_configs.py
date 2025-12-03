def base_config(env, cda_str='num_2', background=238, LA=1):
    if env == 1:
        N = 24
        lam = 0.05
        kappa = 0.05
        T = 15_000
    elif env == 2:
        N = 238
        lam = 0.005
        kappa = 0.02
        T = 10_000
    elif env == 3:
        N = 58
        lam = 0.005
        kappa = 0.02
        T = 5_000
    return {
        'configuration': {
            # "randomSeed": 271828,
            'simLength': T, # length of simulation - SIMULATION_LENGTH
            'CDA': cda_str, # Number of stock exchanges - 
            'meanValue': 100_000, # mean fundamental value of security
            'fundamentalMean': 100_000, # mean fundamental value of security - FUNDAMENTAL_MEAN
            'fundamentalKappa': kappa, # strength of mean reversion for security's fundamental value - FUNDAMENTAL_KAPPA
            'fundamentalShockVar': 5_000_000, # variance of random shock to security fundamental value - FUNDAMENTAL_SHOCK_VAR
            'privateValueVar': 5_000_000, # variance of ZI private valuations - PRIVATE_VALUE_VAR
            'alpha': 0.001, # threshold from which the LA agent determines whether an opportunity is worth pursuing - ALPHA
            'maxPosition': 10, # max quantity ZI agent can be long or short - MAX_POSITION
            "backgroundReentryRate": lam, # Poisson arrival rate for ZI agents - BACKGROUND_REENTRY_RATE
            "reentryRate": lam, # Poisson arrival rate for agents - REENTRY_RATE
            "arrivalRate": lam, # Rate of initial arrival of agents - ARRIVAL_RATE
        },
        'role_counts': {
            'background': N, # Number of background traders
            'LA': LA, # Number of latency arbitrageurs
        }
    }

env_1 = {}
env_1_2ex_1LA = base_config(1, cda_str='num_2', LA=1)

env_1_2ex = base_config(1, cda_str='num_2', LA=0)

env_1_1ex = base_config(1, cda_str='num_1', LA=0)

env_1['CDA'] = env_1_1ex
env_1['2M'] = env_1_2ex
env_1['2M LA'] = env_1_2ex_1LA


env_2 = {}
env_2_2ex_1LA = base_config(2, cda_str='num_2', LA=1)

env_2_2ex = base_config(2, cda_str='num_2', LA=0)

env_2_1ex = base_config(2, cda_str='num_1', LA=0)

env_2['CDA'] = env_2_1ex
env_2['2M'] = env_2_2ex
env_2['2M LA'] = env_2_2ex_1LA


env_3 = {}
env_3_2ex_1LA = base_config(3, cda_str='num_2', LA=1)

env_3_2ex = base_config(3, cda_str='num_2', LA=0)

env_3_1ex = base_config(3, cda_str='num_1', LA=0)

env_3['CDA'] = env_3_1ex
env_3['2M'] = env_3_2ex
env_3['2M LA'] = env_3_2ex_1LA


environments = {}

env_test = {}
env_test['CDA'] = env_1_1ex

environments['env_1'] = env_1
environments['env_2'] = env_2
environments['env_3'] = env_3
environments['env_test'] = env_test