import click

from src.data_engineering import load_data,create_base_dataframe
from src.feature_engineering import generate_stockstats_features
from src.globals import *


@click.command()
@click.option('--ticker',default="APPLE")
@click.option('--train_predict',default="train")
def main(ticker,train_predict):
    generate_stockstats_features(ticker)

if __name__=="__main__":
    main()
