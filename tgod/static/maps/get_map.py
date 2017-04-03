# -*- coding: utf-8 -*-
import os
import pandas as pd

from utils import read_from_path

def _get_key(obj, r=False):
    paths_config = 'file_loc_'+obj+'.csv'
    df_path = pd.read_csv(paths_config)
    if not r:
        for k in df_path.key.tolist():
            print k
    else:
        return df_path.key.tolist()

def get_boundary_key(r=False):
    #boundary_paths = 'file_loc_boundary.csv'
    df_path = _get_key('boundary', r=r)
    if r:
        return df_path

def get_transportation_key(r=False):
    df_path = _get_key('transportation', r=r)
    if r:
        return df_path

def _get_geodf(obj, akey):
    #print os.getcwd()
    fdir = os.path.dirname(__file__)
    paths_config = fdir+'/'+'file_loc_'+obj+'.csv'
    #print paths_config
    df_path = pd.read_csv(paths_config)
    df_path.set_index('key', inplace=True)
    dic_path = df_path.to_dict(orient='index')
    if akey in dic_path:
        fp = fdir+'/'+dic_path[akey]['path']
        print fp
        gdf = read_from_path.reading(fp)
        return gdf.head()
    else:
        print 'key not found, try checking the bkey: print_bkey()'
        print 'not returning anything'
        return None

def get_boundary(bkey):
    gdf = _get_geodf('boundary', bkey)
    return gdf

def get_transportation(tkey):
    gdf = _get_geodf('transportation', tkey)
    return gdf

def main_test():
    #get_boundary_key()
    #get_transportation_key()

    #gdf = get_boundary('bsu0_pingtung')
    #print gdf.head()

    #gdf = get_transportation('highway_2')
    #print gdf.head()
    pass

if __name__ == '__main__':
    main_test()
