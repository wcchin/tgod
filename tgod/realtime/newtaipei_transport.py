# -*- coding: utf-8 -*-

### get data from open data api links -- for new taipei data

import pandas as pd
import time
import datetime

from utils import get_gJX as getting

def vehicle_detector(f_postfix=None):
    return vd(f_postfix=f_postfix)

def vd(f_postfix=None):
    # http://data.gov.tw/node/30858
    url = "http://data.ntpc.gov.tw/api/v1/rest/datastore/382000000A-000357-001"
    out = getting.HandleNonGZippedJSON(url)
    out.run()
    #print out.json_data['result']['fields']
    """
    for key, value in out.json_data['result'].iteritems():
        print key
        print value
    """
    dict_temp = {}
    rec_len = len(out.json_data['result']['records'])
    for i in range(rec_len):
        dict_temp[i] = out.json_data['result']['records'][i]
    df_temp = pd.DataFrame.from_dict(dict_temp,orient='index')
    #print df_temp.head()
    #ubid = df_temp.sno.tolist()
    #df_temp['ubid'] = ubid
    #print len(df_temp)

    vdid_setlist = list(set(df_temp.vdid.tolist()))
    vd_list = []
    direc_list = []
    lane_list = []
    time_list = []
    avg_speed_list = []
    T_vol_list = [] # connect truck
    L_vol_list = [] # big_car
    S_vol_list = [] # car
    M_vol_list = [] # motorcycle
    T_spd_list = [] # connect truck
    L_spd_list = [] # big_car
    S_spd_list = [] # car
    M_spd_list = [] # motorcycle
    total_vol_list = []
    for vd in vdid_setlist:
        df_vd = df_temp[df_temp['vdid']==vd]
        dir_setlist = list(set(df_vd.vsrdir.tolist()))
        for direc in dir_setlist:
            df_dir = df_vd[df_vd['vsrdir']==direc]
            lane_setlist = list(set(df_dir.vsrid.tolist()))
            for lane in lane_setlist:
                df_lane = df_dir[df_dir.vsrid==lane]
                time_setlist = list(set(df_lane.datacollecttime.tolist()))
                for tt in time_setlist:
                    df_time = df_lane[df_lane.datacollecttime==tt]
                    check = any([int(x)<0 for x in df_time.volume.tolist()])
                    if not check:
                        vol_dict = {}
                        spd_dict = {}
                        for i in range(len(df_time)):
                            row = df_time.iloc[i]
                            c_type = row.carid
                            c_vol = row.volume
                            c_spd = row.speed
                            vol_dict[c_type] = c_vol
                            spd_dict[c_type] = c_spd

                        t,l,s,m = (0,0,0,0)
                        t2,l2,s2,m2 = (0,0,0,0)
                        if 'T' in vol_dict:
                            t = int(vol_dict['T'])
                            t2 = float(spd_dict['T'])
                        if 'L' in vol_dict:
                            l = int(vol_dict['L'])
                            l2 = float(spd_dict['L'])
                        if 'S' in vol_dict:
                            s = int(vol_dict['S'])
                            s2 = float(spd_dict['S'])
                        if 'M' in vol_dict:
                            m = int(vol_dict['M'])
                            m2 = float(spd_dict['M'])

                        total_temp = t+l+s+m
                        #print total_temp
                        if total_temp>0:
                            avg_spd = float((t*t2+l*l2+s*s2+m*m2))/(total_temp)
                        else:
                            avg_spd = -1

                        vd_list.append(vd)
                        direc_list.append(direc)
                        lane_list.append(lane)
                        time_list.append(tt)
                        T_vol_list.append(t) # connect truck
                        T_spd_list.append(t2)
                        L_vol_list.append(l) # big_car
                        L_spd_list.append(l2)
                        S_vol_list.append(s) # car
                        S_spd_list.append(s2)
                        M_vol_list.append(m) # motorcycle
                        M_spd_list.append(m2)
                        total_vol_list.append(total_temp)
                        avg_speed_list.append(avg_spd)

    df_temp2 = pd.DataFrame.from_dict({
    'vdid':vd_list, 'dir':direc_list,'lane':lane_list,'data_time':time_list,
    'truc_vol':T_vol_list,'large_vol':L_vol_list,'car_vol':S_vol_list,'motor_vol':M_vol_list,'total_vol':total_vol_list,
    'truc_spd':T_spd_list,'large_spd':L_spd_list,'car_spd':S_spd_list,'motor_spd':M_spd_list,'avg_speed':avg_speed_list})
    #print df_temp2.head(20)
    #print len(df_temp2)
    dt = df_temp2.data_time.tolist()
    dt2 = []
    timestamp = []
    for dt_i in dt:
        tt = datetime.datetime.strptime(dt_i, '%Y/%m/%d %H:%M:%S')
        #print tt
        ts = int(time.mktime(tt.timetuple()))
        #print ts
        dt2.append(tt)
        timestamp.append(ts)
    df_temp2['datetime2'] = dt2
    df_temp2['utimestamp'] = timestamp
    #print df_temp2.head(20)
    #with open('data_storage/data_newtp_vddata2_'+f_postfix+'.csv', 'a') as f:
    #    df_temp2.to_csv(f, encoding="utf-8", header=False)
    ## header:
    ## ind,avg_speed,car_spd,car_vol,data_time,dir,lane,large_spd,large_vol,motor_spd,motor_vol,total_vol,truc_spd,truc_vol,vdid,datetime2,utimestamp
    #df_temp2.to_sql('data_newtp_vddata2', engine, if_exists="append")
    return df_temp2

def bikeshare(f_postfix=None):
    # http://data.gov.tw/node/28318
    url = 'http://data.ntpc.gov.tw/api/v1/rest/datastore/382000000A-000352-001'
    out = getting.HandleNonGZippedJSON(url)
    out.run()
    #print out.json_data['result']['fields']
    """
    for key, value in out.json_data['result'].iteritems():
        print key
        print value
    """
    dict_temp = {}
    rec_len = len(out.json_data['result']['records'])
    for i in range(rec_len):
        dict_temp[i] = out.json_data['result']['records'][i]
    df_temp = pd.DataFrame.from_dict(dict_temp,orient='index')
    #print df_temp.head()
    ubid = df_temp.sno.tolist()
    df_temp['ubid'] = ubid
    dt = df_temp.mday.tolist()
    dt2 = []
    timestamp = []
    for dt_i in dt:
        tt = datetime.datetime.strptime(dt_i, '%Y%m%d%H%M%S')
        #print tt
        ts = int(time.mktime(tt.timetuple()))
        #print ts
        dt2.append(tt)
        timestamp.append(ts)
    df_temp['datetime2'] = dt2
    df_temp['utimestamp'] = timestamp
    #print df_temp.head(10)
    #with open('data_storage/data_newtp_ubike2_'+f_postfix+'.csv', 'a') as f:
    #    df_temp.to_csv(f, encoding="utf-8", header=False)
    ## header:
    ## ind,mday,sareaen,sna,aren,sno,tot,snaen,bemp,ar,act,lat,lng,sbi,sarea,ubid,datetime2,utimestamp
    #df_temp.to_sql('data_newtp_ubike2', engine, if_exists="append")
    return df_temp

if __name__ == '__main__':
    today = str(datetime.datetime.today().date())
    try:
        print 'trying new taipei ubike data '
        udf = bikeshare(f_postfix=today) # every min
        print udf.head(10)
    except:
        print( "new taipei ubike problem "+str(datetime.datetime.now()) )
    try:
        print 'trying new taipei vd data '
        vdf = vd(f_postfix=today) # every min
        print vdf.head(10)
    except:
        print( "new taipei vd problem "+str(datetime.datetime.now()) )
    print( "run once! " +str(datetime.datetime.now()))
