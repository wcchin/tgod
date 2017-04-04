"""

do not use this, use convert.sh instead~~~

"""


# -*- coding: utf-8 -*-
import os
#import geopandas as gpd
import json
from topojson import topojson
from topojson.conversion import convert

def runtopojson(f1,f2):
    with open(f1) as f:
        gjs = json.load(f)
        print gjs
        tj = convert(gjs)
        print tj

#files = os.listdir('shp/boundary')
files = ['county', 'township', 'vil', 'bsu2', 'bsu1', 'bsu0']
for f in files[:4]:
    #fp = 'shp/boundary/'+f+'.shp'
    fp2 = 'geojson/boundary/'+f+'.geojson'
    fp3 = 'topojson/boundary/'+f+'.topojson'
    topojson(fp2,fp3, quantization=1e6, simplify=0.0001)
    #runtopojson(fp2,fp3)
    break
