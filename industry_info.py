# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 12:42:08 2019

@author: zzm
"""

import datetime
from WindPy import w
import pandas as pd

def industry_info(timestr):
    w.start()
    w.isconnected()
    #timestr=input('tradedate')
    datac=[]
    for i in range(49,58):
        windds1=w.wset("sectorconstituent","date="+timestr+";sectorid=b10"+chr(i)+"000000000000;field=wind_code")
        datac=datac+windds1.Data[0]
    for i in range(97,117):
        windds1=w.wset("sectorconstituent","date="+timestr+";sectorid=b10"+chr(i)+"000000000000;field=wind_code")
        datac=datac+windds1.Data[0]
    windds1=w.wss(datac, "industry_citiccode","tradeDate="+timestr+";industryType=3")
    dc={'Ticker':windds1.Codes,'industry_citiccode':windds1.Data[0]}
    df=pd.DataFrame(dc)
    return(df)
   