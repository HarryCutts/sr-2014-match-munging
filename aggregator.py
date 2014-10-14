#!/usr/bin/env python3

import collections
import os
import yaml
import pickle

FILES_ROOT = './sr2014-comp/'
OUTPUT_FILE = 'sr2014.dat'

teams = collections.defaultdict(lambda: [])

def read_matches(dir_path):
    file_names = os.listdir(dir_path)
    for yaml_file in file_names:
        with open(os.path.join(dir_path, yaml_file)) as f:
            data = yaml.load(f)

        for team_tla, appearance in data['teams'].items():
            #if appearance['present'] and not appearance['disqualified']:
            teams[team_tla].append(appearance)

paths = [
        os.path.join(FILES_ROOT, 'league',   'A'),
        os.path.join(FILES_ROOT, 'league',   'B'),
        os.path.join(FILES_ROOT, 'knockout', 'A'),
        os.path.join(FILES_ROOT, 'knockout', 'B'),
        ]

for path in paths:
    read_matches(path)

with open(OUTPUT_FILE, 'wb') as output_file:
    print("Writing to",OUTPUT_FILE,"as pickled Python data.")
    pickle.dump(dict(teams), output_file)
