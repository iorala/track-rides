# this file contains all the functions for track-rides

# Load required modules
import gpxpy
import gpxpy.gpx
import pandas as pd
import datetime

def read_gpx(filename):
# Import data from a gpx-file
    gpx_file = open(filename, 'r')
    gpx = gpxpy.parse(gpx_file)
    return gpx


def create_df(gpx):
    # create a pandas dataframe from a gpx-object
    df_list = []
    for track in gpx.tracks:
        for segment in track.segments:
            for no, point in enumerate(segment.points):
                df_list.append((point.time, point.latitude, point.longitude, point.elevation,
                                point.extensions[0][1].text,
                                point.speed_between(segment.points[no - 1]) * 3.6))  # * 3.6 -> m/ in km/h
    df = pd.DataFrame.from_records(df_list,
                                   columns=['time', 'latitude', 'longitude', 'elevation', 'heartrate', 'speed'])
    df.loc[0, 'speed'] = 0  # correct speed of first item (would be no-1)
    return df

def get_metadata(gpx):
    # get some metadata directly from the gpx-object
    metadata = {"start_time": gpx.get_time_bounds().start_time
                "end_time": gpx.get_time_bounds().end_time
                "duration": gpx.get_duration(),
                "distance": gpx.length_3d(),
                "climbs": get_uphill_downhill().uphill
                }