#!/usr/bin/env python3

import pickle
from fractions import Fraction

from stats_per_match import stats_per_match

with open('sr2014.dat', 'rb') as data_file:
    teams = pickle.load(data_file)

def has_moved_token(appearance):
    return (any(num > 0 for num in appearance['zone_tokens'].values())
         or any(num > 0 for num in appearance['slot_bottoms'].values()))

stats_per_match(teams, has_moved_token)
