# -*- ecoding: utf-8 -*-
# @ModuleName: train_mt5
# @Function: 
# @Author: Yufan-tyf
# @Time: 2022/3/31 21:42
import logging
import pandas as pd
from simpletransformers.t5 import T5Model, T5Args


logging.basicConfig(level=logging.INFO)
transformers_logger = logging.getLogger("transformers")
transformers_logger.setLevel(logging.WARNING)

train_df = pd.read_csv("dataset_post/csgsql_sl/train.tsv", sep="\t").astype(str)
eval_df = pd.read_csv("dataset_post/csgsql_sl/eval.tsv", sep="\t").astype(str)

train_df["prefix"] = ""
eval_df["prefix"] = ""

model_args = T5Args()
model_args.max_seq_length = 512
model_args.train_batch_size = 10
model_args.eval_batch_size = 10
model_args.num_train_epochs = 1
model_args.evaluate_during_training = True
model_args.evaluate_during_training_steps = 3000
model_args.use_multiprocessing = False
model_args.fp16 = False
model_args.save_steps = -1
model_args.save_eval_checkpoints = False
model_args.no_cache = True
model_args.reprocess_input_data = True
model_args.overwrite_output_dir = True
model_args.preprocess_inputs = False
model_args.num_return_sequences = 1

model = T5Model("mt5", "google/mt5-small", args=model_args)

# Train the model
model.train_model(train_df, eval_data=eval_df)

# Optional: Evaluate the model. We'll test it properly anyway.
results = model.eval_model(eval_df, verbose=True)