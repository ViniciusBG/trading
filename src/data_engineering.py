import yfinance as yf
from omegaconf import OmegaConf
import pandas as pd
import os
import logging

from src.globals import *

logger = logging.getLogger(__name__)

def load_data(ticker, stage, train_predict="train"):

    # Creates the path to get the most updated
    path = f"data/{stage}/{ticker}/{train_predict}"
    last_path = os.listdir(path)[-1]
    full_path = os.path.join(path, last_path)
    logger.warning(f"Loading data from {full_path} ")

    # Reads the data
    data = pd.read_csv(full_path)

    return data


def download_data(ticker, train_predict="train"):
    logger.warning(f"Downloading data for {ticker}")

    # Loads the configuration file
    conf = OmegaConf.load(f"conf/{ticker}.yaml")
    stock = conf["ticker"]
    start_date = conf["start_date"]

    # Decides the dates based on the purpose of the run
    if train_predict == "train":
        end_date = conf["train_end_date"]
    elif train_predict == "predict":
        end_date = TODAY
    
    # Loads the data from yahoo finance
    df = yf.download(stock, start_date, end_date)
    df.columns = [col.lower() for col in df.columns]
    df = df.reset_index()
    
    # Defines the path do save the data
    directory = f"data/raw/{ticker}/{train_predict}/"
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
