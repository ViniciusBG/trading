from src.utils.data_engineering import StockDataManager

apple = StockDataManager("APPLE")

print(apple._base_path)
print(apple.conf)
apple.download_data()