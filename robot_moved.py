#!/usr/bin/env python3

import pickle
from fractions import Fraction

from stats_per_match import stats_per_match

with open('sr2014.dat', 'rb') as data_file:
    teams = pickle.load(data_file)

stats_per_match(teams, lambda a: a['robot_moved'])
