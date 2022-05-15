# this file contains all the functions for track-rides

# Load required modules
import gpxo
import json
from collections import defaultdict
from collections import Counter
import os
from datetime import datetime
import plotly.express as px
from plotly.offline import plot


def add_route(routes,route_name,route_type):
        id_route = len(routes)
        routes[id_route] = {
            "name": route_name,
            "type": route_type,
            "rides": defaultdict(dict)
        }
        return (routes,id_route)

def add_ride(routes,id_route,ride_name,savedir):
        id_ride = len(routes[id_route]["rides"])
        gpx = savedir + "/ride" + "_" + str(id_route) + "_" + str(id_ride) + ".gpx"
        routes[id_route]["rides"][id_ride] = {
            "name": ride_name,
            "gpx" : gpx
        }
        return (routes,gpx,id_ride)

def ride_add_data(routes,id_route,id_ride):
    # duration has to be calculated on the fly as serializing timedeltas is too much of a hassle
    track = read_track(routes[id_route]["rides"][id_ride]["gpx"])
    routes[id_route]["rides"][id_ride]["start_time"] = track.time[0].isoformat()
    routes[id_route]["rides"][id_ride]["end_time"] = track.time[-1].isoformat()
    routes[id_route]["rides"][id_ride]["distance"] = track.distance[-1]
    routes[id_route]["rides"][id_ride]["avg_speed"] = track.velocity.mean()
    routes[id_route]["rides"][id_ride]["max_speed"] = track.velocity.max()
    routes[id_route]["rides"][id_ride]["avg_heartrate"] = track.heartrate.mean()
    routes[id_route]["rides"][id_ride]["max_heartrate"] = track.heartrate.max()
    # ToDo: Recalculate the distance from the mean of all rides
    routes[id_route]["distance"]
    return routes

def ride_graphs(routes,id_route,id_ride):
    track = read_track(routes[id_route]["rides"][id_ride]["gpx"])
    fig_speed = px.line(track.data, y="velocity (km/h)", labels={'time': 'Uhrzeit', 'velocity (km/h)': 'Geschwindigkeit in km/h'})
    speed_graph = plot(fig_speed, output_type="div")
    fig_elevation = px.line(track.data, y="elevation (m)", labels={'time': 'Uhrzeit', 'elevation (m)': 'Höhenmeter'})
    elevation_graph = plot(fig_elevation, output_type="div")
    fig_heartrate = px.line(track.data, y="heartrate (bpm)", labels={'time': 'Uhrzeit', 'heartrate (bpm)': 'Herzfrequenz'})
    heartrate_graph = plot(fig_heartrate, output_type="div")
    return(speed_graph,elevation_graph,heartrate_graph)


def write_routes(routes,savefile):
    with open(savefile, "w") as open_file:
        json.dump(routes, open_file)


def load_routes(savefile):
    try:
        with open(savefile) as open_file:
            routes = json.load(open_file)
    except FileNotFoundError:
        # without a file return an empty dict, so a new file can be created
        routes = defaultdict(dict)
    return routes


def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def read_track(filename):
    track = gpxo.Track(filename)
    return track


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

