from stockstats import StockDataFrame
from omegaconf import OmegaConf
import pandas as pd

from src.data_engineering import load_data


def generate_stockstats_features(ticker, train_predict="train"):

    conf = OmegaConf.load(f"conf/{ticker}.yaml")

    features_to_generate = list(conf["stockstats_features"])

    data = load_data(ticker=ticker, train_predict=train_predict, stage="raw")

    stockstats_dataframe = StockDataFrame.retype(data)

    final_data = stockstats_dataframe[features_to_generate]
    print(final_data)
    return final_data
