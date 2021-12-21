from stockstats import StockDataFrame
from omegaconf import OmegaConf


def generate_stockstats_features(ticker):

    conf = OmegaConf.load(f'conf/{ticker}.yaml')

    features_to_generate = conf['stockstats_features']

    stock_df = StockDataFrame.retype(df)

    df = df[features_to_generate]

    print(features_to_generate)




