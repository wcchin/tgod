# -*- coding: utf-8 -*-

### get data from open data api links -- for taipei data

import pandas as pd
import time
import datetime

from utils import get_gJX as getting

def bus(f_postfix=None):
    out = getting.HandleGZippedJSON("http://data.taipei/bus/BUSDATA")
    #out.run()
    table2 = pd.DataFrame.from_dict(out.data['BusInfo'])
    dt = table2.DataTime.tolist()
    dt2 = []
    timestamp = []
    for dt_i in dt:
		tt = datetime.datetime.strptime(dt_i, '%Y-%m-%d %H:%M:%S')
		ts = int(time.mktime(tt.timetuple()))
		dt2.append(tt)
		timestamp.append(ts)
    table2['datetime2'] = dt2
    table2['utimestamp'] = timestamp
    return table2

def busevent(f_postfix=None):
    out = getting.HandleGZippedJSON("http://data.taipei/bus/BUSEVENT")
    #out.run()
    table2 = pd.DataFrame.from_dict(out.data['BusInfo'])
    #print 'hey',table2.columns
    dt = table2['DataTime'].tolist()
    dt2 = []
    timestamp = []
    for dt_i in dt:
		tt = datetime.datetime.strptime(dt_i, '%Y-%m-%d %H:%M:%S')
		ts = int(time.mktime(tt.timetuple()))
		dt2.append(tt)
		timestamp.append(ts)
    table2['datetime2'] = dt2
    table2['utimestamp'] = timestamp
    return table2

def vehicle_detector(f_postfix=None):
    return vd(f_postfix=f_postfix)

def vd(f_postfix=None):
    out = getting.HandleGZippedXML("http://data.taipei/tisv/VDDATA")
    #out.run()
    thetime = out.data['VDInfoSet']['ExchangeTime']
    table2=None
    for row in  out.data['VDInfoSet']['VDInfo']:
        data = row['VDData']['VDDevice']
        vdid=data['DeviceID']
        lanedata=data['LaneData']
        timeinterval=data['TimeInterval']
        totallane=data['TotalOfLane']
        temp_lanes={}
        if type(lanedata) is list:
            lanes={}
            lanes['AvgOccupancy']=[]
            lanes['AvgSpeed']=[]
            lanes['LaneNO']=[]
            lanes['Lvolume']=[]
            lanes['Mvolume']=[]
            lanes['Svolume']=[]
            lanes['Volume']=[]
            lanes['time']=[]
            lanes['vdid']=[]
            lanes['timeinterval']=[]

            for lane in lanedata:
                for key, value in lane.iteritems():
                    lanes[key].append(value)
                lanes['time'].append(thetime)
                lanes['vdid'].append(vdid)
                lanes['timeinterval'].append(timeinterval)
            temp_lanes=lanes
        elif type(lanedata) is dict:
            lanes={}
            for key, value in lanedata.iteritems():
                lanes[key]=[value]
            lanes['time']=[thetime]
            lanes['vdid']=[vdid]
            lanes['timeinterval']=[timeinterval]
            temp_lanes=lanes
        else:
            print "type error"
        temp_table=pd.DataFrame.from_dict(temp_lanes)
        if table2 is None:
            table2=temp_table
        else:
            table2=table2.append(temp_table, ignore_index=True)
    dt = table2.time.tolist()
    dt2 = []
    timestamp = []
    for dt_i in dt:
        tt = datetime.datetime.strptime(dt_i, '%Y/%m/%dT%H:%M:%S')
        ts = int(time.mktime(tt.timetuple()))
        dt2.append(tt)
        timestamp.append(ts)
    table2['datetime2'] = dt2
    table2['utimestamp'] = timestamp
    return table2

def road_level(f_postfix=None):
    out = getting.HandleGZippedXML("http://data.taipei/tisv/VD")
    #out.run()
    data = out.data
    data2 = { k.replace('{http://www.iii.org.tw/dax/vd}',''):v for k,v in data.iteritems() }
    data3 = { k.replace('{http://www.iii.org.tw/dax/vd}',''):v for k,v in data2['ExchangeData'].iteritems() }
    thetime = data3['ExchangeTime']
    tt = datetime.datetime.strptime(thetime, '%Y/%m/%dT%H:%M:%S')
    ts = int(time.mktime(tt.timetuple()))
    data4 = { k.replace('{http://www.iii.org.tw/dax/vd}',''):v for k,v in data3['SectionDataSet'].iteritems() }
    data5 = {}
    i = 0
    time_dic = {'datetime2':tt, 'utimestamp':ts}
    for l in data4['SectionData']:
        d5 = { k.replace('{http://www.iii.org.tw/dax/vd}',''):v for k,v in l.iteritems() }
        d5.update(time_dic)
        data5[i] = d5
        i+=1
    table = pd.DataFrame.from_dict(data5, orient='index')
    #print table.head()
    return table

def bikeshare(f_postfix=None):
    out = getting.HandleGZippedJSON("http://data.taipei/youbike")
    #out.run()
    thetime=None
    table2=None
    for key, val in out.data['retVal'].iteritems():
        ubid=key
        if thetime is None:
            thetime= val['mday']
        temp={}
        for k,v in val.iteritems():
            temp[k]=[v]
        temp['ubid']=key
        temp_table=pd.DataFrame.from_dict(temp)
        if table2 is None:
            table2=temp_table
        else:
            table2=table2.append(temp_table)
    dt = table2.mday.tolist()
    dt2 = []
    timestamp = []
    for dt_i in dt:
        tt = datetime.datetime.strptime(dt_i, '%Y%m%d%H%M%S')
        ts = int(time.mktime(tt.timetuple()))
        dt2.append(tt)
        timestamp.append(ts)
    table2['datetime2'] = dt2
    table2['utimestamp'] = timestamp
    return table2

def mrt(f_postfix=None):
    out = getting.HandleNonGZippedJSON("http://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=55ec6d6e-dc5c-4268-a725-d04cc262172b")
    #out.run()
    table2 =pd.DataFrame.from_dict(out.data['result']['results'])
    dt = table2.UpdateTime.tolist()
    dt2 = []
    timestamp = []
    for dt_i in dt:
        tt = datetime.datetime.strptime(dt_i.split(".")[0], '%Y-%m-%dT%H:%M:%S')
        ts = int(time.mktime(tt.timetuple()))
        dt2.append(tt)
        timestamp.append(ts)
    table2['datetime2'] = dt2
    table2['utimestamp'] = timestamp
    return table2

if __name__ == '__main__':

    today = str(datetime.datetime.today().date())

    try:
        print 'trying taipei bus data '
        busdf = busdata(f_postfix=today) # every min
        print busdf.head(10)
    except:
        print( "busdata problem "+str(datetime.datetime.now()) )
    try:
        print 'trying taipei bus event data '
        busevdf = busevent(f_postfix=today) # every min
        print busevdf.head(10)
    except:
        print( "busevent problem "+str(datetime.datetime.now()) )
    try:
        print 'trying taipei vd data '
        vddf = vddata(f_postfix=today) # every min
        print vddf.head(10)
    except:
        print( "vddata problem "+str(datetime.datetime.now()) )
    try:
        print 'trying taipei road level(vd section) data '
        vd2df = road_level(f_postfix=today) # every min
        print vd2df.head(10)
    except:
        print( "vddata problem "+str(datetime.datetime.now()) )
    try:
        print 'trying taipei ubike data '
        udf = bikeshare(f_postfix=today) # every min
        print udf.head(10)
    except:
        print( "ubike problem "+str(datetime.datetime.now()) )
    try:
        print 'trying taipei mrt data '
        mdf = mrt(f_postfix=today) # every min
        print mdf.head(10)
    except:
        print( "mrt problem "+str(datetime.datetime.now()) )
    print( "run once! " +str(datetime.datetime.now()))
