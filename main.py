import time
import pandas as pd
from iqoptionapi.stable_api import IQ_Option


def run():
    while True:
        Iq = IQ_Option("cognito802@gmail.com", "0lg4ch4v3z")
        Iq.connect()
        Iq.change_balance('PRACTICE')  # MODE: "PRACTICE"/"REAL"
        all_assets = pd.DataFrame(Iq.get_all_open_time())
        divisasTB = all_assets.loc[:, ['binary', 'turbo']]
        divisasTB = divisasTB.dropna()
        divisasActivas = divisasTB.loc[:, ['turbo']] == [{'open': True}]
        div = divisasActivas.to_dict('dict')
        div = list(div.values())
        div = dict(div[0])        
        f = open ('master.txt','w')
        for i in div:
            if div[i] == True:
                f.write(i + '\n')        
        f.close()
        time.sleep(150)


if __name__ == '__main__':
    run()
