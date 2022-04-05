# -*- ecoding: utf-8 -*-
# @ModuleName: data_prep_mt5
# @Function: 
# @Author: Yufan-tyf
# @Time: 2022/3/31 21:31

import os
import pandas as pd

os.chdir('..')


def prepare_translation_datasets(data_path):
    with open(os.path.join(data_path, "train.tgt"), "r", encoding="utf-8") as f:
        sql_text = f.readlines()
        sql_text = [text.strip("\n") for text in sql_text]

    with open(os.path.join(data_path, "train.src"), "r") as f:
        nl_text = f.readlines()
        nl_text = [text.strip("\n") for text in nl_text]

    data = []
    for sql, nl in zip(sql_text, nl_text):
        data.append(["translate sql to nl", sql, nl])
        data.append(["translate nl to sql", nl, sql])

    train_df = pd.DataFrame(data, columns=["prefix", "input_text", "target_text"])

    with open(os.path.join(data_path, "dev.tgt"), "r", encoding="utf-8") as f:
        sql_text = f.readlines()
        sql_text = [text.strip("\n") for text in sql_text]

    with open(os.path.join(data_path, "dev.src"), "r") as f:
        nl_text = f.readlines()
        nl_text = [text.strip("\n") for text in nl_text]

    data = []
    for sql, nl in zip(sql_text, nl_text):
        data.append(["translate sql to nl", sql, nl])
        data.append(["translate nl to sql", nl, sql])

    eval_df = pd.DataFrame(data, columns=["prefix", "input_text", "target_text"])

    return train_df, eval_df

if __name__ == '__main__':
    train_df, eval_df = prepare_translation_datasets("dataset_post/csgsql_sl")
    train_df.to_csv("dataset_post/csgsql_sl/train.tsv", sep="\t")
    eval_df.to_csv("dataset_post/csgsql_sl/eval.tsv", sep="\t")