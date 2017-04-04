# -*- coding: utf-8 -*-

import gzip
import geobuf
import geopandas as gpd

def making(fp):
    import json
    gp = 'geojson/boundary/'+fp+'.geojson.gz'
    with gzip.open(gp, 'rb') as f:
        my_jsons = f.read()
        my_json = json.loads(my_jsons)

    pbf = geobuf.encode(my_json)
    #print pbf[:100]

    with gzip.open('pbf/boundary/'+fp+'.pbf.gz', 'wb') as f:
        f.write(pbf)


def reading(fp):
    pp = 'pbf/boundary/'+fp+'.pbf.gz'
    with gzip.open(pp, 'rb') as f:
        pbf = f.read()

    my_json = geobuf.decode(pbf)
    gdf = gpd.GeoDataFrame.from_features(my_json['features'])
    print gdf.head()



def making2(bp,fp):
    import json
    gp = 'geojson/boundary/'+bp+'/'+fp+'.geojson.gz'
    with gzip.open(gp, 'rb') as f:
        my_jsons = f.read()
        my_json = json.loads(my_jsons)

    pbf = geobuf.encode(my_json)
    #print pbf[:100]

    with gzip.open('pbf/boundary/'+bp+'/'+fp+'.pbf.gz', 'wb') as f:
        f.write(pbf)


def reading2(bp,fp):
    pp = 'pbf/boundary/'+bp+'/'+fp+'.pbf.gz'
    with gzip.open(pp, 'rb') as f:
        pbf = f.read()

    my_json = geobuf.decode(pbf)
    gdf = gpd.GeoDataFrame.from_features(my_json['features'])
    print gdf.head()


if __name__ == '__main__':
    """
    files = ['county', 'township', 'village', 'bsu2']
    for fp in files:
        making(fp)
        reading(fp)
    """

    bp = 'bsu0'
    bpp = 'geojson/boundary/'+bp+'/'
    import os
    files = os.listdir(bpp)
    for fp in files:
        fp2 = fp.replace('.geojson.gz','')
        making2(bp,fp2)
        reading2(bp,fp2)

    bp = 'bsu1'
    bpp = 'geojson/boundary/'+bp+'/'
    import os
    files = os.listdir(bpp)
    for fp in files:
        fp2 = fp.replace('.geojson.gz','')
        making2(bp,fp2)
        reading2(bp,fp2)
