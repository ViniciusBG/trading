import yfinance as yf
from omegaconf import OmegaConf
import pandas as pd

from src.globals import *


def load_data(ticker,train_predict="train"):


    conf = OmegaConf.load(f'conf/{ticker}.yaml')

    stock = conf["ticker"]
    start_date = conf['start_date']

    if train_predict=="train":
        end_date = conf['train_end_date']
    elif train_predict=="predict":
        end_date= TODAY

    df = yf.download(stock,start_date, end_date)
    df.to_csv(f"data/{ticker}__{end_date}__{train_predict}")
    
    print(df)
    #return df
                
