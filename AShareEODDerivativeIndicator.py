# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 14:40:55 2019

@author: zzm
"""
import datetime
from WindPy import w
import pandas as pd

def AShareEODDerivativeIndicator(timestr):
    w.start()
    w.isconnected()

    timey=timestr[0:4]
    timem=timestr[4:6]
    timed=timestr[6:8]
    date= datetime.datetime(int(timey), int(timem), int(timed))
    windds1=w.wset('SectorConstituent','date='+timestr+';sector=全部A股')
    datac=windds1.Data[1]
    #datat=['000001.SZ','000002.SZ']

    date52b=date+datetime.timedelta(-364)
    startdate=str(date52b)
    windds6=w.wss(datac,"latelyrd_bt","tradeDate="+timestr)

    lt=list(set(windds6.Data[0]))
    latelyrd=[[] for x in range(len(lt))]
    lty=list(set(windds6.Data[0]))
    for a in range(len(lt)):
        if lty[a].month!=12:
            lty[a]=datetime.datetime(lt[a].year-1,12,31)
        
    for b in range(len(windds6.Codes)):
        for a in range(len(lt)):
            if windds6.Data[0][b]==lt[a]:
                latelyrd[a].append(windds6.Codes[b])
                break
    windds4=w.wss(latelyrd[0], "pe,pb,pe_ttm,pcf_ocf,pcf_ocf_ttm,pcf_ncf,pcf_ncf_ttm,ps,ps_ttm,netprofit_ttm,np_belongto_parcomsh,net_cash_flows_oper_act,oper_rev,net_incr_cash_cash_equ_dm","tradeDate="+timestr+";ruleType=10;unit=1;rptDate="+str(lty[0])+";rptType=1;currencyType=")
    if(len(lt)>1):
        for a in range(1,len(lt)):
            winddst=w.wss(latelyrd[a], "pe,pb,pe_ttm,pcf_ocf,pcf_ocf_ttm,pcf_ncf,pcf_ncf_ttm,ps,ps_ttm,netprofit_ttm,np_belongto_parcomsh,net_cash_flows_oper_act,oper_rev,net_incr_cash_cash_equ_dm","tradeDate="+timestr+";ruleType=10;unit=1;rptDate="+str(lty[a])+";rptType=1;currencyType=") 
            windds4.Codes+=winddst.Codes
            for b in range(len(winddst.Data)):
                windds4.Data[b]+=winddst.Data[b]
    del winddst

    lt=list(set(windds6.Data[0]))
    latelyrd=[[] for x in range(len(lt))]
    for b in range(len(windds6.Codes)):
       for a in range(len(lt)):
           if windds6.Data[0][b]==lt[a]:
               latelyrd[a].append(windds6.Codes[b])
               break
    windds5=w.wss(latelyrd[0], "wgsd_bps_new,total_shares,operatecashflow_ttm2,or_ttm2","currencyType=;unit=1;tradeDate="+timestr+";rptDate="+str(lt[0]))
    if(len(lt)>1):
        for a in range(1,len(lt)):
            winddst=w.wss(latelyrd[a], "wgsd_bps_new,total_shares,operatecashflow_ttm2,or_ttm2","currencyType=;unit=1;tradeDate="+timestr+";rptDate="+str(lt[a]))
            windds5.Codes+=winddst.Codes
            for b in range(len(winddst.Data)):
                windds5.Data[b]+=winddst.Data[b]
    del winddst

    windds2=w.wss(windds5.Codes,'ev,mkt_cap_float,high_per,low_per,turn,free_turn_n,total_shares,float_a_shares,free_float_shares',"unit=1;tradeDate="+timestr+";currencyType=;startDate="+startdate+";endDate="+timestr+";priceAdj=U")
    windds3=w.wss(windds5.Codes,"high_per,low_per,maxupordown,high_date_per,low_date_per","unit=1;tradeDate="+timestr+";currencyType=;startDate="+startdate+";endDate="+timestr+";priceAdj=B")

    windds7=w.wss(latelyrd[0], "wgsd_cce","unit=1;rptDate="+str(lt[0])+";rptType=1;currencyType=")
    if(len(lt)>1):
        for a in range(1,len(lt)):
            winddst=w.wss(latelyrd[a], "wgsd_cce","unit=1;rptDate="+str(lt[a])+";rptType=1;currencyType=")
            windds7.Codes+=winddst.Codes
            for b in range(len(winddst.Data)):
                windds7.Data[b]+=winddst.Data[b]
    del winddst

    windds8=w.wss(latelyrd[0], "wgsd_cce","unit=1;rptDate="+str(datetime.datetime(lt[0].year-1,lt[0].month,lt[0].day))+";rptType=1;currencyType=")
    if(len(lt)>1):
        for a in range(1,len(lt)):
            winddst=w.wss(latelyrd[a], "wgsd_cce","unit=1;rptDate="+str(datetime.datetime(lt[a].year-1,lt[a].month,lt[a].day))+";rptType=1;currencyType=")
            windds8.Codes+=winddst.Codes
            for b in range(len(winddst.Data)):
                windds8.Data[b]+=winddst.Data[b]
    del winddst


    dc1={'Ticker':windds5.Codes,'Date':[timestr]*len(datac),'MarketValue':windds2.Data[0], \
         'MarketValueFree':windds2.Data[1],'High52w':windds2.Data[2],'Low52w':windds2.Data[3] \
         ,'TurnOver':windds2.Data[4],'TurnOverFree':windds2.Data[5],'TotalShares':windds2.Data[6],
                'TotalSharesLT':windds2.Data[7],'TotalSharesFree':windds2.Data[8]}
    lhs=[]
    for i in range(len(datac)):
        lhs.append(int(date==windds3.Data[3][i] or date==windds3.Data[4][i]))
    dc2={'AdjHigh52w':windds3.Data[0],'AdjLow52w':windds3.Data[1],'UpDownLimitStatus':windds3.Data[2],'LowestHighestStatus':lhs}

    dc3={'PE':windds4.Data[0],'PB':windds4.Data[1],'PE_ttm':windds4.Data[2],'PCF_ocf':windds4.Data[3] \
         ,'PCF_ocfttm':windds4.Data[4],'PCF_ncf':windds4.Data[5],'PCF_ncfttm':windds4.Data[6], \
         'PS':windds4.Data[7],'PS_ttm':windds4.Data[8],'NetProfit_parent_comp_ttm':windds4.Data[9], \
         'NetProfit_parent_comp_lyr':windds4.Data[10],'NetCashFlow_oper_act_lyr':windds4.Data[11], \
         'OperRev_lyr':windds4.Data[12],'NetIncrCash_cash_equ_lyr':windds4.Data[13]}
    lhs=[]
    for i in range(len(datac)):
        lhs.append(windds5.Data[0][i]*windds5.Data[1][i])
    dc4={'NetAsset':lhs,'NetCashFlow_oper_act_ttm':windds5.Data[2],'OperRev_ttm':windds5.Data[3]}

    lhs=[]
    for i in range(len(datac)):
        if windds7.Data[0][i]==None or windds8.Data[0][i]==None:
            lhs.append(None)
        else: lhs.append(windds7.Data[0][i]-windds8.Data[0][i])
    dc5={'NetIncrCash_cash_equ_ttm':lhs}
    df1=pd.DataFrame(dc1)
    df2=pd.DataFrame(dc2)
    df3=pd.DataFrame(dc3)
    df4=pd.DataFrame(dc4)
    df5=pd.DataFrame(dc5)
    df=pd.concat([df1,df2],axis=1)
    df=pd.concat([df,df3],axis=1)
    df=pd.concat([df,df4],axis=1)
    df=pd.concat([df,df5],axis=1)
    df = df[['Ticker','Date','MarketValue','MarketValueFree','High52w','Low52w','TurnOver','TurnOverFree','TotalShares','TotalSharesLT','TotalSharesFree','AdjHigh52w','AdjLow52w','UpDownLimitStatus','LowestHighestStatus','PE','PB','PE_ttm','PCF_ocf','PCF_ocfttm','PCF_ncf','PCF_ncfttm','PS','PS_ttm','NetProfit_parent_comp_ttm','NetProfit_parent_comp_lyr','NetAsset','NetCashFlow_oper_act_ttm','NetCashFlow_oper_act_lyr','OperRev_ttm','OperRev_lyr','NetIncrCash_cash_equ_ttm','NetIncrCash_cash_equ_lyr']]
    df=df.sort_values(by="Ticker")
    print(df)
    w.stop()
    return df


