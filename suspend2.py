# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 15:00:07 2019

@author: zzm
"""

import datetime
from WindPy import w
import pandas as pd
def suspend1(timestr):
    w.start() 
    w.isconnected()
    #timestr=input('tradedate')
    windds1=w.wset("pauselistsecurity","startdate=1998-04-28;enddate="+timestr+";sectorid=a001010100000000;field=wind_code,susp_list_date")
    windds2=w.wset("resumelistsecurity","startdate=1998-04-28;enddate="+timestr+";sectorid=a001010100000000;field=wind_code,resume_list_date")
    dc1={'codes':windds1.Data[0],'date':windds1.Data[1],'status':[1 for i in range(len(windds1.Codes))]}
    dc2={'codes':windds2.Data[0],'date':windds2.Data[1],'status':[2 for i in range(len(windds2.Codes))]}
    df1=pd.DataFrame(dc1)
    df2=pd.DataFrame(dc2)
    df=pd.concat([df1,df2],ignore_index=True)
    df=df.sort_values(by=["codes",'date'])
    code=[]
    entrydate=[]
    removedate=[]
    i=0
    while(i<len(df)):
        if(df.iloc[i][2]==2):
            i+=1
        elif(i<(len(df)-1) and df.iloc[i][0]==df.iloc[i+1][0]):
            code.append(df.iloc[i][0])
            entrydate.append(str(df.iloc[i][1])[0:4]+str(df.iloc[i][1])[5:7]+str(df.iloc[i][1])[8:10])
            removedate.append(str(df.iloc[i+1][1])[0:4]+str(df.iloc[i+1][1])[5:7]+str(df.iloc[i+1][1])[8:10])
            i+=2
        else:
            code.append(df.iloc[i][0])
            entrydate.append(str(df.iloc[i][1])[0:4]+str(df.iloc[i][1])[5:7]+str(df.iloc[i][1])[8:10])
            removedate.append(None)
            i+=1
    dc={'Ticker':code,'EntryDate':entrydate,'RemoveDate':removedate}
    df=pd.DataFrame(dc)
    code=[]
    for i in range(len(df)):
        if(df.iloc[i][2]==None):
            code.append(df.iloc[i][0])
    dc={'Ticker':code,'Date':[timestr for i in range(len(code))]}
    df=pd.DataFrame(dc)
    return(df)
