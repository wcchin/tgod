# -*- coding: utf-8 -*-

import gzip
import geobuf
import geopandas as gpd

def reading(filepath):
    #import os
    #print os.getcwd(), filepath
    with gzip.open(filepath, 'rb') as f:
        pbf = f.read()

    my_json = geobuf.decode(pbf)
    gdf = gpd.GeoDataFrame.from_features(my_json['features'])
    #print gdf.head()
    return gdf


if __name__ == '__main__':

    fp = 'mrt_way'
    print 'running: ',fp
    reading(fp)
