#%%
from stockstats import StockDataFrame
from datetime import datetime
import matplotlib.pyplot as plt


from utils import globals
# %%

#%%

# %%
stock_df = StockDataFrame.retype(df)
stock_df
# %%
stock_df[["change", "rate", "close_-1_d", "log-ret"]]

# %% 
SELECTED_COLUMNS = ['close']
test_df = df[SELECTED_COLUMNS]
# %%
teste_df_stock = StockDataFrame.retype(test_df)
# %%
teste_df_stock[["change", "rate", "close_-1_d", "log-ret"]]

# %%
teste_df_stock[["close_10_sma"]].tail()
#%%
teste_df_stock[["close", "close_10_sma", "close_50_sma"]].plot(title="SMA example");
# %%
teste_df_stock["rsi_12"]
# %%
teste_df_stock["macd"].plot()

# %%
teste_df_stock[["change","close","close_200_ema", "close_30_sma", "close_50_sma","macd","rsi_12"]].plot(title="SMA example");

#%%
teste_df_stock['change'].plot()

# %%
teste_df_stock[['change','close']].plot()

# %%
print(len(teste_df_stock[teste_df_stock['change']>0]))
print(len(teste_df_stock[teste_df_stock['change']<0]))

# %%
from hyperopt import fmin, tpe, hp
best = fmin(fn=lambda x: x * 5 + x**5,
    space=hp.uniform('x', -4, 10),
    algo=tpe.suggest,
    max_evals=100)
print (best)
# %%
