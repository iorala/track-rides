# this file contains all the functions for track-rides

# Load required modules
import gpxo
import json
from collections import defaultdict
from collections import Counter
import os

# Example structure of the routes dictionary
routes_ex = defaultdict(dict)
routes_ex[0] = {
                        "name": "Fahrt um den Zürichsee",
                        "gpx": "path to file",
                        "avg distance": 10.0,
                        "avg duration": 123,
                        "rides": [
                            {"id": 0,
                             "distance": 10.4,
                             "duration": 123,
                             "avg speed": 25,
                             "climbs": 3233}
                                ]
                    }

def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def read_track(filename):
    track = gpxo.Track(filename)
    return track


# Test-Function
def tesd(hello):
    return "Testing tr import"


def read_routes(file):
    routes = routes_structure
    return routes


def add_route(new_route,routes):
    return 1


def write_routes(file):
    return 0
# Return error message if write isn't possible


# To do
# - Draw map with Folium
# - import folium
#
# m = folium.Map(location=[40.720, -73.993],
#               zoom_start=15)
#
# loc = [(40.720, -73.993),
#        (40.721, -73.996)]
#
# folium.PolyLine(loc,
#                 color='red',
#                 weight=15,
#                 opacity=0.8).add_to(m)
# m


'''
# Not needed anymore because of using gpxo instead of gpxpy directly 
def create_df(gpx):
    # create a pandas dataframe from a gpx-object
    df_list = []
    for track in gpx.tracks:
        for segment in track.segments:
            for no, point in enumerate(segment.points):
                df_list.append((point.time, point.latitude, point.longitude, point.elevation,
                                point.extensions[0][1].text, segment.get_speed(no) * 3.6))  # * 3.6 -> m/ in km/h
    df = pd.DataFrame.from_records(df_list,
                                   columns=['time', 'latitude', 'longitude', 'elevation', 'heartrate', 'speed'])
    return df


def get_metadata(gpx):
    # get some metadata directly from the gpx-object
    metadata = {"start_time": gpx.get_time_bounds().start_time,
                "end_time": gpx.get_time_bounds().end_time,
                "duration": gpx.get_duration(),
                "distance": gpx.length_3d(),
                "climbs": gpx.get_uphill_downhill().uphill
                }
    return metadata
'''
