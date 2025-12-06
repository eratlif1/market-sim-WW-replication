#!/usr/bin/env python
import argparse
import json
import sys
import os
from os import path
import itertools
import WW_model_configs
import WW_trader_profiles
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
        default=Path('./WW/'),
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
        default="1,2,3",
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
    for env in envs:
        env_key = f'env_{env}'
        trader_profiles = convert_environments(WW_trader_profiles.environments, WW_trader_profiles.profiles)
        for key, simspec in WW_model_configs.environments[env].items():

            profiles = trader_profiles[env][key]
            for lat, profile in profiles.items():
                role_counts = simspec['role_counts']
                lat_spec = simspec.copy()
                lat_spec['configuration']['nbboLatency'] = lat

                # Create directory structure
                # iterates from 0 to num_samples - 1
                # e.g., if there are 100 samples, length 09-99 is 2
                fmt = "%0" + str(len(str(num_samples - 1))) + "d"
                dir = base_dir / env_key / f'CDA{lat_spec["configuration"]["CDA"]}_LA{lat_spec["role_counts"]["LA"]}_delta{lat}'
                dirs.append(dir)
                for i in range(num_samples):
                    # example: sim_dir = /my_output_dir/02
                    sample_str = fmt % i
                    sim_dir = dir / sample_str
                    sim_dir.mkdir(exist_ok=True, parents=True)
                    lat_spec['assignment'] = sample_players(profile, role_counts, rng=rng)
                    with open(path.join(sim_dir, 'simulation_spec.json'), 'w') as f:
                        # write out object simspec to output stream f
                        json.dump(lat_spec, f)
    
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

def convert_env(old_env, profiles):
    """
    Convert a single environment dict from {category: {index: {weight: profile_key_or_string}}}
    to {category: {index: {"background": {profile_string: weight}}}}
    """
    new_env = {}
    for category, indices in old_env.items():
        new_env[category] = {}
        for idx, weight_to_profile in indices.items():
            background = {}
            for weight, prof in weight_to_profile.items():
                # Resolve profile to its full string via profiles map if needed
                if isinstance(prof, str) and prof.startswith("ZIRP:"):
                    profile_str = prof
                elif isinstance(prof, str) and prof in profiles:
                    profile_str = profiles[prof]
                else:
                    raise ValueError(f"Unrecognized profile reference: {prof!r}")
                background[profile_str] = float(weight)
            new_env[category][idx] = {"background": background}
    return new_env


def convert_environments(old_environments, profiles, rename_fn=None):
    """
    Convert environment configs from replication-script format to format needed for MarketSim
    """
    if rename_fn is None:
        rename_fn = lambda k: k
    new_envs = {}
    for key, env in old_environments.items():
        new_key = rename_fn(key)
        new_envs[new_key] = convert_env(env, profiles)
    return new_envs

def run_hft_sim(folder: Path, num_obs: int, script_dir: Path) -> None:
    """
    Equivalent to: ./run-hft.sh "$folder" num_obs
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

    # Equivalent of oneE25A/[0-9]*
    folders = sorted(
        p for p in base_dir.iterdir()
        if p.is_dir() and p.name and p.name[0].isdigit()
    )

    if not folders:
        print(f"No matching folders found in {base_dir}", file=sys.stderr)
        sys.exit(1)

    with multiprocessing.Pool(processes=processes, maxtasksperchild=100) as pool:
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