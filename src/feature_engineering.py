import yfinance as yf
from omegaconf import OmegaConf
import pandas as pd
import os
import logging
from stockstats import StockDataFrame

from src.globals import *

logger = logging.getLogger(__name__)

from src.data_engineering import StockDataManager

logger = logging.getLogger(__name__)

class FeatureEngineering(StockDataManager):
    def __init__(self, ticker):
        super().__init__(ticker)
        

    def generate_stockstats_features(ticker, train_predict="train"):
        pass
        # # Loads the configs from the conf file
        # conf = OmegaConf.load(f"conf/{ticker}.yaml")
        # features_to_generate = list(conf["stockstats_features"])

        # # Loads data from raw layer
        # data = load_data(ticker=ticker, train_predict=train_predict, stage="raw")

        # # Creates the trading features
        # stockstats_dataframe = StockDataFrame.retype(data)
        # final_data = stockstats_dataframe[features_to_generate]
        # logger.warning("Generating features with stockstats")
        # logger.warning(f"Chosen features --> {features_to_generate}")

        # return final_data
