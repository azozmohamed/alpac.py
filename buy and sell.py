import alpaca_trade_api as tradeapi
import numpy as np
import time


key = "PKHLR865RN5X219RSVE2"
sec = "4fCQbuK0tzsW9TiFBZKfc1zMzMotimAVfsB9XTOg"
BASE_URL = 'https://paper-api.alpaca.markets'
api = tradeapi.REST(key_id=key, secret_key=sec, base_url=BASE_URL)



def get_data():
    # Returns a an numpy array of the closing prices of the past 5 minutes
    market_data = api.get_barset(symb, 'minute', limit=5)

    close_list = []
    for bar in market_data[symb]:
        close_list.append(bar.c)

    close_list = np.array(close_list, dtype=np.float64)

    return close_list


def buy(q, s):  # Returns nothing, makes call to buy stock
    api.submit_order(
        symbol=s,
        qty=q,
        side='sell',
        type='market',
        time_in_force='gtc'
    )


def sell(q, s):  # Returns nothing, makes call to sell stock
    api.submit_order(
        symbol=s,
        qty=q,
        side='sell',
        type='market',
        time_in_force='gtc'
    )


symb = 'AMZN'  # Ticker of stock you want to trade

pos_held = False

while True:
    print("")
    print("Checking Price")

    close_list = get_data()

    ma = np.mean(close_list)
    last_price = close_list[4]

    print("Moving Average: " + str(ma))
    print("Last Price: " + str(last_price))

    # Make buy/sell decision
    # This algorithm buys or sells when the moving average crosses the most recent closing price

    if ma + 0.1 < last_price and not pos_held:  # Buy when moving average is ten cents below the last price
        print("Buy")
        buy(1, symb)
        pos_held = True

    elif ma - 0.1 > last_price and pos_held:  # Sell when moving average is ten cents above the last price
        print("Sell")
        sell(1, symb)
        pos_held = False

    time.sleep(5)
