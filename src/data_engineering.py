import yfinance as yf
from omegaconf import OmegaConf
import pandas as pd
import os

from src.globals import *


def load_data(ticker, stage, train_predict="train"):

    # Creates the path to get the most updated
    path = f"data/{stage}/{ticker}/{train_predict}"
    last_path = os.listdir(path)[-1]
    full_path = os.path.join(path, last_path)

    # Reads the data
    data = pd.read_csv(full_path)

    print(data)
    return data


def download_data(ticker, train_predict="train"):

    conf = OmegaConf.load(f"conf/{ticker}.yaml")

    stock = conf["ticker"]
    start_date = conf["start_date"]

    if train_predict == "train":
        end_date = conf["train_end_date"]
    elif train_predict == "predict":
        end_date = TODAY

    df = yf.download(stock, start_date, end_date)

    df.columns = [col.lower() for col in df.columns]
    df = df.reset_index()

    directory = f"data/raw/{ticker}/{train_predict}/"
    if not os.path.exists(directory):
        os.makedirs(directory)

    df.to_csv(f"{directory}{TODAY}")

    return df


def create_base_dataframe(ticker, train_predict="train"):

    conf = OmegaConf.load(f"conf/{ticker}.yaml")

    start_date = conf["start_date"]

    if train_predict == "train":
        end_date = conf["train_end_date"]
    elif train_predict == "predict":
        end_date = TODAY

    base_dataframe = pd.date_range(start=start_date, end=end_date)

    print(base_dataframe)


def generate_target():
    pass
