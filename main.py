from flask import Flask, redirect
from flask import render_template
from flask import request
from collections import defaultdict
import tr

app = Flask("track-ride")

# Create directories for data
savefile = "routes.json"
savedir = "uploads"
tr.create_dir(savedir)

routes = defaultdict(dict)

@app.route('/')
# For testing
def hello_world():
    routes = tr.load_routes(savefile)
    return routes

@app.route('/new_route', methods=["GET","POST"])
def new_route():
# - Strecke erstellen: new_route
#     - Statische Seite mit Formular
#     - Metadaten für Route
#         - Name
#         - Funktion (training, commute, race)
#     - Erste Fahrt erstellen - - Formular create_ride einbetten
#           - GPX-Datei hochladen *
#           - Medataten erfassen
#     -> Formularinhalt mit POST an add_route
    return render_template("new_route.html")


@app.route('/new_route_add', methods=["GET","POST"])
def new_route_add():
# Saves the route and displays the route overview after
    if request.method == "POST":
        routes = tr.load_routes(savefile)
        # neue Route speichern
        route_name = request.form['route_name']
        route_type = request.form['route_type']
        routes,id_route = tr.add_route(routes,route_name,route_type)
        # add first ride
        ride_name = request.form['ride_name']
        routes,gpx,id_ride = tr.add_ride(routes,id_route,ride_name,savedir)
        gpx_file = request.files['gpx_file']
        gpx_file.save(gpx)
        # add ride data after writing the file
        routes = tr.ride_add_data(routes, id_route, id_ride)
        tr.write_routes(routes, savefile)
    #return redirect("/view_route/", code=302)
    return redirect("/view_route/" + str(id_route), code=302)

@app.route('/new_ride_add/<selected_route>', methods=["GET","POST"])
def new_ride_add(selected_route):
# Saves the ride and displays it after
    if request.method == "POST":
        id_route = selected_route
        routes = tr.load_routes(savefile)
        # neue Route speichern
        # erste fahrt in der Route speichern
        ride_name = request.form['ride_name']
        routes,gpx,id_ride = tr.add_ride(routes,id_route,ride_name,savedir)
        gpx_file = request.files['gpx_file']
        gpx_file.save(gpx)
        # add ride data after writing the file
        routes = tr.ride_add_data(routes, id_route, id_ride)
        tr.write_routes(routes, savefile)
    return redirect("/view_ride/" + str(id_route) +"/" + str(id_ride), code=302)

@app.route('/view_route/<selected_route>', methods=["GET","POST"])
def view_route(selected_route):
# - Streckenübersicht: view_route
#     - Auf Karte Zeichnen
#     - Übersicht der gefahrenen Strecken
#     - Allgemeine Statistiken (on the fly berechnet aus den Fahrten)
#     - Button für neue Fahrt
    routes = tr.load_routes(savefile)


    return render_template("view_route.html", routes=routes, selected_route=selected_route)


@app.route('/new_ride/<selected_route>', methods=["GET","POST"])
def new_ride(selected_route):
# - Neue Fahrt: new_ride
#     - Formular ausfüllen
#     - Datei hochladen
#     - Metadaten erfassen
#         - Namen, Evtl. dropdown mit training/pendeln
#     -> Fahrt ansehen
    # routen laden, damit der Name zur verfügung steht
    routes = tr.load_routes(savefile)

    return render_template("new_ride.html", selected_route=selected_route, route_name=routes[selected_route]["name"])


@app.route('/main', methods=["GET","POST"])
# - Main page: main_page
# Could maybe be replaced by an overview page: e.g. Search/Insights/view-routes. Could maybe include excerpts from them
def main_page():
    # if request.method == "POST":
    #    return "Formular empfangen"
    #
    return render_template("main.html")

@app.route('/show_routes', methods=["GET","POST"])
# - Streckenübersicht
# - Empfängt Formularinhalte von new_route
# - Filtermöglichkeiten für Suche (Ersetzt separate Suchseite)
def show_routes():
    # if request.method == "POST":
    #     return "Formular empfangen"
    return render_template("show_routes.html")




@app.route('/view_ride/<selected_route>/<selected_ride>', methods=["GET","POST"])
def view_ride(selected_route,selected_ride):
# - Fahrten ansehen: view_ride
#     - Einzelansicht der Fahrt
#     - Lädt das GPX-Ein
#     - Auf Karte Zeichnen
#     - Statistikplots
#     -> zurück zu Strecke

    routes = tr.load_routes(savefile)
    speed_graph,elevation_graph,heartrate_graph = tr.ride_graphs(routes,selected_route,selected_ride)
    return render_template("view_ride.html", routes=routes, selected_route=selected_route, selected_ride=selected_ride, speed_graph=speed_graph,elevation_graph=elevation_graph,heartrate_graph=heartrate_graph)



@app.route('/diary', methods=["GET","POST"])
def diary():
# - Trainingstagebuch
#     - Zeigt letzte Strecken
#     - letzte fahrten mit Statistiken
#     - Fahrten pro woche
    return render_template("diary.html")

# App Ausführen
if __name__ == "__main__":
    app.run(debug=True, port=5000)
