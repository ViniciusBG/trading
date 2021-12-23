import yfinance as yf
from omegaconf import OmegaConf
import pandas as pd
import os
import logging

from src.globals import *

logger = logging.getLogger(__name__)

class StockDataManager():

    def __init__(self,ticker):

        self.ticker = ticker
        self._base_path = f"data/{ticker}/"
        self.conf = OmegaConf.load(f"conf/{ticker}.yaml")
        self.stock = self.conf["ticker"]
        self.start_date = self.conf["start_date"]
        self.end_date = self.conf["train_end_date"]

    
    def load_data(self,ticker, stage, train_predict="train"):

        # Creates the path to get the most updated
        path = f"data/{stage}/{ticker}/{train_predict}"
        last_path = os.listdir(path)[-1]
        full_path = os.path.join(path, last_path)
        logger.warning(f"Loading data from {full_path} ")

        # Reads the data
        data = pd.read_csv(full_path)

        return data


    def download_data(self, train_predict="train"):
        logger.warning(f"Downloading data for {self.ticker}")

        # Loads the configuration file
        #conf = OmegaConf.load(f"conf/{self.ticker}.yaml")
        stock = self.stock
        start_date = self.start_date

        # Decides the dates based on the purpose of the run
        if train_predict == "train":
            end_date = self.end_date
        elif train_predict == "predict":
            end_date = TODAY
        
        # Loads the data from yahoo finance
        df = yf.download(stock, start_date, end_date)
        df.columns = [col.lower() for col in df.columns]
        df = df.reset_index()
        
        # Defines the path do save the data
        directory = f"data/raw/{self.ticker}/{train_predict}/"
        if not os.path.exists(directory):
            os.makedirs(directory)

        df.to_csv(f"{directory}{TODAY}")
        logger.warning(f"Saving the data --> {directory} ")

        return df


    def create_base_dataframe(ticker, train_predict="train"):
        
        # Loads the conf file
        conf = OmegaConf.load(f"conf/{ticker}.yaml")
        start_date = conf["start_date"]

        if train_predict == "train":
            end_date = conf["train_end_date"]
        elif train_predict == "predict":
            end_date = TODAY

        # Generates a dataframe with all the days
        base_dataframe = pd.date_range(start=start_date, end=end_date)

        return base_dataframe


    def generate_target():
        pass
