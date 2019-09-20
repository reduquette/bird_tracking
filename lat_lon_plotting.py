import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.dates as mpldate

birddata = pd.read_csv('bird_tracking.csv')
# print(birddata.columns)
birdids = {
    719: "Harry",
    801: "Jurgen",
    833: "Sanne",
    849: "Hilbran",
    851: "Eric",
    853: "Michelle",
    864: "Nico"
}
birdcolors = {
    719: "Blues",
    801: "Greens",
    833: "Purples",
    849: "Oranges",
    851: "Reds",
    853: "PuRd",
    864: "YlOrBr"
}


def plot_migration(birdid):
    bird_info = birddata[birddata.device_info_serial == birdid]
    time_floats = [(datetime.strptime(time,
                                      "%Y-%m-%d %H:%M:%S+00")).timestamp()
                   for time in bird_info['date_time']]
    fig = plt.figure()
    plt.scatter(
        bird_info['longitude'],
        bird_info['latitude'],
        c=time_floats,
        cmap='Blues',
        s=2)
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title(birdids[birdid] + "'s Migration")
    plt.show()


def plot_migration_all():
    # fig = plt.figure()
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.coastlines()
    ax.background_img(resolution='med', extent=[-20, 10, 10, 55])
    for birdid in birdids.keys():
        bird_info = birddata[birddata.device_info_serial == birdid]
        time_floats = [(datetime.strptime(time,
                                          "%Y-%m-%d %H:%M:%S+00")).timestamp()
                       for time in bird_info['date_time']]
        plt.scatter(
            bird_info['longitude'],
            bird_info['latitude'],
            c=time_floats,
            cmap=birdcolors[birdid],
            s=2,
            label=birdids[birdid])
    plt.title("Migration")
    ax.gridlines(draw_labels=True)
    # plt.legend()
    # ax = plt.gca()
    # leg = ax.get_legend()
    # for i in range(7):
    #     leg.legendHandles[i].set_color(birdcolors[i])
    plt.show()
