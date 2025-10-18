#! /usr/bin/env python3
import yfinance as yf

# 获取股票数据
symbol = "600519.SS"
start_date = "2025-01-01"
end_date = "2025-06-01"

data = yf.download(symbol, start=start_date, end=end_date,threads=False, proxy="http://127.0.0.1:7890")
print(data.head())


