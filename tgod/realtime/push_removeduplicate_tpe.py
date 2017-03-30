# -*- coding: utf-8 -*-

### get data from data_storage, remove duplicates, then push table to data_processed -- for taipei data
### should be run daily

import pandas as pd
import datetime
import time
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))
#print os.getcwd()


def retrieve_bus(dstr):
    header = ['ind_0','azimuth','busid','busstatus','carid','cartype','datatime','dutystatus','goback','latitude','longitude','providerid','routeid','speed','stationid','datetime2','utimestamp']
    df = pd.read_csv('data_storage/data_bus2_'+dstr+'.csv', index_col=0, header=None, names=header)
    #print df.head()
    #print len(df)
    df.drop_duplicates(subset=['utimestamp','carid'],inplace=True)
    df.reset_index(inplace=True)
    #print df.head()
    #df = df.drop('index',axis=1)
    df = df.drop('ind_0',axis=1)
    #print len(df)
    with open('data_processed/data_bus3_'+dstr+'.csv', 'a') as f:
        df.to_csv(f,index_label='ind',encoding="utf-8")

def retrieve_busevent(dstr):
    header = ['ind_0','busid','busstatus','carid','caronstop','cartype','datatime','dutystatus','goback','providerid','routeid','stationid','stopid','datetime2','utimestamp']
    df = pd.read_csv('data_storage/data_busevent2_'+dstr+'.csv', index_col=0, header=None, names=header)
    #print df.head()
    #print len(df)
    df.drop_duplicates(subset=['utimestamp','carid'],inplace=True)
    df.reset_index(inplace=True)
    #df = df.drop('index',axis=1)
    df = df.drop('ind_0',axis=1)
    #print len(df)
    with open('data_processed/data_busevent3_'+dstr+'.csv', 'a') as f:
        df.to_csv(f,index_label='ind',encoding="utf-8")

def retrieve_vd(dstr):
    header = ['ind_0','avgoccupancy','avgspeed','laneno','lvolume','mvolume','svolume', 'volume','time','timeinterval','vdid','datetime2','utimestamp']
    df = pd.read_csv('data_storage/data_vddata2_'+dstr+'.csv', header=None, names=header)
    #print df.head()
    #print len(df)
    df.drop_duplicates(subset=['vdid','laneno','utimestamp'],inplace=True)
    #print len(df)
    df.reset_index(inplace=True)
    #df = df.drop('index',axis=1)
    df = df.drop('ind_0',axis=1)
    #print df.head()

    with open('data_processed/data_vddata3_'+dstr+'.csv', 'a') as f:
        df.to_csv(f,index_label='ind',encoding="utf-8")


def retrieve_ubike(dstr):
    header = ['ind_0','act','ar','aren','bemp','lat','lng','mday','sarea','sareaen','sbi','sna','snaen','sno','tot','ubid','datetime2','utimestamp']
    df = pd.read_csv('data_storage/data_ubike2_'+dstr+'.csv', index_col=0, header=None, names=header)
    #print df.head()
    #print len(df)
    df.drop_duplicates(subset=['utimestamp','sno'],inplace=True)
    df.reset_index(inplace=True)
    #df = df.drop('index',axis=1)
    df = df.drop('ind_0',axis=1)
    #print len(df)
    with open('data_processed/data_ubike3_'+dstr+'.csv', 'a') as f:
        df.to_csv(f,index_label='ind',encoding="utf-8")

def retrieve_mrt(dstr):
    header = ['ind_0', 'boundfor', 'station', 'updatetime', 'idd','datetime2','utimestamp']
    df = pd.read_csv('data_storage/data_mrt2_'+dstr+'.csv', index_col=0, header=None, names=header)
    #print df.head()
    #print len(df)
    df.drop_duplicates(subset=['utimestamp','boundfor','station'],inplace=True)
    df.reset_index(inplace=True)
    #df = df.drop('index',axis=1)
    df = df.drop('ind_0',axis=1)
    #print len(df)
    with open('data_processed/data_mrt3_'+dstr+'.csv', 'a') as f:
        df.to_csv(f,index_label='ind',encoding="utf-8")

def main():
    yesterday = datetime.datetime.today() - datetime.timedelta(1)
    #yesterday = datetime.datetime(2016,10,3)
    yesterdaystr = datetime.datetime.strftime(yesterday,"%Y-%m-%d")
    #print yesterdaystr
    retrieve_vd(yesterdaystr)

    #"""
    try:
        retrieve_bus(yesterdaystr) # every day
    except:
        print( "busdata problem "+str(datetime.datetime.now()) )
    try:
        retrieve_busevent(yesterdaystr) # every day
    except:
        print( "busevent problem "+str(datetime.datetime.now()) )
    try:
        retrieve_vd(yesterdaystr) # every day
    except:
        print( "vddata problem "+str(datetime.datetime.now()) )
    try:
        retrieve_ubike(yesterdaystr) # every day
    except:
        print( "ubike problem "+str(datetime.datetime.now()) )
    try:
        retrieve_mrt(yesterdaystr) # every day
    except:
        print( "mrttrain problem "+str(datetime.datetime.now()) )
    print( "run once! " +str(datetime.datetime.now()))
    #"""

if __name__ == '__main__':
    main()
