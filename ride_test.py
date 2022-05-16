import gpxo
from datetime import datetime
from datetime import timedelta
import folium

import plotly.express as px
from plotly.offline import plot

import pandas as pd
track = gpxo.Track('activity_1.gpx')
#print(track.data.reset_index().iloc[0]["time"])
# print(track.data)
# print(track.data)
# print(track.distance[-1])
# print(track.seconds[-1])
# print(track.data.iloc[0])
duration = track.time[-1] - track.time[0]
start_time = track.time[0].isoformat()
end_time = track.time[-1].isoformat()


#duration = end_time - start_time

distance = track.distance[-1]
avg_speed = track.velocity.mean()
max_speed = track.velocity.max()
avg_heartrate = track.heartrate.mean()
max_heartrate = track.heartrate.max()
#fig = px.line(x=track.time, y=track.velocity, title="Geschwindigkeit")
# fig = px.line(track.data, y="velocity (km/h)", labels={'time': 'Uhrzeit', 'velocity (km/h)':'Geschwindigkeit in km/h'})
# fig.show()
# fig = px.line(track.data, y="elevation (m)", labels={'time': 'Uhrzeit', 'elevation (m)':'Höhenmeter'})
# fig.show()
# fig = px.line(track.data, y="heartrate (bpm)", labels={'time': 'Uhrzeit', 'heartrate (bpm)':'Herzfrequenz'})
# fig.show()
#print(track.data.iloc[:,[0,1]])
loc = list(track.data.iloc[:,[0,1]].itertuples(index=False, name=None))
# - Draw map with Folium
# - import folium
#
m = folium.Map(location=[track.latitude[0], track.longitude[0]],zoom_start=15)
#
# loc = [(40.720, -73.993),
#        (40.721, -73.996)]
#
folium.PolyLine(loc,color='red',weight=15,opacity=0.8).add_to(m)
m