#!/usr/bin/env python
import argparse
import json
import sys
import os
from os import path
import itertools
import WWW_model_configs
import WWW_trader_profiles
from pathlib import Path
import numpy as np
import multiprocessing
from functools import partial
import subprocess
import datetime

from numpy import random
# example call:
# python3 -u sample_WWW.py --num_samples=500 --directory=./my_dir 
parser = argparse.ArgumentParser(description='Sample player strategies for simulation spec files from a distribution of strategies by role.')
def get_parser():
    parser = argparse.ArgumentParser(
        description='Sample player strategies for simulation spec files from a distribution of strategies by role.',
        usage=f"python {__name__}.py",
    )
    parser.add_argument(
        '--num_samples', 
        type=int, 
        default=1, 
        help='The number of profile mixtures to run for.'
    )
    parser.add_argument(
        '--num_obs', 
        type=int, 
        default=1, 
        help='The number of simulations per mixture.'
    )
    parser.add_argument(
        '--processes', 
        type=int, 
        default=10, 
        help='The number of mixtures to run for in parallel.'
    )
    parser.add_argument(
        '--directory',
        type=Path,
        default=Path('./WWW/'),
        help='The directory to put all of the simulations in.'
    )
    parser.add_argument( 
        '--seed',
        type=int,
        default=0,
        help='The random seed.'
    )
    parser.add_argument(
        '--envs',
        type=str,
        default="A,B,C",
        help='The experiment environments to run for.'
    )
    return parser


# profile.json has:
# profile: a Python dictionary object from the entire profile.json file

def main(
    directory: Path,
    seed: int,
    envs: str,
    num_samples: int,
    processes: int,
    num_obs: int
):
    base_dir = Path(directory)
    envs = [i for i in envs.split(',')]
    rng = np.random.default_rng(seed=seed)
    dirs = []
    for env, simspec in WWW_model_configs.www_N66_noMM.items():
        if env not in envs:
            continue
        
        profiles = WWW_trader_profiles.N_66_noMM[env]
        for t, profile in profiles.items():
            role_counts = simspec['role_counts']
            t_spec = simspec.copy()
            t_spec['configuration']['simLength'] = t * 1_000

            # Create directory structure
            # e.g., if there are 100 samples, length 09-99 is 2
            # d means integer base 10
            # %02 means to pad the number with leading zeros up to length 2
            fmt = "%0" + str(len(str(num_samples - 1))) + "d"
            # iterates from 0 to num_samples - 1
            dir = base_dir / f'env{env}{t}_MM{t_spec["role_counts"]["marketMaker"]}'
            dirs.append(dir)
            for i in range(num_samples):
                # example: sim_dir = /my_output_dir/02
                sample_str = fmt % i
                sim_dir = dir / sample_str
                sim_dir.mkdir(exist_ok=True, parents=True)
                t_spec['assignment'] = sample_players(profile, role_counts, rng=rng)
                with open(path.join(sim_dir, 'simulation_spec.json'), 'w') as f:
                    # write out object simspec to output stream f
                    json.dump(t_spec, f)
    
    print(f"{datetime.datetime.now()} Finished saving run configs in {base_dir}. Kicking off simulations now.")
    for dir in dirs:
        run_simulations(base_dir=dir, processes=processes, num_obs=num_obs,)
    print(f"{datetime.datetime.now()} Finished simulations. Exiting.")

# profile is a dict object
# players is a list of how many players there are per role
def sample_players(profile, players, rng):
    assignment = {}
    # profile must contain a set of key-value pairs.
    # iterate over all key-value pairs in the dict object "profile"
    # role is the key, probs is the value
    for role, probs in profile.items():
        strats, probs = zip(*probs.items())
        assignment[role] = list(itertools.chain.from_iterable(
            itertools.repeat(x, y) for x, y
            in zip(strats, rng.multinomial(players[role], probs))))
    return assignment

def run_hft_sim(folder: Path, num_obs: int, script_dir: Path) -> None:
    """
    Equivalent to the following in command line: ./run-hft.sh "$folder" num_obs
    """
    cmd = [
        "./run-hft.sh",
        str(folder),
        str(num_obs),
    ]

    # print(f">> Starting {folder} ...", flush=True)
    print(f"{cmd[0]} {cmd[1]} {cmd[2]}", flush=True)
    result = subprocess.run(
        cmd,
        cwd=script_dir,                 # matches cd "$LOC" in your script
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    if result.returncode != 0:
        raise RuntimeError(
            f"Job failed for {folder}\n"
            f"STDOUT:\n{result.stdout}\n"
            f"STDERR:\n{result.stderr}"
        )

    print(f">> Finished {folder}", flush=True)


def run_simulations(
    base_dir: Path,
    processes: int,
    num_obs: int,
):
    script_dir = Path(__file__).resolve().parent

    folders = sorted(
        p for p in base_dir.iterdir()
        if p.is_dir() and p.name and p.name[0].isdigit()
    )

    if not folders:
        print(f"No matching folders found in {base_dir}", file=sys.stderr)
        sys.exit(1)

    with multiprocessing.Pool(processes=processes, maxtasksperchild=1) as pool:
        pool.map(
            partial(
                run_hft_sim,
                num_obs=num_obs,
                script_dir=script_dir,
            ),
            folders,
            chunksize=1,
        )

if __name__ == "__main__":
    main(**vars(get_parser().parse_args()))