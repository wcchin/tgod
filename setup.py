from setuptools import setup
from setuptools import find_packages

setup(
    name="tgod",

    version="0.0.1",
    
    author="Benny Chin",
    author_email="wcchin.88@gmal.com",

    packages=['tgod', 'tgod.realtime', 'tgod.realtime.utils', 'tgod.static', 'tgod.static.maps', 'tgod.static.maps.pbfs', 'tgod.static.maps.pbfs.boundary', 'tgod.static.maps.pbfs.boundary.bsu0', 'tgod.static.maps.pbfs.boundary.bsu1', 'tgod.static.maps.pbfs.facility', 'tgod.static.maps.pbfs.recreation', 'tgod.static.maps.pbfs.transportation', 'tgod.static.maps.utils'],

    include_package_data=True,

    url="https://github.com/wcchin/tgod",

    # license="LICENSE.txt",
    description="Taiwan Geographic Open Data",

    long_description=open("README.md").read(),
    
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: GIS',

         'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2.7',
    ],

    keywords='spatial network concentration',

    install_requires=[
        "pandas",
        "geopandas",
        "geobuf",
    ],
)
