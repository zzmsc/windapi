# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 09:48:19 2019

@author: zzm
"""

from WindPy import w
import pandas as pd
import tushare as ts
def AShareDescription(timestr):
    w.start()
    w.isconnected()
    windds1=w.wset('SectorConstituent','date='+timestr+';sector=已摘牌股票')
    data1=windds1.Data[1]
    windds4=w.wset('SectorConstituent','date='+timestr+';sector=全部A股')
    data4=windds4.Data[1]
    data1=data4+data1
    windds2=w.wsd(data1, "ipo_date")
    windds3=w.wsd(data1, "delist_date")
    data2=windds2.Data[0]
    d2=[]
    for i in range(len(data2)):
        d2.append(str(data2[i])[0:4]+str(data2[i])[5:7]+str(data2[i])[8:10])
    d3=[]
    data3=windds3.Data[0]
    for i in range(len(data3)):
        d3.append(str(data2[i])[0:4]+str(data2[i])[5:7]+str(data2[i])[8:10])
    data={'Ticker':data1,'ListDate':d2,'DeListDate':d3}
    df=pd.DataFrame(data)
    return(df)

