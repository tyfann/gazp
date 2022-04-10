import nltk
from nltk import word_tokenize
import json
import jieba
from nltk.tokenize import WordPunctTokenizer, WhitespaceTokenizer
import re
import argparse
import os
from preprocess_csgsql import convert_single_query
from copy import copy
from tqdm import tqdm

os.chdir('..')


def no_value_tokenize(string):
    string = str(string)
    string = string.replace("\'", "\"")
    string = re.sub(r'".*?"', 'value', string)
    string = re.sub(r' [0-9]+', ' value', string)
    quote_idxs = [idx for idx, char in enumerate(string) if char == '"']
    assert len(quote_idxs) % 2 == 0, "Unexpected quote"

    # keep string value as token
    vals = {}
    for i in range(len(quote_idxs) - 1, -1, -2):
        qidx1 = quote_idxs[i - 1]
        qidx2 = quote_idxs[i]
        val = string[qidx1: qidx2 + 1]
        key = "__val_{}_{}__".format(qidx1, qidx2)
        string = string[:qidx1] + key + string[qidx2 + 1:]
        vals[key] = val

    toks = [word.lower() for word in WordPunctTokenizer().tokenize(string)]
    # replace with string value token
    for i in range(len(toks)):
        if toks[i] in vals:
            toks[i] = vals[toks[i]]

    return toks


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-C", "--path", default='./data/CSgSQL', help="Configuration (*.json).")

    args = parser.parse_args()
    path = args.path

    for k in ['train', 'dev']:

        with open(os.path.join(path, k + '.json')) as f:
            data = json.load(f)

        for raw_data in tqdm(data, desc='processing {}'.format(k)):
            query = re.sub(r'<.*?>', '', raw_data['query'])
            # raw_data['query'] = convert_single_query(query)
            # query = copy(raw_data['query'])
            raw_data['query_toks'] = query.split()
            raw_data['query_toks_no_value'] = no_value_tokenize(query)
            raw_data['question_toks'] = list(jieba.cut(raw_data['question']))

        with open(os.path.join(path, k + '.json'), 'w', encoding='utf-8') as f:
            f.write(json.dumps(data, indent=4, separators=(',', ': '), ensure_ascii=False))


if __name__ == '__main__':
    main()
