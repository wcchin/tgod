# -*- coding: utf-8 -*-
import os
import geopandas as gpd

wgs84 = "+init=epsg:4326"

def try1():
    files = ['airports', 'dock', 'highspeedrail_station', 'highspeedrail_way', 'highway_1', 'highway_2', 'mrt_station', 'mrt_way', 'rail_station', 'rail_way', ]
    for f in files:
        fp = 'shp/transportation/'+f+'.shp'
        fp2 = 'geojson/transportation/'+f+'.geojson'
        gdf = gpd.read_file(fp)
        #gdf = gdf.to_crs(epsg=4326)
        #print gdf.head()
        print 'writing geojson:', f
        gdf.to_file(fp2, driver="GeoJSON")
        #break
    #print files

def try2():
    f = 'mrt_way'
    fp = 'shp/transportation/'+f+'.shp'
    fp2 = 'geojson/transportation/'+f+'.geojson'
    gdf = gpd.read_file(fp)
    #gdf = gdf.to_crs(epsg=4326)
    #print gdf.head()
    print 'writing geojson:', f
    gdf.to_file(fp2, driver="GeoJSON")
    #break
#print files


if __name__ == '__main__':
    try2()
