from alpha_vantage.timeseries import TimeSeries
import yfinance as yf
import json
import requests
import pandas as pd

def alpha_vantage():

    Key = "FAJXBY00QP7J7MGF"
    ts = TimeSeries(Key)
    aapl= ts.get_daily(symbol="AAPL")
    x = (aapl) #["2019-09-12"])
    print(x)


    # get as API_request in json().

    API_URL = "https://www.alphavantage.co/query"

    data = {
        "function": "TIME_SERIES_DAILY",
        "symbol": "IBM",
        "outputsize": "compact",
        "apikey": "FAJXBY00QP7J7MGF"
        }
    response = requests.get(API_URL, data)
    #print(response.json())

    #data = pd.DataFrame.from_dict(response_json['Time Series (Daily)'], orient= 'index').sort_index(axis=1)
    #data = data.rename(columns={ '1. open': 'Open', '2. high': 'High', '3. low': 'Low', '4. close': 'Close', '5. adjusted close': 'AdjClose', '6. volume': 'Volume'})
    #data = data[[ 'Open', 'High', 'Low', 'Close', 'AdjClose', 'Volume']]
    #data.tail() # check OK or not
