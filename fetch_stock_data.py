import yfinance as yf
from datetime import datetime

# Define the stock symbol and date range
symbol = "AAPL"
start_date = "2023-01-01"
end_date = "2023-01-31"

# Fetch the data
df = yf.download(symbol, start=start_date, end=end_date, progress=False)

# Save to CSV
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"{symbol}_stock_data_{timestamp}.csv"
df.to_csv(filename)

print(f"Saved {symbol} data to {filename}")
