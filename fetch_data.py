import yfinance as yf

aapl = yf.Ticker("AAPL")
period = input("Period: ")

hist = aapl.history(period=period)

print(hist)

