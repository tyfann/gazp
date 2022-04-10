# -*- ecoding: utf-8 -*-
# @ModuleName: preprocess_csgsql
# @Function: 
# @Author: Yufan-tyf
# @Time: 2022/4/2 14:21

import json
import os
import argparse
import sys
sys.path.append('..')
from copy import copy
from tqdm import tqdm
import re

# os.chdir('..')


def convert_query():
    parser = argparse.ArgumentParser()
    parser.add_argument("-C", "--path", default='./data/csgsql', help="Configuration (*.json).")
    args = parser.parse_args()

    path = args.path

    # for k in ['train', 'dev']:
    for k in ['train']:
        file = os.path.join(path, k + '.json')
        with open(file) as f:
            data = json.load(f)

        for sentence in data:
            query = copy(sentence['query'])
            query_tokens = query.split()

            AS_index = [i for i, x in enumerate(query_tokens) if x == 'AS']
            alias_to_table = {}
            # for index in AS_index:
            #     # {'TOWER_BASIC': 'T1'}
            #     alias_to_table[query_tokens[index-1]] = query_tokens[index+1]

            while 'AS' in query_tokens:
                index = query_tokens.index('AS')
                # {'T1': 'TOWER_BASIC'}
                alias_to_table[query_tokens[index + 1]] = query_tokens[index - 1]
                query_tokens.remove(query_tokens[index + 1])
                query_tokens.remove(query_tokens[index])

            seq = ' '
            query_new = seq.join(query_tokens)
            for key in alias_to_table:
                query_new = query_new.replace(key, alias_to_table[key])
            sentence['query'] = query_new


def convert_single_query(query):
    query_tokens = query.split()

    # AS_index = [i for i, x in enumerate(query_tokens) if x == 'AS']
    alias_to_table = {}

    while 'AS' in query_tokens:
        index = query_tokens.index('AS')
        # {'T1': 'TOWER_BASIC'}
        alias_to_table[query_tokens[index + 1]] = query_tokens[index - 1]
        query_tokens.remove(query_tokens[index + 1])
        query_tokens.remove(query_tokens[index])

    seq = ' '
    query_new = seq.join(query_tokens)
    for key in alias_to_table:
        query_new = query_new.replace(key, alias_to_table[key])
    return query_new


if __name__ == '__main__':
    convert_query()
