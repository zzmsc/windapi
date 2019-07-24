# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 14:33:17 2019

@author: zzm
"""

import datetime
from WindPy import w
import pandas as pd
def suspend1(timestr):
    w.start() 
    w.isconnected()
    #timestr=input('tradedate')
    windds1=w.wset("tradesuspend","startdate="+timestr+";enddate="+timestr+";field=date,wind_code")
    dc1={'Ticker':windds1.Data[1],'Date':[timestr for i in range(len(windds1.Data[1]))]}
    df=pd.DataFrame(dc1)
    return(df)
