from flask import Flask
from flask import render_template
from flask import request

app = Flask("Formular")

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

@app.route('/form', methods=["GET","POST"])
def formular():
    if request.method == "POST":
        return "Formular empfangen"
    return render_template("formular.html")

# # Benötigte Seiten
# - Main page: main_page
#     - Index.html
# - Strecke erstellen: new_route
#     - Datei hochladen *
#     - Medataten erfassen
#     -> Streckenübersicht
# - Streckenübersicht: view_route
#     - Auf Karte Zeichnen
#     - Übersicht der gefahrenen Strecken
#     - Allgemeine Statistiken (on the fly berechnet aus den Fahrten)
#     - Button für neue Fahrt
# - Neue Fahrt: new_ride
#     - Datei hochladen *
#     - Metadaten erfassen
#         - Namen, Evtl. dropdown mit training/pendeln
#     -> Fahrt ansehen
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



if __name__ == "__main__":
    app.run(debug=True, port=5000)
