import yfinance as yf
from omegaconf import OmegaConf
import pandas as pd
import os
import logging
from stockstats import StockDataFrame


from src.utils.defaults import *

logger = logging.getLogger(__name__)


class StockDataManager:
    def __init__(self, ticker):

        self.ticker = ticker
        self._base_path = f"data/{ticker}/"
        self.conf = OmegaConf.load(f"conf/{ticker}.yaml")
        self.stock = self.conf["ticker"]
        self.start_date = self.conf["start_date"]
        self.end_date = self.conf["train_end_date"]

    def download_data(self, train_predict="train"):

        logger.warning(f"Downloading data for {self.ticker}")

        # Decides the dates based on the purpose of the run
        end_date = self._train_or_predict(stage=train_predict)

        # Loads the data from yahoo finance
        df = yf.download(self.stock, self.start_date, end_date)
        df.columns = [col.lower() for col in df.columns]

        self._save_data(df=df, stage="raw", train_predict=train_predict)

        return df

    def _save_data(self,df,stage, train_predict):
        # Defines the path do save the data
        directory = f"{self._base_path}/{stage}/{train_predict}/"
        if not os.path.exists(directory):
            os.makedirs(directory)

        df.to_csv(f"{directory}{TODAY}")
        logger.warning(f"Saving the data --> {directory} ")

    def _load_data(self, stage, train_predict="train"):

        # Creates the path to get the most updated
        path = f"{self._base_path}/{stage}/{train_predict}"
        last_path = os.listdir(path)[-1]
        full_path = os.path.join(path, last_path)
        logger.warning(f"Loading data from {full_path} ")

        # Reads the data
        data = pd.read_csv(full_path)

        return data

    def _create_base_dataframe(ticker, train_predict="train"):

        # Loads the conf file
        end_date = self._train_or_predict(train_predict)
        # Generates a dataframe with all the days
        base_dataframe = pd.date_range(start=self.start_date, end=end_date)

        return base_dataframe

    def generate_target():
        pass

    def _train_or_predict(self, stage):
        """Defines the purpose of the data transformations.
        If the purpose is to train models, it will have a fix end date.
        If the purpose is a live prediction, it will get today's date

        Args:
            stage ([type]): [description]

        Returns:
            [type]: [description]
        """
        if stage == "train":
            end_date = self.end_date
        elif stage == "predict":
            end_date = TODAY

        return end_date
