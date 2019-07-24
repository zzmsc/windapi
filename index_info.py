# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 10:19:30 2019

@author: zzm
"""

import datetime
from WindPy import w
import pandas as pd

def index_info(timestr):
    w.start()
    w.isconnected()
    #timestr=input('tradedate')
    timey=timestr[0:4]
    timem=timestr[4:6]
    timed=timestr[6:8]
    date= datetime.datetime(int(timey), int(timem), int(timed))
    windds1=w.wset("indexhistory","startdate=2001-01-01;enddate="+timestr+";windcode=000300.SH;field=tradedate,tradecode,tradestatus")
    dc1={'tradedate':windds1.Data[0],'tradecode':windds1.Data[1],'tradestatus':windds1.Data[2]}
    df1=pd.DataFrame(dc1)
    df1=df1.sort_index(axis=0,by=['tradecode','tradedate'],ascending=True)
    df1=df1.reset_index(drop=True)
    i=0
    df=pd.DataFrame({},columns=['Ticker','EntryDate','RemoveDate'])
    while(i<len(df1)):
        if(df1.loc[i,'tradecode']==df1.loc[i+1,'tradecode']):
            dc={'Ticker':df1.loc[i,'tradecode'],'EntryDate':str(df1.loc[i,'tradedate'])[0:4]+str(df1.loc[i,'tradedate'])[5:7]+str(df1.loc[i,'tradedate'])[8:10],'RemoveDate':str(df1.loc[i+1,'tradedate'])[0:4]+str(df1.loc[i+1,'tradedate'])[5:7]+str(df1.loc[i+1,'tradedate'])[8:10]}
            df=df.append(dc,ignore_index=True)
            i=i+2
        else:
            dc={'Ticker':df1.loc[i,'tradecode'],'EntryDate':str(df1.loc[i,'tradedate'])[0:4]+str(df1.loc[i,'tradedate'])[5:7]+str(df1.loc[i,'tradedate'])[8:10],'RemoveDate':None}
            df=df.append(dc,ignore_index=True)
            i=i+1
    return(df)
