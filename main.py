import click

from src.data_engineering import load_data
from src.globals import *


@click.command()
@click.option('--ticker',default="APPLE")
@click.option('--train_predict',default="train")
def main(ticker,train_predict):
    load_data(ticker,train_predict)

if __name__=="__main__":
    main()
