import akshare as ak
from datetime import datetime as dt
import pandas as pd
import mplfinance as mpf

today = dt.today().strftime("%Y%m%d")
df = ak.stock_zh_a_hist_tx(
    symbol="sz002475", start_date="20260301", end_date=today, adjust="qfq", timeout=10
)
# Rename to mplfinance expected column names
df = df.rename(columns={"amount": "volume"})
df["date"] = pd.to_datetime(df["date"])
df.set_index("date", inplace=True)
df.index.name = "date"

mpf.plot(df, type="candle", style="charles", volume=True)
mpf.plot(df, type="candle", style="charles", mav=(20, 60, 120), volume=True)    
