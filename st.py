# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 12:53:16 2019

@author: zzm
"""
import datetime
from WindPy import w
import pandas as pd
def st(timestr):
    w.start() 
    w.isconnected()
    #timestr=input('tradedate')
    windds1=w.wset("carryoutspecialtreatment","startdate=1998-04-28;enddate="+timestr+";field=wind_code,implementation_date")
    wcode=[]
    wdate=[]
    status=[]
    for i in range(len(windds1.Codes)):
       if(windds1.Data[0][i][7:9]!='OC') :
           wcode.append(windds1.Data[0][i])
           wdate.append(windds1.Data[1][i])
           status.append(1)
    dc1={'codes':wcode,'date':wdate,'status':status}
    windds2=w.wset("cancelspecialtreatment","startdate=1998-04-28;enddate="+timestr+";field=wind_code,implementation_date")
    wcode=[]
    wdate=[]
    status=[]
    for i in range(len(windds2.Codes)):
       if(windds1.Data[0][i][7:9]!='OC') :
           wcode.append(windds2.Data[0][i])
           wdate.append(windds2.Data[1][i])
           status.append(2)
    dc2={'codes':wcode,'date':wdate,'status':status}
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
    return(df)
            


