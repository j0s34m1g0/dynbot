import time
from iqoptionapi.stable_api import IQ_Option
Iq=IQ_Option("cognito802@gmail.com","0lg4ch4v3z")
Iq.connect()
goal="EURUSD-OTC"
while True:
    print(Iq.get_server_timestamp())