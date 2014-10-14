#!/usr/bin/env python3

import pickle
from fractions import Fraction

from binomial import probability_mass

def stats_per_match(teams, predicate):
    teams_fraction_true = []

    for team_tla, appearances in teams.items():
        num_true = [predicate(appearance) for appearance in appearances].count(True)
        fraction_true = Fraction(num_true, len(appearances))
        teams_fraction_true.append(fraction_true)
        print(team_tla,": ",float(fraction_true) * 100,"%")

    mean = float(sum(teams_fraction_true) / len(teams_fraction_true))
    print("Mean percentage:", mean * 100)

    print("Percentage probability for a number of robots in a match:")
    for i in range(5):
        print(i, '\t', probability_mass(k=i, n=4, p=mean) * 100)
