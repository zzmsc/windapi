# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 09:13:12 2019

@author: zzm
"""

import datetime
from WindPy import w
import pandas as pd

def df_eod_prices(timestr):
    w.start()
    w.isconnected()
    #timestr=input('tradedate')
    timey=timestr[0:4]
    timem=timestr[4:6]
    timed=timestr[6:8]
    date= datetime.datetime(int(timey), int(timem), int(timed))
    windds1=w.wset('SectorConstituent','date='+timestr+';sector=全部A股')
    datac=windds1.Data[1]
    #datat=['000001.SZ','000002.SZ']
    windds2=w.wss(datac, "pre_close,open,high,low,close,chg,pct_chg,volume,amt,adjfactor,vwap,trade_status","tradeDate="+timestr+";priceAdj=U;cycle=D")
    dc1={'Ticker':datac,'Date':[timestr]*len(datac),'PreClose':windds2.Data[0],'Open':windds2.Data[1],'High':windds2.Data[2],'Low':windds2.Data[3],'Close':windds2.Data[4],'Change':windds2.Data[5],'PctChg':windds2.Data[6],'Volume':windds2.Data[7],'Amount':windds2.Data[8],'AdjFactor':windds2.Data[9],'VWAP':windds2.Data[10],'TradeStatus':windds2.Data[11]}
    df=pd.DataFrame(dc1)
    return(df)
