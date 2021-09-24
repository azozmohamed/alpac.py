import alpaca_trade_api as tradeapi
import openpyxl
import time
kye = ''
sec = ''
url = "https://paper-api.alpaca.markets"
api = tradeapi.REST(kye, sec, url, api_version='v2')
# Get daily price data for AAPL over the last 5 trading days.
# ____________EXCEL_____________
excel = openpyxl.load_workbook(filename='alpac.xlsx')
sheet = excel.active
symbols = []
for s in sheet.iter_rows(values_only=True):
    for q in s:
        symbols.append(q)
for sy in symbols:
    symbol = sy
    minute = 5
    barset = api.get_barset(symbol, 'minute', limit=minute)
    aapl_bars = barset[symbol]
    # See how much AAPL moved in that timeframe.
    week_open = aapl_bars[0].o
    print('Market Opening Price:', week_open)
    week_close = aapl_bars[-1].c
    print('Market close Price:', week_close)
    percent_change = (week_close - week_open) / week_open * 100
    print('{} moved {}% over the last {} minute'.format(symbol, percent_change, minute))
    print("___________________________________________\n")
