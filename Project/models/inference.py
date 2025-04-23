
import json, pickle, numpy as np, pandas as pd, tensorflow as tf
from pathlib import Path
MODEL_PATH = Path(__file__).with_name("tx_model_lstm_model_thisone.keras")
COLS_PATH  = Path(__file__).with_name("feature_cols.json")
MEAN_PATH  = Path(__file__).with_name("mean.pkl")
STD_PATH   = Path(__file__).with_name("std.pkl")

def _load():
    model = tf.keras.models.load_model(MODEL_PATH, compile=False)
    cols  = json.load(open(COLS_PATH))
    mean  = pickle.load(open(MEAN_PATH, "rb"))
    std   = pickle.load(open(STD_PATH,  "rb"))
    return model, cols, mean, std
    
def predict(df_last_48h):
    model, cols, mean, std = _load()
    x = df_last_48h[cols].replace([np.inf, -np.inf], np.nan).fillna(0)
    x = ((x-mean)/std).values.astype("float32")[None, ...]
    return float(model(x)[0,0])
