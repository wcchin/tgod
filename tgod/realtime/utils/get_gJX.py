# -*- coding: utf-8 -*-

### snippets for downloading data from gzip/simple json/xml
### return dict object
### calling from get_and_push processes

import urllib2, httplib
import json
import StringIO
import gzip
import xml.etree.ElementTree as ET
from collections import defaultdict

class HandleGZippedJSON:
    def __init__(self, url):
        self.url = url
        self.json_data = None

    def run(self):
        #httplib.HTTPConnection.debuglevel = 1
        request = urllib2.Request(self.url)
        request.add_header('Accept-encoding', 'gzip')
        opener = urllib2.build_opener()
        f = opener.open(request)
        c_data = f.read()
        c_stream = StringIO.StringIO(c_data)
        gzipper = gzip.GzipFile(fileobj=c_stream)
        data = gzipper.read()
        #print data
        self.json_data = json.loads(data) # is a dict
        #return json.loads(data)

class HandleNonGZippedJSON:
    def __init__(self, url):
        self.url = url
        self.json_data = None

    def run(self):
        #httplib.HTTPConnection.debuglevel = 1
        request = urllib2.Request(self.url)
        request.add_header('User-Agent', 'Mozilla/5.0')
        request.add_header('Accept-encoding', 'gzip')
        opener = urllib2.build_opener()
        f = opener.open(request)
        c_data = f.read()
        #print c_data
        self.json_data = json.loads(c_data) # is a dict


class HandleGZippedXML:
    def __init__(self, url):
        self.url = url
        self.xml_data = None

    def run(self):
        #httplib.HTTPConnection.debuglevel = 1
        request = urllib2.Request(self.url)
        request.add_header('Accept-encoding', 'gzip')
        opener = urllib2.build_opener()
        f = opener.open(request)
        c_data = f.read()
        c_stream = StringIO.StringIO(c_data)
        gzipper = gzip.GzipFile(fileobj=c_stream)
        data = gzipper.read()
        #print data
        xml_root = ET.fromstring(data)
        self.xml_data = etree_to_dict(xml_root)

class HandleNonGZippedXML:
    def __init__(self, url):
        self.url = url
        self.xml_data = None

    def run(self):
        #httplib.HTTPConnection.debuglevel = 1
        request = urllib2.Request(self.url)
        #request.add_header('Accept-encoding', 'gzip')
        opener = urllib2.build_opener()
        f = opener.open(request)
        c_data = f.read()
        #print c_data
        xml_root = ET.fromstring(c_data)
        self.xml_data = etree_to_dict(xml_root)

def etree_to_dict(t):
    d = {t.tag: {} if t.attrib else None}
    children = list(t)
    if children:
        dd = defaultdict(list)
        for dc in map(etree_to_dict, children):
            for k, v in dc.iteritems():
                dd[k].append(v)
        d = {t.tag: {k:v[0] if len(v) == 1 else v for k, v in dd.iteritems()}}
    if t.attrib:
        d[t.tag].update(('@' + k, v) for k, v in t.attrib.iteritems())
    if t.text:
        text = t.text.strip()
        if children or t.attrib:
            if text:
              d[t.tag]['#text'] = text
        else:
            d[t.tag] = text
    return d

def mainXML():
    from pprint import pprint
    out = HandleGZippedXML("http://data.taipei/tisv/VDDATA")
    out.run()
    pprint(out.xml_data)

def mainJSON():
    from pprint import pprint
    out = HandleGZippedJSON("http://data.taipei/bus/BUSDATA")
    out.run()
    pprint(out.json_data)

def mainJSON2():
    from pprint import pprint
    out = HandleNonGZippedJSON("http://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=55ec6d6e-dc5c-4268-a725-d04cc262172b")
    out.run()
    pprint(out.json_data)

def mainJSON3():
    from pprint import pprint
    url = "http://data.ntpc.gov.tw/api/v1/rest/datastore/382000000A-000357-001"
    out = HandleNonGZippedJSON(url)
    out.run()
    pprint(out.json_data)

def mainXML2():
    url = 'http://xml11.kctmc.nat.gov.tw:8080/XML/roadlevel_value.xml'
    out = HandleNonGZippedXML(url)
    out.run()
    print out.xml_data

if __name__ == '__main__':
    mainXML2()
