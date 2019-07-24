# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 16:02:11 2019

@author: zzm
"""

import datetime
from WindPy import w
import pandas as pd
def trade_days(timestr):
    w.start() 
    w.isconnected()
    windds=w.tdays("1990-12-03", timestr, "")
    type(str(windds.Times[0])[0:4]+str(windds.Times[0])[5:7]+str(windds.Times[0])[8:10])
    T=['19901203','19901204','19901205','19901206','19901207','19901210','19901211','19901212','19901213','19901214','19901217','19901218']
    for i in range(len(windds.Times)):
        T.append(str(windds.Times[i])[0:4]+str(windds.Times[i])[5:7]+str(windds.Times[i])[8:10])
    dc={'TradeDay':T}
    df=pd.DataFrame(dc)
    return(df)
