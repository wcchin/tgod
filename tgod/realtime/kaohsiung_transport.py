# -*- coding: utf-8 -*-

### get data from open data api links -- for kaohsiung data

import pandas as pd
import time
import datetime

import get_gJX as getting

def bus_data(f_postfix=None):
    # http://data.kcg.gov.tw/dataset/bus-real-time-dynamic
    url = 'http://ibus.tbkc.gov.tw/xmlbus/GetBusData.xml'
    out = getting.HandleNonGZippedXML(url)
    out.run()
    infos = out.xml_data['BusDynInfo']['EssentialInfo']
    busdata = out.xml_data['BusDynInfo']['BusInfo']['BusData']
    bus_dict = {}
    i = 0
    for bus in busdata:
        bus_dict[i] = bus
        i+=1
    df = pd.DataFrame.from_dict(bus_dict, orient='index')
    col = df.columns.tolist()
    col2 = { c:c.replace('@','') for c in col }
    df = df.rename(columns=col2)
    df['DataTime'] = pd.to_datetime(df['DataTime'], format='%Y-%m-%d %H:%M:%S')
    timestamp = [ int(time.mktime(tt.timetuple())) for tt in df['DataTime'].tolist() ]
    df = df.rename(columns={'DataTime':'datetime2'})
    df['utimestamp'] = timestamp
    return df


def road_level(f_postfix=None):
    # http://data.kcg.gov.tw/dataset/department-of-transportation9
    url = 'http://xml11.kctmc.nat.gov.tw:8080/XML/roadlevel_value.xml'
    out = getting.HandleNonGZippedXML(url)
    out.run()
    infos = out.xml_data['XML_Head']['Infos']['Info']
    data_dic = {}
    for i in range(len(infos)):
        data_dic[i] = infos[i]
    df = pd.DataFrame.from_dict(data_dic, orient='index')
    col = df.columns.tolist()
    col2 = { c:c.replace('@','') for c in col }
    df = df.rename(columns=col2)

    df['datacollecttime'] = pd.to_datetime(df['datacollecttime'], format='%Y/%m/%d %H:%M:%S')
    timestamp = [ int(time.mktime(tt.timetuple())) for tt in df['datacollecttime'].tolist() ]
    df = df.rename(columns={'datacollecttime':'datetime2'})
    df['utimestamp'] = timestamp
    return df

def vd(f_postfix=None):
    # http://data.kcg.gov.tw/dataset/department-of-transportation1
    url = 'http://xml11.kctmc.nat.gov.tw:8080/XML/vd_value.xml'
    out = getting.HandleNonGZippedXML(url)
    out.run()
    infos = out.xml_data['XML_Head']['Infos']['Info']
    data_dic = {}
    j = 0
    for i in infos:
        d = {k: i[k] for k in ('@vdid', '@status', '@datacollecttime')}
        for l in i['lane']:
            li = { k:l[k] for k in ('@laneoccupy','@speed','@vsrid','@vsrdir') }
            li.update(d)
            for c in l['cars']:
                k = '@'+c['@carid']+'_vol'
                v = c['@volume']
                li[k] = v
            data_dic[j] = li
            j+=1

    df = pd.DataFrame.from_dict(data_dic, orient='index')
    col = df.columns.tolist()
    col2 = { c:c.replace('@','') for c in col }
    df = df.rename(columns=col2)

    df['datacollecttime'] = pd.to_datetime(df['datacollecttime'], format='%Y/%m/%d %H:%M:%S')
    timestamp = [ int(time.mktime(tt.timetuple())) for tt in df['datacollecttime'].tolist() ]
    df = df.rename(columns={'datacollecttime':'datetime2'})
    df['utimestamp'] = timestamp
    return df

def vd5min(f_postfix=None):
    # http://data.kcg.gov.tw/dataset/department-of-transportation2
    url = 'http://xml11.kctmc.nat.gov.tw:8080/XML/vd_value5.xml'
    out = getting.HandleNonGZippedXML(url)
    out.run()
    infos = out.xml_data['XML_Head']['Infos']['Info']
    data_dic = {}
    j = 0
    for i in infos:
        d = {k: i[k] for k in ('@vdid', '@status', '@datacollecttime')}
        #print d
        for l in i['lane']:
            li = { k:l[k] for k in ('@laneoccupy','@speed','@vsrid','@vsrdir') }
            li.update(d)
            for c in l['cars']:
                k = '@'+c['@carid']+'_vol'
                v = c['@volume']
                li[k] = v
            data_dic[j] = li
            j+=1

    df = pd.DataFrame.from_dict(data_dic, orient='index')
    col = df.columns.tolist()
    col2 = { c:c.replace('@','') for c in col }
    df = df.rename(columns=col2)

    df['datacollecttime'] = pd.to_datetime(df['datacollecttime'], format='%Y/%m/%d %H:%M:%S')
    timestamp = [ int(time.mktime(tt.timetuple())) for tt in df['datacollecttime'].tolist() ]
    df = df.rename(columns={'datacollecttime':'datetime2'})
    df['utimestamp'] = timestamp
    return df

if __name__ == '__main__':

    rdf = road_level()
    print rdf.head(10)

    vdf = vd()
    print vdf.head(10)

    vdf5 = vd5min()
    print vdf5.head(10)

    busdf = bus_data()
    print busdf.head(10)
