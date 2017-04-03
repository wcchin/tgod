# -*- coding: utf-8 -*-

from tgod import get_map

def testing_boundary():

    gdf = get_map.get_boundary('bsu0_pingtung')
    print gdf.head()

def testing_transportation():
    gdf = get_map.get_transportation('highway_2')
    print gdf.head()


if __name__ == '__main__':
    #testing_boundary()
    testing_transportation()
