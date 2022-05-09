from flask import Flask
from flask import render_template
from flask import request

app.config["uploads"]

app = Flask("track-ride")


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/form', methods=["GET","POST"])
def formular():
    if request.method == "POST":
        return "Formular empfangen"
    return render_template("formular.html")


@app.route('/', methods=["GET","POST"])
# - Main page: main_page
# COuld maybe be replaced by an overview page: e.g. Search/INsights/view-routes. Could maybe include excerpts from them 
def main_page():
    # if request.method == "POST":
    #    return "Formular empfangen"
    #
    return render_template("main.html")

@app.route('/show_routes', methods=["GET","POST"])
# - Streckenübersicht
# - Empfängt Formularinhalte von new_route
# - FIltermöglichkeiten für Suche (Ersetzt separate suchseite
def show_routes():
    # if request.method == "POST":
    #     return "Formular empfangen"
    return render_template("show_routes.html")


@app.route('/new_route', methods=["GET","POST"])
def new_route():
# - Strecke erstellen: new_route
#     - Statische Seite mit Formular
#     - Metadaten für Route
#         - Name
#         - Funktion (training, time trial, race)
#     - Erste Fahrt erstellen - - Formular create_ride einbetten
#           - GPX-Datei hochladen *
#           - Medataten erfassen
#     -> Formularinhalt mit POST an view_route
    return render_template("new_route.html")


@app.route('/new_ride', methods=["GET","POST"])
def new_ride():
# - Neue Fahrt: new_ride
#     - Formular ausfüllen
#     - Datei hochladen
#     - Metadaten erfassen
#         - Namen, Evtl. dropdown mit training/pendeln
#     -> Fahrt ansehen
    return render_template("new_ride.html")

@app.route('/view_route', methods=["GET","POST"])
def view_route():
# - Streckenübersicht: view_route
#     - Auf Karte Zeichnen
#     - Übersicht der gefahrenen Strecken
#     - Allgemeine Statistiken (on the fly berechnet aus den Fahrten)
#     - Button für neue Fahrt
#     - Empfängt daten von new_ride und new_route
# if request.method == "POST":
#     return "Formular empfangen"

    return render_template("view_route.html")

@app.route('/view_ride', methods=["GET","POST"])
def view_ride():
# - Fahrten ansehen: view_ride
#     - Einzelansicht der Fahrt
#     - Auf Karte Zeichnen
#     - Statistikplots
#     -> zurück zu Strecke

    return render_template("view_ride.html")


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
