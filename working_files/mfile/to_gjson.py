# -*- coding: utf-8 -*-
import os
import geopandas as gpd

wgs84 = "+init=epsg:4326"

def try1():
    files = ['county', 'township', 'vil', 'bsu2', 'bsu1', 'bsu0']
    for f in files:
        fp = 'shp/boundary/'+f+'.shp'
        fp2 = 'geojson/boundary/'+f+'.geojson'
        gdf = gpd.read_file(fp)
        gdf = gdf.to_crs(epsg=4326)
        #print gdf.head()
        print 'writing geojson:', f
        gdf.to_file(fp2, driver="GeoJSON")
        #break
    #print files

def manage_bsu():
    cf = 'county'
    bf = 'bsu1'
    cdf = gpd.read_file('shp/boundary/'+cf+'.shp')
    cdf2 = cdf[['countyid','sname']]
    cdf2.set_index('countyid', inplace=True)
    #print cdf2
    cdic = cdf2.to_dict(orient='index')
    cdic = { k:v['sname'] for k,v in cdic.iteritems() }
    #print cdic
    cids = cdf2.index.tolist()
    #print cids

    bdf = gpd.read_file('shp/boundary/'+bf+'.shp')
    #bdf = bdf.to_crs(epsg=4326)
    #print bdf.head(10)
    #fp2 = 'geojson/boundary/'+bf+'/'+f+'.geojson'
    for c in cids:
        temp_bdf = bdf[bdf['countyid']==c]
        temp_bdf = temp_bdf.to_crs(epsg=4326)
        cname = cdic[c]
        fp2 = 'geojson/boundary/'+bf+'/'+cname+'.geojson'
        print 'writing geojson:', fp2
        temp_bdf.to_file(fp2, driver="GeoJSON")


if __name__ == '__main__':
    manage_bsu()
