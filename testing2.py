# -*- coding: utf-8 -*-
import gzip
import geobuf
import geopandas as gpd
import matplotlib.pyplot as plt

from tgod import get_map

"""
import json
gp = '/media/benny/data/Workspaces/tgod/working_files/mfile/gz/geojson/transportation/highway_1.geojson.gz'
with gzip.open(gp, 'rb') as f:
    my_jsons = f.read()
    my_json = json.loads(my_jsons)
print type(my_json)
gdf = gpd.GeoDataFrame.from_features(my_json['features'])
print gdf

gdf.plot()
plt.show()


pbf = geobuf.encode(my_json)

with gzip.open('test.pbf.gz', 'wb') as f:
    f.write(pbf)
with gzip.open('test.pbf.gz', 'rb') as f:
        pbf2 = f.read()
my_json2 = geobuf.decode(pbf2)
gdf2 = gpd.GeoDataFrame.from_features(my_json2['features'])
print gdf2

gdf2.plot()
plt.show()

"""

gdf = get_map.get_transportation('highway_1')
gdf.plot()
plt.show()
