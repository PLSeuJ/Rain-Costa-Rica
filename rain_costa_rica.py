# -*- coding: utf-8 -*-
"""
rain_costa_rica: Make a few need plots of the trend of rainfall in CR.

This script shall make a timeseries of rainfall in costa rica, to investigate
the question if a 4 day periode of no rain is a common thing in january/febuary
or if other effects naming: La Niña or Climate Change have an ifluence.

Created on Mon Jan 30 22:08:48 2022

@author: jonathan
"""
import sys, os
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt


def info(path):
    """Print Information on what is contained in data"""
    path = os.path.normpath(path)
    ncdata = xr.open_dataset(path)

    print('---   NC Data   ---')
    print(ncdata.crwc)  # I am interested in this variable only

    ncdata.close()
    return


def test_homogenity(data1, *, data2, var='time'):
    """
    Check if data1 and data2 share the same location or have continous time

    data1 and data2 must be an xarray opened netCDF dataset each
    """
    print('currently under construction')

# these variables could be used to test for data homogenity
# but have no use otherwise
# lon = ncdata.variables['longitude'][:]
# lat = ncdata.variables['latitude'][:]
# time = ncdata.variables['time'][:]


def main():
    """This is the Main Function, calling all other"""

    filenames = ['-1643580761.7229903-1238-1-27fb2751-540f-4fc2-8a1b-'
                 '2d3b52232031.nc',
                  # '-1643580774.111298-29588-1-48dc09bf-b020-46ed-9525-'
                  # 'b422ea2bd266.nc',
                  # '-1643587444.750283-5100-17-2a6b948b-3047-4495-994a-'
                  # '5eff282263c3.nc',
                  # '-1643595171.5860167-3290-16-f9ccdf58-c616-48ae-b870-'
                  # '8c84fb490be6.nc',
                  # '-1643597615.2167664-2055-8-39d479ab-1e1f-4515-a20b-'
                  # '1fcf8b6482d7.nc',
                  # '-1643605275.8023982-20353-10-b0d78bc0-8684-4c90-81a0'
                  # '-735ab864b847.nc',
                 '-1643609751.1888597-7377-11-0ca0918c-4701-4c65-b596'
                 '-fa3d89b17269.nc']

    path = (r'C:/Users/jonat/Programming/rain_costa_rica/'
            r'data/adaptor.mars.internal')

    time = []
    crwc = []

    for name in filenames:
        p = str(path + name)
        info(p)

        p = os.path.normpath(p)
        ncdata = xr.open_dataset(p)

        # time = time.append(ncdata.time[:])
        x = ncdata.crwc[0:10, 0, 0].plot()
        y = ncdata.crwc.time[0:10]

        plt.show()

        # plt.plot(x, y)

        ncdata.close()
    return x, y


if __name__ == "__main__":
    x, y = main()
    # plt.plot(x[:], y[:])
