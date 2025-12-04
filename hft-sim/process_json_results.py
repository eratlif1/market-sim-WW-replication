import json
import math
import numpy as np
import pandas as pd
import random
from pathlib import Path
import argparse
import glob
import matplotlib.pyplot as plt
import seaborn as sns
from numba import njit, prange
import datetime

from scipy import stats
from pathlib import Path
import scipy.stats as stats

def get_parser():
    parser = argparse.ArgumentParser(
        description="Simulates implementation of base Wah and Wellman (2016) market model.",
        usage=f"python {__name__}.py",
    )
    parser.add_argument(
        "--dir",
        type=Path,
        default=Path('./WWW'),
        help="Directory with different configuration outputs",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=Path('./WWW_processed/'),
        help="Output directory",
    )
    parser.add_argument(
        "--model",
        type=str,
        default='WWW',
        help="Model",
    )
    parser.add_argument(
        "--envs",
        type=str,
        default='A,B,C',
        help="Environments to process results from",
    )
    return parser

spreadString = "spreads_mean_markets"
spreadNbboString = "spreads_median_nbbo"
timeString = "exectime_mean"
tradeString = "trans_num"
laTradeString = "trans_laagent_num"
bgSurplusString = "surplus_sum_no_disc"
laProfitString = "profit_sum_hft"
spreadIfDefinedString = "mean_median_spread_not_inf_nan"
rmsString = "mean_rms_midquote_error_vs_estim_rt"
minShadeString = "mean_min_shade_vs_estim_rt"
fracString = "mean_fraction_estim_rt_in_spread"
inventoryString = "sum_absv_inventory_mm"
spreadsEarnedString = "total_spreads_earned_mm"
spreadProfitString = "sum_spread_profit_mm"
positioningProfitString = "sum_positioning_profit_mm"
bgArrivalsString = "background_arrivals"
mmProfitString = "profit_sum_marketmaker"

col_to_json = {
    "spread": spreadString,
    "nbboSpread": spreadNbboString,
    "executionTime": timeString,
    "numTrades": tradeString,
    # "mmTrades",
    # "welfare":, # BG + LA
    "bgSurplus": bgSurplusString,
    "laProfit": laProfitString,
    "mmProfit": mmProfitString,
    "spreadIfDef": spreadIfDefinedString,
    # "midquoteRmsVsEst": rmsString,
    # "minShade": minShadeString,
    # "fracEstInSpread": fracString,
    'laTrades': laTradeString,
    # "mmInventory": ,
    # "mmSpreadsEarned",
    # "mmSpreadProfit"
    # "mmPositioningProfit",
}
featureString = "features"

def main(
    dir: Path,
    out: Path,
    model: str,
    envs: str,
):
    envs = envs.split(',')
    model = str.upper(model)
    dfs = []
    out.mkdir(exist_ok=True, parents=True)

    dir = str(dir)
    print(dir)
    if model == 'WW':
        base_config = 'CDAnum'
        other_trader_type = 'la'
    elif model == 'WWW':
        base_config = 'env'
        other_trader_type = 'mm'
        
    for configFolder in glob.glob(f'{dir}/{base_config}*'):
        data = []
        configuration = configFolder.split('/')[-1]
        if model == 'WW':
            other_trader_num = int(configuration.split('_')[2].split('A')[1])
            CDAnum = int(configuration.split('_')[1])
            delta = int(configuration.split('delta')[1])
        elif model == 'WWW':
            other_trader_num = int(configuration.split('MM')[-1])
            delta = 0
            CDAnum = 1
            env = configuration.split('_')[0].split('v')[-1]
        
        if env[0] not in envs:
            print(f"Skipping env {env}")
            continue
        
        print(f"{datetime.datetime.now()} processing results from {configFolder}")
        
        mixtures = 0
        for runFolder in glob.glob(f'{configFolder}/*'):
            # print('runFolder', runFolder)
            mixture = int(runFolder.split('/')[-1])
            mixtures += 1
            runs = 0
            for fileName in glob.glob(f'{runFolder}/observation*.json'):
                #print('fileName', fileName)
                jsonObs = ''
                with open(fileName) as obsFile:
                    jsonObs = json.load(obsFile)

                d = {}
                for col, key in col_to_json.items():
                    if key == laTradeString:
                        if key in jsonObs[featureString]:
                            val = jsonObs[featureString][key]
                        else:
                            val = 0.0
                    else:
                        if key in jsonObs[featureString]:
                            val = jsonObs[featureString][key]
                        else:
                            val = None
                    if val == 'Infinity':
                        print(f"{key} value {val} in {fileName} results")
                        val = None
                    d[col] = val

                d['totalSurplus'] = d['bgSurplus'] + d[f'{other_trader_type}Profit']
                d['exch'] = CDAnum
                d[other_trader_type] = other_trader_num
                d['SIP_latency'] = delta
                d['mixture'] = mixture
                d['env'] = env
                data.append(d)
                runs += 1
        df = pd.DataFrame(data)
        dfs.append(df)

    df = pd.concat(dfs)
    df.sort_values(by='env', ascending=True, inplace=True)
    # NOTE: Current naming logic assumes num. of mixtures and runs are constant across configs
    out_path = out / f'{model}_{mixtures}x{runs}_simulation_results.parq'
    df.to_parquet(out_path)
    print(f"Saved output to {out_path}")
    # return df


if __name__ == "__main__":
    main(**vars(get_parser().parse_args()))