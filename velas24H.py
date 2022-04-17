from iqoptionapi.stable_api import IQ_Option
import pandas as pd
import numpy as np
import datetime
import time


Iq = IQ_Option("cognito802@gmail.com", "0lg4ch4v3z")
Iq.connect()
Iq.change_balance('PRACTICE')  # MODE: "PRACTICE"/"REAL"
divisa = 'GBPUSD-OTC'
velas = Iq.get_candles(divisa, 60, 1000, Iq.get_server_timestamp())
timeVela = time.strftime('%H:%M', time.localtime(velas[0]['from']))
candles = []
for i in range(len(velas)):
    openn = velas[i]['open']
    close = velas[i]['close']
    max = velas[i]['max']
    min = velas[i]['min']
    hora = time.strftime('%H:%M', time.localtime(velas[i]['from']))
    if openn - close > 0:
        color = 'rojo'
        total = max - min
        total2 = 100
        mecha_arriba = max - openn
        mecha_arriba2 = round(((max - openn)*100)/(max - min))
        cuerpo = openn - close
        cuerpo2 = round(((openn - close)*100)/(max - min))
        mecha_abajo = close - min
        mecha_abajo2 = round(((close - min)*100)/(max - min))        
    elif openn - close < 0 :
        color = 'verde'
        total = max - min
        total2 = 100
        mecha_arriba = max - close
        mecha_arriba2 = round(((max - close)*100)/(max - min))
        cuerpo = close - openn
        cuerpo2 = round(((close - openn)*100)/(max - min))
        mecha_abajo = openn - min 
        mecha_abajo2 = round(((openn - min)*100)/(max - min))  
    else:
        color = 'blanco'
        total = max - min
        total2 = 100
        mecha_arriba = max - openn
        mecha_arriba2 = round(((max - openn)*100)/(max - min))
        cuerpo = 0
        cuerpo2 = 0
        mecha_abajo = openn - min
        mecha_abajo2 = round(((openn - min)*100)/(max - min))
    candles.append([{'hora': hora
                     , 'color': color
                     , 'total': total
                     , 'total2': total2
                     , 'mecha_arriba': mecha_arriba
                     , 'mecha_arriba2': mecha_arriba2
                     , 'cuerpo': cuerpo
                     , 'cuerpo2': cuerpo2
                     , 'mecha_abajo':mecha_abajo
                     , 'mecha_abajo2': mecha_abajo2}])
f = open (divisa+'.txt','w')
for i in candles:
    f.write(str(i) + '\n')        
f.close()
    #print(str(hora), str(color)
        #  , '|| ' + str(total) + ' |', str(total2) + ' ||'
        #  , '|| ' + str(mecha_arriba) + ' |', str(mecha_arriba2) + ' ||'
        #  , '|| ' + str(cuerpo) + ' |', str(cuerpo2) + ' ||'
        #  , '|| ' + str(mecha_abajo) + ' |', str(mecha_abajo2) + ' ||')***
        


