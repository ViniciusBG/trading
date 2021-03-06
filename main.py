import click

from src.utils.data_engineering import download_data, load_data, create_base_dataframe
from src.utils.feature_engineering import generate_stockstats_features
from src.utils.globals import *


@click.command()
@click.option("--ticker", default="APPLE")
@click.option("--train_predict", default="train")
# @click.option('--stage',default="raw")
def main(ticker, train_predict):
    download_data(ticker=ticker, train_predict=train_predict)

    generate_stockstats_features(
        ticker=ticker,
        train_predict=train_predict,
    )


if __name__ == "__main__":
    main()
