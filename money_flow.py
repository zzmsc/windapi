# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 09:34:32 2019

@author: zzm
"""

import datetime
from WindPy import w
import pandas as pd

def money_flow(timestr):
    w.start() 
    w.isconnected()
    #timestr=input('tradedate')
    windds1=w.wset('SectorConstituent','date='+timestr+';sector=全部A股')
    datac=windds1.Data[1]
    #datat=['000001.SZ','000002.SZ']
    windds2=w.wss(datac, "mfd_buyamt_d,mfd_sellamt_d,mfd_buyvol_d,mfd_sellvol_d,mfd_buyord,mfd_sellord,mfd_netbuyvol,mfd_netbuyvol_a,mfd_netbuyamt,mfd_netbuyamt_a,mfd_buyamt_a,mfd_sellamt_a,mfd_buyvol_a,mfd_sellvol_a","unit=1;tradeDate="+timestr+";traderType=1")
    windds3=w.wss(datac, "mfd_buyamt_d,mfd_sellamt_d,mfd_buyvol_d,mfd_sellvol_d,mfd_buyord,mfd_sellord,mfd_netbuyvol,mfd_netbuyvol_a,mfd_netbuyamt,mfd_netbuyamt_a,mfd_buyamt_a,mfd_sellamt_a,mfd_buyvol_a,mfd_sellvol_a","unit=1;tradeDate="+timestr+";traderType=2")
    windds4=w.wss(datac, "mfd_buyamt_d,mfd_sellamt_d,mfd_buyvol_d,mfd_sellvol_d,mfd_buyord,mfd_sellord,mfd_netbuyvol,mfd_netbuyvol_a,mfd_netbuyamt,mfd_netbuyamt_a,mfd_buyamt_a,mfd_sellamt_a,mfd_buyvol_a,mfd_sellvol_a","unit=1;tradeDate="+timestr+";traderType=3")
    windds5=w.wss(datac, "mfd_buyamt_d,mfd_sellamt_d,mfd_buyvol_d,mfd_sellvol_d,mfd_buyord,mfd_sellord,mfd_netbuyvol,mfd_netbuyvol_a,mfd_netbuyamt,mfd_netbuyamt_a,mfd_buyamt_a,mfd_sellamt_a,mfd_buyvol_a,mfd_sellvol_a","unit=1;tradeDate="+timestr+";traderType=4")
    windds6=w.wss(datac, "dealnum,mf_vol,volume,amt","tradeDate="+timestr+";unit=1;traderType=1;cycle=D")
    d=[]
    for j in range(len(windds2.Codes)):
        windds2.Data[0][j]=windds2.Data[0][j]/10000
        windds2.Data[1][j]=windds2.Data[1][j]/10000
        windds2.Data[2][j]=windds2.Data[2][j]/100
        windds2.Data[3][j]=windds2.Data[3][j]/100
        windds2.Data[6][j]=windds2.Data[6][j]/100
        windds2.Data[7][j]=windds2.Data[7][j]/100
        windds2.Data[8][j]=windds2.Data[8][j]/10000
        windds2.Data[9][j]=windds2.Data[9][j]/10000
        windds2.Data[12][j]=windds2.Data[12][j]/10000
        windds2.Data[13][j]=windds2.Data[13][j]/10000
        windds2.Data[10][j]=windds2.Data[10][j]/10000
        windds2.Data[11][j]=windds2.Data[11][j]/10000
    for j in range(len(windds3.Codes)):
        windds3.Data[0][j]=windds3.Data[0][j]/10000
        windds3.Data[1][j]=windds3.Data[1][j]/10000
        windds3.Data[2][j]=windds3.Data[2][j]/100
        windds3.Data[3][j]=windds3.Data[3][j]/100
        windds3.Data[6][j]=windds3.Data[6][j]/100
        windds3.Data[7][j]=windds3.Data[7][j]/100
        windds3.Data[8][j]=windds3.Data[8][j]/10000
        windds3.Data[9][j]=windds3.Data[9][j]/10000
        windds3.Data[12][j]=windds3.Data[12][j]/10000
        windds3.Data[13][j]=windds3.Data[13][j]/10000
        windds3.Data[10][j]=windds3.Data[10][j]/10000
        windds3.Data[11][j]=windds3.Data[11][j]/10000
    for j in range(len(windds4.Codes)):
        windds4.Data[0][j]=windds4.Data[0][j]/10000
        windds4.Data[1][j]=windds4.Data[1][j]/10000
        windds4.Data[2][j]=windds4.Data[2][j]/100
        windds4.Data[3][j]=windds4.Data[3][j]/100
        windds4.Data[6][j]=windds4.Data[6][j]/100
        windds4.Data[7][j]=windds4.Data[7][j]/100
        windds4.Data[8][j]=windds4.Data[8][j]/10000
        windds4.Data[9][j]=windds4.Data[9][j]/10000
        windds4.Data[12][j]=windds4.Data[12][j]/10000
        windds4.Data[13][j]=windds4.Data[13][j]/10000
        windds4.Data[10][j]=windds4.Data[10][j]/10000
        windds4.Data[11][j]=windds4.Data[11][j]/10000
    for j in range(len(windds5.Codes)):
        windds5.Data[0][j]=windds5.Data[0][j]/10000
        windds5.Data[1][j]=windds5.Data[1][j]/10000
        windds5.Data[2][j]=windds5.Data[2][j]/100
        windds5.Data[3][j]=windds5.Data[3][j]/100
        windds5.Data[6][j]=windds5.Data[6][j]/100
        windds5.Data[7][j]=windds5.Data[7][j]/100
        windds5.Data[8][j]=windds5.Data[8][j]/10000
        windds5.Data[9][j]=windds5.Data[9][j]/10000
        windds5.Data[12][j]=windds5.Data[12][j]/10000
        windds5.Data[13][j]=windds5.Data[13][j]/10000
        windds5.Data[10][j]=windds5.Data[10][j]/10000
        windds5.Data[11][j]=windds5.Data[11][j]/10000
        
    for i in range(len(windds6.Codes)):
        if(windds6.Data[2][i]!=0):
            d.append(windds6.Data[1][i]/windds6.Data[2][i])
        else: d.append(None)
    dc1={'trades_count':windds6.Data[0],'s_mfd_inflowvolume':[windds6.Data[1][i]/100 for i in range(len(windds6.Codes))] ,'net_inflow_rate_volume':d}
    dc2={'buy_value_exlarge_order':windds2.Data[0],'sell_value_exlarge_order':windds2.Data[1],'buy_value_large_order':windds3.Data[0],'sell_value_large_order':windds3.Data[1],'buy_value_med_order':windds4.Data[0],'sell_value_med_order':windds4.Data[1],'buy_value_small_order':windds5.Data[0],'sell_value_small_order':windds5.Data[1], \
         'buy_volume_exlarge_order':windds2.Data[2],'sell_volume_exlarge_order':windds2.Data[3],'buy_volume_large_order':windds3.Data[2],'sell_volume_large_order':windds3.Data[3],'buy_volume_med_order':windds4.Data[2],'sell_volume_med_order':windds4.Data[3],'buy_volume_small_order':windds5.Data[2],'sell_volume_small_order':windds5.Data[3], \
         'buy_trades_exlarge_order':windds2.Data[4],'sell_trades_exlarge_order':windds2.Data[5],'buy_trades_large_order':windds3.Data[4],'sell_trades_large_order':windds3.Data[5],'buy_trades_med_order':windds4.Data[4],'sell_trades_med_order':windds4.Data[5],'buy_trades_small_order':windds5.Data[4],'sell_trades_small_order':windds5.Data[5], \
         'volume_diff_small_trader':windds5.Data[6],'volume_diff_small_trader_act':windds5.Data[7],'volume_diff_med_trader':windds4.Data[6],'volume_diff_med_trader_act':windds4.Data[7],'volume_diff_large_trader':windds3.Data[6],'volume_diff_large_trader_act':windds3.Data[7],'volume_diff_institute':windds2.Data[6],'volume_diff_institute_act':windds2.Data[7], \
         'value_diff_small_trader':windds5.Data[8],'value_diff_small_trader_act':windds5.Data[9],'value_diff_med_trader':windds4.Data[8],'value_diff_med_trader_act':windds4.Data[9],'value_diff_large_trader':windds3.Data[8],'value_diff_large_trader_act':windds3.Data[9],'value_diff_institute':windds2.Data[8],'value_diff_institute_act':windds2.Data[9], \
         'buy_value_exlarge_order_act':windds2.Data[10],'sell_value_exlarge_order_act':windds2.Data[11],'buy_value_large_order_act':windds3.Data[10],'sell_value_large_order_act':windds3.Data[11],'buy_value_med_order_act':windds4.Data[10],'sell_value_med_order_act':windds4.Data[11],'buy_value_small_order_act':windds5.Data[10],'sell_value_small_order_act':windds5.Data[11], \
         'buy_volume_exlarge_order_act':windds2.Data[12],'sell_volume_exlarge_order_act':windds2.Data[13],'buy_volume_large_order_act':windds3.Data[12],'sell_volume_large_order_act':windds3.Data[13],'buy_volume_med_order_act':windds4.Data[12],'sell_volume_med_order_act':windds4.Data[13],'buy_volume_small_order_act':windds5.Data[12],'sell_volume_small_order_act':windds5.Data[13]}
    windds7=w.wss(datac, "mfd_inflowvolume_open_a,mfd_volinflowrate_open_a,mfd_inflowvolume_close_a,mfd_volinflowrate_close_a,mf_amt,mf_amt_open,mfd_inflowrate_open_a,mf_amt_close,mfd_inflowrate_close_a,mf_vol_ratio,mfd_volinflowproportion_open_a,mfd_volinflowproportion_close_a,mfd_inflowproportion_a,mfd_inflowproportion_open_a,mfd_inflowproportion_close_a","unit=1;tradeDate="+timestr+";traderType=1")
    for j in range(len(windds7.Codes)):
        windds7.Data[0][j]=windds7.Data[0][j]/100
        windds7.Data[1][j]=windds7.Data[1][j]/100
        windds7.Data[2][j]=windds7.Data[2][j]/100
        windds7.Data[3][j]=windds7.Data[3][j]/100
        windds7.Data[4][j]=windds7.Data[4][j]/10000
        windds7.Data[5][j]=windds7.Data[5][j]/10000
        windds7.Data[6][j]=windds7.Data[6][j]/100
        windds7.Data[7][j]=windds7.Data[7][j]/10000
        windds7.Data[8][j]=windds7.Data[8][j]/100
        windds7.Data[12][j]=windds7.Data[12][j]/100
        windds7.Data[13][j]=windds7.Data[13][j]/100
        windds7.Data[14][j]=windds7.Data[14][j]/100
    d=[]
    for i in range(len(windds7.Codes)):
        if(windds6.Data[3][i]!=0):
            d.append(windds7.Data[4][i]*10000/windds6.Data[3][i])
        else: d.append(None)
    dc3={'s_mfd_inflow_openvolume':windds7.Data[0],'open_net_inflow_rate_volume':windds7.Data[1],'s_mfd_inflow_closevolume':windds7.Data[2],'close_net_inflow_rate_volume':windds7.Data[3],'s_mfd_inflow':windds7.Data[4],'net_inflow_rate_value':d,'s_mfd_inflow_open':windds7.Data[5],'open_net_inflow_rate_value':windds7.Data[6],'s_mfd_inflow_close':windds7.Data[7],'close_net_inflow_rate_value':windds7.Data[8],'tot_volume_bid':[None for i in range(len(windds7.Codes))],'tot_volume_ask':[None for i in range(len(windds7.Codes))],'moneyflow_pct_volume':windds7.Data[9],'open_moneyflow_pct_volume':windds7.Data[10],'close_moneyflow_pct_volume':windds7.Data[11],'moneyflow_pct_value':windds7.Data[12],'open_moneyflow_pct_value':windds7.Data[13],'close_moneyflow_pct_value':windds7.Data[14]}
    windds8=w.wss(datac, "mfd_buyvol_m,mfd_volinflowrate_m,mfd_inflow_m,mfd_inflowrate_m,mfd_volinflowproportion_m,mfd_inflowproportion_m,mfd_buyvol_open_m,mfd_volinflowrate_open_m,mfd_inflow_open_m,mfd_inflowrate_open_m,mfd_volinflowproportion_open_m,mfd_inflowproportion_open_m,mfd_buyvol_close_m,mfd_volinflowrate_close_m,mfd_inflow_close_m,mfd_inflowrate_close_m,mfd_volinflowproportion_close_m,mfd_inflowproportion_close_m","unit=1;tradeDate="+timestr)
    for j in range(len(windds8.Codes)):
        windds8.Data[0][j]=windds8.Data[0][j]/100
        windds8.Data[2][j]=windds8.Data[2][j]/10000
        windds8.Data[6][j]=windds8.Data[6][j]/100
        windds8.Data[8][j]=windds8.Data[8][j]/10000
        windds8.Data[12][j]=windds8.Data[12][j]/100
        windds8.Data[14][j]=windds8.Data[14][j]/10000
    dc4={'Ticker':windds8.Codes,'Date':[timestr for i in range(len(windds8.Codes))],'s_mfd_inflowvolume_large_order':windds8.Data[0],'net_inflow_rate_volume_l':windds8.Data[1],'s_mfd_inflow_large_order':windds8.Data[2],'net_inflow_rate_value_l':windds8.Data[3],'moneyflow_pct_volume_l':windds8.Data[4],'moneyflow_pct_value_l':windds8.Data[5],'s_mfd_inflow_openvolume_l':windds8.Data[6],'open_net_inflow_rate_volume_l':windds8.Data[7],'s_mfd_inflow_open_large_order':windds8.Data[8],'open_net_inflow_rate_value_l':windds8.Data[9],'open_moneyflow_pct_volume_l':windds8.Data[10],'open_moneyflow_pct_value_l':windds8.Data[11],'s_mfd_inflow_closevolume_l':windds8.Data[12],'close_net_inflow_rate_volume_l':windds8.Data[13],'s_mfd_inflow_close_large_order':windds8.Data[14],'close_net_inflow_rate_valu_l':windds8.Data[15],'close_moneyflow_pct_volume_l':windds8.Data[16],'close_moneyflow_pct_value_l':windds8.Data[17]}
    df1=pd.DataFrame(dc1)
    df2=pd.DataFrame(dc2)
    df3=pd.DataFrame(dc3)
    df4=pd.DataFrame(dc4)
    df=pd.concat([df1,df2],axis=1)
    df=pd.concat([df,df3],axis=1)
    df=pd.concat([df,df4],axis=1)
    df=df[["Ticker","Date","buy_value_exlarge_order","sell_value_exlarge_order","buy_value_large_order","sell_value_large_order","buy_value_med_order","sell_value_med_order","buy_value_small_order","sell_value_small_order","buy_volume_exlarge_order","sell_volume_exlarge_order","buy_volume_large_order","sell_volume_large_order","buy_volume_med_order","sell_volume_med_order","buy_volume_small_order","sell_volume_small_order","trades_count","buy_trades_exlarge_order","sell_trades_exlarge_order","buy_trades_large_order","sell_trades_large_order","buy_trades_med_order","sell_trades_med_order","buy_trades_small_order","sell_trades_small_order","volume_diff_small_trader","volume_diff_small_trader_act","volume_diff_med_trader","volume_diff_med_trader_act","volume_diff_large_trader","volume_diff_large_trader_act","volume_diff_institute","volume_diff_institute_act","value_diff_small_trader","value_diff_small_trader_act","value_diff_med_trader","value_diff_med_trader_act","value_diff_large_trader","value_diff_large_trader_act","value_diff_institute","value_diff_institute_act","s_mfd_inflowvolume","net_inflow_rate_volume","s_mfd_inflow_openvolume","open_net_inflow_rate_volume","s_mfd_inflow_closevolume","close_net_inflow_rate_volume","s_mfd_inflow","net_inflow_rate_value","s_mfd_inflow_open","open_net_inflow_rate_value","s_mfd_inflow_close","close_net_inflow_rate_value","tot_volume_bid","tot_volume_ask","moneyflow_pct_volume","open_moneyflow_pct_volume","close_moneyflow_pct_volume","moneyflow_pct_value","open_moneyflow_pct_value","close_moneyflow_pct_value","s_mfd_inflowvolume_large_order","net_inflow_rate_volume_l","s_mfd_inflow_large_order","net_inflow_rate_value_l","moneyflow_pct_volume_l","moneyflow_pct_value_l","s_mfd_inflow_openvolume_l","open_net_inflow_rate_volume_l","s_mfd_inflow_open_large_order","open_net_inflow_rate_value_l","open_moneyflow_pct_volume_l","open_moneyflow_pct_value_l","s_mfd_inflow_closevolume_l","close_net_inflow_rate_volume_l","s_mfd_inflow_close_large_order","close_net_inflow_rate_valu_l","close_moneyflow_pct_volume_l","close_moneyflow_pct_value_l","buy_value_exlarge_order_act","sell_value_exlarge_order_act","buy_value_large_order_act","sell_value_large_order_act","buy_value_med_order_act","sell_value_med_order_act","buy_value_small_order_act","sell_value_small_order_act","buy_volume_exlarge_order_act","sell_volume_exlarge_order_act","buy_volume_large_order_act","sell_volume_large_order_act","buy_volume_med_order_act","sell_volume_med_order_act","buy_volume_small_order_act","sell_volume_small_order_act"]]
    print(df)
