import tr
import babel.dates
import dateutil.parser

'''
testliste = [
    ("2021-12-02","fahrt 1", "2km"),
    ("2020-02-02","fahrt 1", "2km"),
    ("2019-12-02","fahrt 1", "2km"),
    ]

testliste_sort = sorted(testliste)
print(testliste_sort)
'''
savefile = "routes.json"
routes = tr.load_routes(savefile)
list_rides = []
for id_route,content in routes.items():
    for id_ride, ride_content in content['rides'].items():
        date_parsed = dateutil.parser.isoparse(ride_content['start_time'])
        date_formated = babel.dates.format_datetime(date_parsed, "YYYY-MM-dd", tzinfo='Europe/Zurich')
        list_rides.append((date_formated,id_route,id_ride))

last_rides = sorted(list_rides,reverse=True)[:3]

if len(last_rides) == 0:
    no_rides = True
print(no_rides)

#for ride in last_rides:
#    print( routes[ride[1]]["rides"][ride[2]]["start_time"])

