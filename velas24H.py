from iqoptionapi.stable_api import IQ_Option
import pandas as pd
import numpy as np

Iq = IQ_Option("cognito802@gmail.com", "0lg4ch4v3z")
Iq.connect()
Iq.change_balance('PRACTICE')  # MODE: "PRACTICE"/"REAL"
divisa = 'EURUSD-OTC'
velas = Iq.get_candles(divisa, 60, 1000, Iq.get_server_timestamp())
all_candles = pd.DataFrame(velas)
all_candles['color'] = all_candles['open'] - all_candles['close']
all_candles['max-min'] = all_candles['max'] - all_candles['min']
all_candles['max-open'] = all_candles['open'] - all_candles['close']
all_candles['max-close'] = all_candles['open'] - all_candles['close']

print(all_candles)



print(all_candles)

