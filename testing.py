# -*- coding: utf-8 -*-



def testing_taipei_transport_data():
    from tgod import taipei_transport as tt

    busdf = tt.bus()
    print busdf.head(10)

    busevdf = tt.busevent()
    print busevdf.head(10)

    vddf = tt.vd()
    print vddf.head(10)

    udf = tt.bikeshare()
    print udf.head(10)

    mdf = tt.mrt()
    print mdf.head(10)

def testing_newtaipei_transport_data():
    from tgod import newtaipei_transport as nt

    vdf = nt.vd() # every min
    print vdf.head(10)

    udf = nt.bikeshare() # every min
    print udf.head(10)

def testing_kaohsiung_transport_data():
    from tgod import kaohsiung_transport as kh

    rdf = kh.road_level()
    print rdf.head(10)

    vdf = kh.vd()
    print vdf.head(10)

    vdf5 = kh.vd5min()
    print vdf5.head(10)

if __name__ == '__main__':
    #testing_taipei_transport_data()
    #testing_newtaipei_transport_data()
    testing_kaohsiung_transport_data()
