import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.dates as mpldate

birddata = pd.read_csv(
    'bird_tracking.csv', header=0, parse_dates=['date_time'])

birdids = {
    719: "Harry",
    801: "Jurgen",
    833: "Sanne",
    849: "Hilbran",
    851: "Eric",
    853: "Michelle",
    864: "Nico"
}


def plot_speed(bird_id):
    bird = birddata[birddata.device_info_serial == bird_id]
    speed = bird['speed_2d']
    times = bird['date_time']

    fig = plt.figure()
    plt.scatter(times, speed, s=2)
    plt.xlabel("Date")
    plt.ylabel("Speed (m/s)")
    plt.show()


def plot_speed_restricted(bird_id, start_time, stop_time):
    bird = birddata[birddata.device_info_serial == bird_id]
    bird = bird[(bird['date_time'] > start_time)
                & (bird['date_time'] < stop_time)]
    speed = bird['speed_2d']
    times = bird['date_time']

    fig = plt.figure()
    plt.scatter(times, speed, s=2)
    plt.xlabel("Date")
    plt.ylabel("Speed (m/s)")
    plt.title("Speed Data \n" + start_time + " - " + stop_time)
    plt.show()


start = '2014-01'
stop = '2014-02'
plot_speed_restricted(719, start, stop)
