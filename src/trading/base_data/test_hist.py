import akshare as ak
from datetime import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

today = dt.today().strftime("%Y%m%d")
df = ak.stock_zh_a_hist(
    symbol="002475", period="daily", start_date="20250101", end_date=today, adjust="qfq"
)
df = df.iloc[:, 0:7].drop(df.columns[1], axis=1)
print(df.head())


df.columns = ["date", "open", "close", "high", "low", "volume"]
df.date = pd.to_datetime(df.date)
df.set_index("date", inplace=True)
print(df.head())

# mpf.plot(df, type="candle", style="charles", volume=True)
# mpf.plot(df, type="candle", style="charles", mav=(20, 60, 120), volume=True)    


dx = ak.stock_zh_a_spot_em()
print(dx.head())
 