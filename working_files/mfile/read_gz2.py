# -*- coding: utf-8 -*-

import gzip
import geobuf
import geopandas as gpd

def making(fp):
    import json
    gp = 'geojson/transportation/'+fp+'.geojson.gz'
    with gzip.open(gp, 'rb') as f:
        my_jsons = f.read()
        my_json = json.loads(my_jsons)

    pbf = geobuf.encode(my_json)
    #print pbf[:100]

    with gzip.open('pbf/transportation/'+fp+'.pbf.gz', 'wb') as f:
        f.write(pbf)


def reading(fp):
    pp = 'pbf/transportation/'+fp+'.pbf.gz'
    with gzip.open(pp, 'rb') as f:
        pbf = f.read()

    my_json = geobuf.decode(pbf)
    gdf = gpd.GeoDataFrame.from_features(my_json['features'])
    print gdf.head()


if __name__ == '__main__':
    """
    files = ['airports', 'dock', 'highspeedrail_station', 'highspeedrail_way', 'highway_1', 'highway_2', 'mrt_station', 'mrt_way', 'rail_station', 'rail_way', ]
    for fp in files:
        print 'running: ',fp
        making(fp)
        reading(fp)
    """
    fp = 'mrt_way'
    print 'running: ',fp
    making(fp)
    reading(fp)
