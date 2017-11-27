# -*- coding: utf-8 -*-

### get data from data_storage, remove duplicates, then push table to data_processed -- for new taipei data
### should be run daily

import pandas as pd
import datetime
import time
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))
#print os.getcwd()


def retrieve_vd2(dstr):
    header = ['ind_0','avg_speed','car_spd','car_vol','data_time','dir','lane','large_spd','large_vol','motor_spd','motor_vol','total_vol','truc_spd','truc_vol','vdid','datetime2','utimestamp']
    df = pd.read_csv('data_storage/data_newtp_vddata2_'+dstr+'.csv', header=None, names=header)
    #print df.head()
    #print len(df)
    df.drop_duplicates(subset=['vdid','dir','lane','utimestamp'],inplace=True)
    #print len(df)
    df.reset_index(inplace=True)
    #df = df.drop('index',axis=1)
    df = df.drop('ind_0',axis=1)
    #print df.head()
    with open('data_processed/data_newtp_vddata3_'+dstr+'.csv', 'a') as f:
        df.to_csv(f,index_label='ind',encoding="utf-8")

def retrieve_ubike2(dstr):
    header = ['ind_0','mday','sareaen','sna','aren','sno','tot','snaen','bemp','ar','act','lat','lng','sbi','sarea','ubid','datetime2','utimestamp']
    df = pd.read_csv('data_storage/data_newtp_ubike2_'+dstr+'.csv', index_col=0, header=None, names=header)
    #print df.head()
    #print len(df)
    df.drop_duplicates(subset=['utimestamp','sno'],inplace=True)
    df.reset_index(inplace=True)
    #df = df.drop('index',axis=1)
    df = df.drop('ind_0',axis=1)
    #print len(df)
    with open('data_processed/data_newtp_ubike3_'+dstr+'.csv', 'a') as f:
        df.to_csv(f,index_label='ind',encoding="utf-8")


def main():
    yesterday = datetime.datetime.today() - datetime.timedelta(1)
    yesterdaystr = datetime.datetime.strftime(yesterday,"%Y-%m-%d")
    #print yesterdaystr

    try:
        retrieve_vd2(yesterdaystr) # every day
    except:
        print( "vddata problem "+str(datetime.datetime.now()) )
    try:
        retrieve_ubike2(yesterdaystr) # every day
    except:
        print( "ubike problem "+str(datetime.datetime.now()) )
    print( "run once! " +str(datetime.datetime.now()))

if __name__ == '__main__':
    main()
