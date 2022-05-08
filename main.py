from flask import Flask
from flask import render_template
from flask import request

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
def main_page():
    # if request.method == "POST":
    #    return "Formular empfangen"
    #
    return render_template("main.html")

# - Streckenübersicht
def show_routes():
    # if request.method == "POST":
    #     return "Formular empfangen"
    return render_template("show_routes.html")

def new_route():
# - Strecke erstellen: new_route
#     - Statische Seite mit Formular
#     - Metadaten für Route
#         - Name
#         - Funktion (training, time trial, race)
#     - Erste Fahrt erstellen - - Formular create_ride einbetten
#           - GPX-Datei hochladen *
#           - Medataten erfassen
#     -> Formularinhalt mit POST an
    return render_template("new_route.html")

def new_ride():
# - Neue Fahrt: new_ride
#     - Formular ausfüllen
#     - Datei hochladen
#     - Metadaten erfassen
#         - Namen, Evtl. dropdown mit training/pendeln
#     -> Fahrt ansehen
    return render_template("new_ride.html")

# - Streckenübersicht: view_route
#     - Auf Karte Zeichnen
#     - Übersicht der gefahrenen Strecken
#     - Allgemeine Statistiken (on the fly berechnet aus den Fahrten)
#     - Button für neue Fahrt

# - Fahrten ansehen: view_ride
#     - Einzelansicht der Fahrt
#     - Auf Karte Zeichnen
#     - Statistikplots
#     -> zurück zu Strecke
# - Search page
#     - Filtert die Strecken
#     - > Streckenübersicht
# - Trainingstagebuch
#     - Zeigt letzte Strecken
#     - letzte fahrten mit Statistiken


# App Ausführen
if __name__ == "__main__":
    app.run(debug=True, port=5000)
